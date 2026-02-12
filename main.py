from auditor import SecurityAuditor

def run_security_audit_demo():
    print("="*60)
    print("🚀 AUTOMATED SECURITY INTENT AUDIT")
    print("="*60)
    
    auditor = SecurityAuditor()

    test_cases = [
        {
            "name": "Access Control Audit (IAM vs RBAC Policy)",
            "policy": "policies/hr_access_intent.txt",
            "config": "configs/iam_payroll_config.json"
        },
        {
            "name": "Network Segmentation Audit (Firewall vs Isolation Policy)",
            "policy": "policies/network_isolation_rules.txt",
            "config": "configs/network_firewall_rules.yaml"
        }
    ]

    for case in test_cases:
        print(f"\n🔍 Running: {case['name']}...")
        print(f"📄 Policy: {case['policy']}")
        print(f"⚙️ Config: {case['config']}")
        print("-" * 40)
        
        try:
            report = auditor.audit(case['policy'], case['config'])
            print(report)
        except Exception as e:
            print(f"❌ Error during audit: {e}")
        
        print("-" * 60)

    print("\n✅ Audit Demo Completed.")

if __name__ == "__main__":
    run_security_audit_demo()