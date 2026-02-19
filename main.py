from colorama import Fore, Style, init

from auditor import SecurityAuditor

init(autoreset=True)


def run_security_audit_demo():
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.CYAN + Style.BRIGHT + "🚀 AUTOMATED SECURITY INTENT AUDIT")
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)

    auditor = SecurityAuditor()

    test_cases = [
        {
            "name": "Access Control Audit (IAM vs RBAC Policy)",
            "policy": "policies/hr_access_intent.txt",
            "config": "configs/iam_payroll_config.json",
        },
        {
            "name": "Network Segmentation Audit (Firewall vs Isolation Policy)",
            "policy": "policies/network_isolation_rules.txt",
            "config": "configs/network_firewall_rules.yaml",
        },
    ]

    for case in test_cases:
        print(f"\n🔍 {Fore.YELLOW}Running: {case['name']}...")
        print(f"{Fore.WHITE}📄 Policy: {case['policy']}")
        print(f"{Fore.WHITE}⚙️  Config: {case['config']}")
        print(Fore.BLUE + "-" * 40)

        try:
            report = auditor.audit(case["policy"], case["config"])
            print(Fore.GREEN + report)
        except Exception as e:
            print(f"{Fore.RED}❌ Error during audit: {e}")

        print(Fore.BLUE + "-" * 60)

    print(Fore.CYAN + Style.BRIGHT + "\n✅ Audit Demo Completed.")


if __name__ == "__main__":
    run_security_audit_demo()
