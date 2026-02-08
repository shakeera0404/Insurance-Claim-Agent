import sys
import json
from agent import InsuranceClaimAgent

def read_fnol(file_path):
    with open(file_path, "r") as file:
        return file.read()

if __name__ == "__main__":
    fnol_path = sys.argv[1]
    content = read_fnol(fnol_path)

    agent = InsuranceClaimAgent()
    result = agent.process_claim(content)

    print(json.dumps(result, indent=4))
