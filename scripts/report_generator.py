import json
from pathlib import Path

summary = []

# Load Snyk
snyk_file = Path("reports/snyk.json")
if snyk_file.exists():
    with snyk_file.open() as f:
        snyk_data = json.load(f)
        for v in snyk_data.get("vulnerabilities", []):
            summary.append(f"SNYK: {v['packageName']} - {v['severity']}")

# Load Trivy
trivy_file = Path("reports/trivy-fs.json")  # Make sure this matches the Trivy output file
if trivy_file.exists():
    with trivy_file.open() as f:
        trivy_data = json.load(f)
        for r in trivy_data.get("Results", []):
            for v in r.get("Vulnerabilities", []):
                summary.append(f"TRIVY: {v['VulnerabilityID']} - {v['Severity']}")

# Save consolidated summary
Path("reports/summary.html").write_text("<br>".join(summary))
print("Summary report generated at reports/summary.html")
