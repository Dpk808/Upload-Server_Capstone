import json

with open('reports/snyk.json') as f:
    data = json.load(f)

print("Suggested dependency fixes:")
for vuln in data.get('vulnerabilities', []):
    print(f"Package: {vuln['packageName']}, Version: {vuln.get('version')}, Severity: {vuln['severity']}")
    print(f"Suggested fix: {vuln.get('upgradePath', 'Check Snyk advisory')}")