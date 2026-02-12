# Security Policies Repository 📋

This directory contains the **Administrative Security Policies** that define the "Security Intent" of the organization. These documents serve as the ground truth for the **Sentinel-AI** auditor.

## 🛡️ Governance Framework

The policies here are modeled after the principles of the **ISC2 Certified in Cybersecurity (CC)** framework, focusing on:

- **The CIA Triad:** Ensuring that every policy addresses Confidentiality, Integrity, or Availability.
- **Access Control Models:** Implementing Role-Based Access Control (RBAC) and the Principle of Least Privilege.
- **Data Handling:** Defining how data should be classified, labeled, and protected throughout its lifecycle.

## 📝 Policy Structure

Each `.txt` file follows a specific format to be correctly interpreted by the AI engine:

1.  **Intent Identifier:** Starts with `SECURITY INTENT:` to provide clear context to the LLM.
2.  **Context:** Defines the "Subject" (who), the "Object" (what), and the "Rules" (how/when).
3.  **Security Constraint:** Explicitly mentions the security requirement (e.g., Encryption, MFA, Isolation).

## 📂 Included Examples

- `hr_access_policy.txt`: Demonstrates **Access Control** and Least Privilege for sensitive HR data.
- `data_protection_standards.txt`: Focuses on **Data Handling** and encryption requirements for classified information.
- `network_isolation_rules.txt`: Applies **Defense in Depth** strategies to network segment isolation.

---

_Note: These policies are designed to be compared against technical configuration files located in the `/configs` directory._
