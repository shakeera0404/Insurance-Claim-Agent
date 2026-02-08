from extractor import extract_fields
from validator import find_missing_fields
from router import decide_route

class InsuranceClaimAgent:
    def process_claim(self, text):
        extracted_fields = extract_fields(text)
        missing_fields = find_missing_fields(extracted_fields)
        route, reason = decide_route(extracted_fields, missing_fields)

        return {
            "extractedFields": extracted_fields,
            "missingFields": missing_fields,
            "recommendedRoute": route,
            "reasoning": reason
        }
