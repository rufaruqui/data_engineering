import requests
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# ── Fetch ──────────────────────────────────────────────────────────────────────
url = (
    "https://hapi.fhir.org"
    "/baseR4/Observation"
    "?_count=50&_format=json"
)

bundle = requests.get(url).json()
entries = bundle.get("entry", [])

# ── Challenge 1: Are LOINC codes present on every Observation? ─────────────────
# FHIR Observation.code.coding[] may be empty, absent, or contain non-LOINC
# systems (SNOMED, local codes).  We count how many resources have at least one
# coding entry whose system is the official LOINC URI.
LOINC_SYSTEM = "http://loinc.org"

missing_loinc = 0
for e in entries:
    r = e["resource"]
    codings = r.get("code", {}).get("coding", [])
    has_loinc = any(c.get("system") == LOINC_SYSTEM for c in codings)
    if not has_loinc:
        missing_loinc += 1

print(f"Entries without a LOINC code: {missing_loinc}/{len(entries)}")

# ── Challenge 2: What field carries patient identity? ──────────────────────────
# Observation.subject is a FHIR Reference — typically {"reference": "Patient/123"}.
# It is NOT a bare patient ID; we must parse the reference string.
# The field may be absent for unlinked or device observations.
def extract_patient_id(resource: dict) -> str | None:
    ref = resource.get("subject", {}).get("reference", "")
    if ref.startswith("Patient/"):
        return ref.split("/", 1)[1]
    return None  # urn:uuid refs, Device refs, or missing subject

# ── Flatten Bundle.entry[] → rows ─────────────────────────────────────────────
rows = []
for e in entries:
    r = e["resource"]
    codings = r.get("code", {}).get("coding", [])
    loinc_code = next(
        (c.get("code") for c in codings if c.get("system") == LOINC_SYSTEM),
        None,
    )
    rows.append({
        "id":           r.get("id"),
        "status":       r.get("status"),
        "patient_id":   extract_patient_id(r),
        "loinc":        loinc_code,
        "display":      next(
                            (c.get("display") for c in codings if c.get("system") == LOINC_SYSTEM),
                            None,
                        ),
        "value":        r.get("valueQuantity", {}).get("value"),
        "unit":         r.get("valueQuantity", {}).get("unit"),
        "effective_dt": r.get("effectiveDateTime"),
    })

# ── Challenge 3: Flatten into a Spark DataFrame ────────────────────────────────
# SparkSession must be created before any DataFrame operation.
# In a notebook / local test, use master("local[*]"); on a cluster, omit it.
spark = (
    SparkSession.builder
    .appName("FHIR-Observations")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame(rows)

# Cast numeric value column — arrives as Python float but make it explicit.
df = df.withColumn("value", F.col("value").cast("double"))

df.printSchema()
df.show(10, truncate=False)

# Quick audit: null rate per column
total = df.count()
null_counts = {c: df.filter(F.col(c).isNull()).count() for c in df.columns}
print("\nNull counts per column (out of", total, "rows):")
for col, n in null_counts.items():
    print(f"  {col:15s}: {n:3d}  ({100*n/total:.0f}%)")
