import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()


class SecurityAuditor:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )

    def read_file(self, file_path):
        with open(file_path, "r") as f:
            return f.read()

    def audit(self, policy_path, config_path):
        policy = self.read_file(policy_path)
        config = self.read_file(config_path)

        system_template = """
            You are a Senior Cybersecurity Auditor (ISC2 Certified). 
            Your goal is to produce a highly readable, professional audit report.

            FOLLOW THIS FORMAT RIGIDLY:
            1. Use **BOLD CAPS** for section headers (e.g., **FINDING 1: [TITLE]**).
            2. Use `backticks` for technical values like ports, IP addresses, or roles.
            3. Use bullet points for risks.
            4. Use a "---" horizontal rule between findings.

            Structure each finding as:
            **FINDING [X]: [Brief Description]**

            - **Direct Violation:** [Description]

            - **Risk Analysis:** [Bullet points mentioning CIA Triad]
            
            - **Remediation:** [Step-by-step fix]
            """

        user_template = """
        ### SECURITY INTENT (Policy):
        {policy}

        ### TECHNICAL CONFIGURATION:
        {config}

        ### AUDIT REPORT:
        """

        prompt = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", user_template)]
        )

        chain = prompt | self.llm
        response = chain.invoke({"policy": policy, "config": config})

        return response.content
