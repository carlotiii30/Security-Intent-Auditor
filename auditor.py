import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

class SecurityAuditor:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

    def read_file(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()

    def audit(self, policy_path, config_path):
        policy = self.read_file(policy_path)
        config = self.read_file(config_path)

        system_template = """
        You are an expert Cybersecurity Auditor certified by ISC2. 
        Your task is to compare a "Security Intent" (administrative policy) against a "Technical Configuration".
        
        Analyze the following based on the CIA Triad, Least Privilege, and Defense in Depth:
        1. Identify any direct violations.
        2. Explain the risk associated with the violation.
        3. Suggest a remediation step.
        
        Be concise, professional, and technical.
        """
        
        user_template = """
        ### SECURITY INTENT (Policy):
        {policy}

        ### TECHNICAL CONFIGURATION:
        {config}

        ### AUDIT REPORT:
        """

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_template),
            ("user", user_template)
        ])

        chain = prompt | self.llm
        response = chain.invoke({"policy": policy, "config": config})
        
        return response.content