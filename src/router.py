def decide_route(extracted_fields, missing_fields):
    description = extracted_fields.get("Description", "").lower()
    claim_type = extracted_fields.get("Claim Type", "").lower()
    damage = int(extracted_fields.get("Estimated Damage", "0"))

    if missing_fields:
        return "Manual Review", "Mandatory fields are missing"

    if any(word in description for word in ["fraud", "inconsistent", "staged"]):
        return "Investigation Flag", "Suspicious keywords found in description"

    if claim_type == "injury":
        return "Specialist Queue", "Claim type is injury"

    if damage < 25000:
        return "Fast-track", "Estimated damage below 25,000"

    return "Standard Processing", "Does not meet fast-track criteria"
