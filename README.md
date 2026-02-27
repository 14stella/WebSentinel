🛡️ WebSentinel – Integrated Security Analysis Platform

📌 Overview
WebSentinel is a lightweight integrated Static Application Security Testing (SAST) platform designed to perform automated security analysis using multiple security tools in a unified pipeline.

The platform integrates:

🔍 Bandit – Python security vulnerability detection

🔎 Semgrep – Multi-language static security analysis

WebSentinel executes both tools against a target codebase, analyzes the results, removes duplicate and low-confidence findings, and generates a single consolidated developer-friendly security report.

🎯 Objectives

Provide unified security scanning from multiple tools

Reduce false positives by filtering low-severity findings

Remove duplicate vulnerabilities across tools

Generate clean, readable text-based reports

Maintain modular and scalable architecture

🏗️ Project Structure
security-lab/
│
├── tools/
│   ├── bandit/
│   └── semgrep/
│
├── targets/
│   ├── py_project/
│   └── js_project/
│
├── reports/
│   ├── raw/
│   └── final_report.txt
│
├── engine/
│   └── websentinel.py
│
└── README.md
⚙️ Tools Used
1️⃣ Bandit

Python-focused static security analyzer

Detects insecure coding practices

Identifies command injection, insecure deserialization, hardcoded secrets, etc.

2️⃣ Semgrep

Multi-language static analysis engine

Uses rule-based pattern matching

Detects injection flaws, secret leaks, insecure APIs

🚀 Installation & Setup
Step 1 – Clone or Create Project Structure
mkdir security-lab
cd security-lab

Create folders:

mkdir tools targets reports engine
mkdir reports/raw
Step 2 – Install Bandit
cd tools
mkdir bandit
cd bandit
python3 -m venv venv
source venv/bin/activate
pip install bandit
deactivate
Step 3 – Install Semgrep
cd ~/security-lab/tools
mkdir semgrep
cd semgrep
python3 -m venv venv
source venv/bin/activate
pip install semgrep
deactivate

🧠 How It Works
WebSentinel runs Bandit and Semgrep on the target directory.
Raw JSON results are stored inside:

reports/raw/

The engine:
Extracts findings
Removes duplicates
Filters LOW/INFO severity
Generates final consolidated report

Final output is generated in:

reports/final_report.txt
▶️ Running the Scanner

Navigate to engine directory:

cd ~/security-lab/engine

Run scan:

python3 websentinel.py <target_folder>

Example:

python3 websentinel.py ~/security-lab/targets/py_project

OR

python3 websentinel.py ~/security-lab/targets/js_project

📄 Sample Output Report
===== WEB SENTINEL SECURITY ANALYSIS REPORT =====

Total Valid Findings: 4

1. Tool: Bandit
   File: vulnerable_app.py
   Line: 15
   Severity: HIGH
   Issue: Use of unsafe pickle deserialization
------------------------------------------------------------
2. Tool: Semgrep
   File: vulnerable_app.py
   Line: 8
   Severity: HIGH
   Issue: Potential command injection
------------------------------------------------------------

🧹 False Positive Handling

WebSentinel improves result accuracy by:
Removing duplicate findings
Filtering LOW and INFO severity issues
Consolidating findings from multiple tools

⚠️ Note: No SAST system can guarantee 100% false-positive elimination.
However, WebSentinel significantly reduces noise compared to raw tool outputs.

🔐 Supported Languages

Python (Bandit + Semgrep)

JavaScript (Semgrep)

📌 Current Capabilities

✔ Multi-tool integrated scanning
✔ Duplicate removal
✔ Low severity filtering
✔ Unified reporting
✔ Clean text-based report output

🔮 Future Enhancements

Confidence scoring (cross-tool validation)
Severity aggregation summary
CVSS-based risk scoring
HTML dashboard report
CI/CD pipeline integration
Web UI (SonarQube-style interface)
