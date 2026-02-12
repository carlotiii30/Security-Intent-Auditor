# Intent-Based Security Auditor 🛡️🤖

This is a security tool designed to bridge the gap between high-level administrative policies and technical configurations. By leveraging **Large Language Models (LLMs)** and **LangChain**, this tool audits whether technical implementations align with the original security intent of an organization.

---

## 🌟 Project Overview

In modern IT environments, there is often a "translation gap" between security policies and actual configurations. This project applies the core principles from the **ISC2 Certified in Cybersecurity (CC)** certification—such as the **CIA Triad**, **Least Privilege**, and **Defense in Depth**—to automate the auditing process using AI.

## 🚀 Key Features

- **Intent Verification:** Analyzes if technical rules (Firewalls, IAM, JSON configs) honor the "Security Intent" described in natural language policies.
- **Access Control Auditing:** Specifically designed to detect violations in **RBAC** (Role-Based Access Control) and **Principle of Least Privilege**.
- **Policy Alignment:** Evaluates **Data Handling** and **Acceptable Use Policies** against active system configurations.
- **Risk Mitigation:** Automatically identifies discrepancies and suggests remediation steps based on security best practices.

## 🛠️ Technical Stack

- **Language:** Python 3.10+
- **AI Orchestration:** LangChain
- **LLM Integration:** OpenAI / Anthropic / Local LLMs
- **Security Framework:** Grounded in **ISC2 CC** standards (Access Control & Security Operations).

## 📖 How it Works

1. **Define Intent:** Provide a natural language policy (e.g., _"Only the Finance Role should have access to payroll databases"_).
2. **Ingest Technical Data:** Load configuration files (JSON, YAML) or access logs.
3. **AI Audit:** The engine compares the "Sujeto" (Subject) and "Objeto" (Object) against the established "Reglas" (Rules).
4. **Reporting:** Generates a report highlighting where the technical implementation fails to meet the administrative intent.

## 📂 Repository Structure

- `/policies`: Sample administrative security policies (Security Intents).
- `/configs`: Example technical configuration files (Firewall rules, IAM policies).
- `auditor.py`: Core logic for AI-driven policy auditing.
- `main.py`: Entry point to run the automated audit demo.
- `pyproject.toml`: Poetry configuration and dependency management.

## 🛠️ Installation & Setup

This project uses **Poetry** for dependency management.

1. **Install dependencies:**
   ```bash
   poetry install
   ```
2. **Set up environment variables:** Create a `.env` file and add your `OPENAI_API_KEY`.

3. **Run the demo:**
   ```bash
   poetry run python main.py
   ```

---

> _This project validates the competencies acquired in the **ISC2 Certified in Cybersecurity (CC)** program (Completed Feb 2026)._
