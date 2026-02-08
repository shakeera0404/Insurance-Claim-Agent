MANDATORY_FIELDS = [
    "Policy Number",
    "Policyholder Name",
    "Policy Effective Dates",
    "Incident Date",
    "Incident Time",
    "Incident Location",
    "Description",
    "Claimant",
    "Contact Details",
    "Asset Type",
    "Asset ID",
    "Estimated Damage",
    "Claim Type",
    "Attachments",
    "Initial Estimate"
]

def find_missing_fields(extracted_fields):
    missing = []

    for field in MANDATORY_FIELDS:
        if field not in extracted_fields or not extracted_fields[field]:
            missing.append(field)

    return missing
