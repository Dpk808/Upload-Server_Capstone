## Automated Security & Manual Remediation Strategy

This project follows a **robust DevSecOps approach** where security vulnerabilities are automatically detected but **not auto-remediated**.

### How It Works
- Static code issues are detected using **SonarCloud**
- Dependency vulnerabilities are identified using **Snyk**
- Filesystem vulnerabilities are scanned using **Trivy**
- All security findings are exported as **JSON reports**
- Reports are uploaded as **GitHub Actions artifacts**

### Manual Fix Policy (Intentional Design)
Auto-fixing vulnerabilities directly in the pipeline can introduce breaking changes or unstable dependencies.

Therefore:
- Developers **review security reports manually**
- Fixes are applied consciously and tested locally
- This ensures **code stability, accountability, and auditability**

This design mirrors **real-world enterprise DevSecOps pipelines**, where security teams and developers collaborate on remediation rather than relying on blind automation.
