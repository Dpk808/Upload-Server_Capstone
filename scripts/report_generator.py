import json
from pathlib import Path

summary = []

with open('reports/snyk.json') as f:
    snyk_data = json.load(f)
    for v in snyk_data.get('vulnerabilities', []):
        summary.append(f"SNYK: {v['packageName']} - {v['severity']}")

with open('reports/trivy-fs.json') as f:
    trivy_data = json.load(f)
    for r in trivy_data.get('Results', []):
        for v in r.get('Vulnerabilities', []):
            summary.append(f"TRIVY: {v['VulnerabilityID']} - {v['Severity']}")

Path('reports/summary.html').write_text('<br>'.join(summary))
print("Summary report generated at reports/summary.html")