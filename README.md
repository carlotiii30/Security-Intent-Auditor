# Intent-Based Security Auditor 🛡️🤖

This is a security tool designed to bridge the gap between high-level administrative policies and technical configurations. By leveraging **Large Language Models (LLMs)** and **LangChain**, this tool audits whether technical implementations align with the original security intent of an organization.

---

## 🌟 Project Overview
In modern IT environments, there is often a "translation gap" between security policies and actual configurations. This project applies the core principles from the **ISC2 Certified in Cybersecurity (CC)** certification—such as the **CIA Triad**, **Least Privilege**, and **Defense in Depth**—to automate the auditing process using AI.

## 🚀 Key Features
* **Intent Verification:** Analyzes if technical rules (Firewalls, IAM, JSON configs) honor the "Security Intent" described in natural language policies.
* **Access Control Auditing:** Specifically designed to detect violations in **RBAC** (Role-Based Access Control) and **Principle of Least Privilege**.
* **Policy Alignment:** Evaluates **Data Handling** and **Acceptable Use Policies** against active system configurations.
* **Risk Mitigation:** Automatically identifies discrepancies and suggests remediation steps based on security best practices.

## 🛠️ Technical Stack
* **Language:** Python 3.10+
* **AI Orchestration:** LangChain
* **LLM Integration:** OpenAI / Anthropic / Local LLMs
* **Security Framework:** Grounded in **ISC2 CC** standards (Access Control & Security Operations).

## 📖 How it Works
1. **Define Intent:** Provide a natural language policy (e.g., *"Only the Finance Role should have access to payroll databases"*).
2. **Ingest Technical Data:** Load configuration files (JSON, YAML) or access logs.
3. **AI Audit:** The engine compares the "Sujeto" (Subject) and "Objeto" (Object) against the established "Reglas" (Rules).
4. **Reporting:** Generates a report highlighting where the technical implementation fails to meet the administrative intent.

## 📂 Repository Structure
* `/policies`: Sample administrative security policies.
* `/configs`: Example technical configuration files (Firewall rules, IAM policies).
* `auditor.py`: Core logic for AI-driven policy auditing.
* `requirements.txt`: Project dependencies.

---
*Created as a practical application of the ISC2 CC certification to solve real-world IT security challenges.* [cite: 1, 3, 4, 5]
