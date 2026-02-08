Insurance Claim Agent

## Overview
This project implements a lightweight autonomous agent to process FNOL (First Notice of Loss) documents.
The agent extracts key information, identifies missing or inconsistent fields, classifies claims, and routes them
to the appropriate workflow with an explanation.

## Features
- FNOL document ingestion (TXT format)
- Structured field extraction
- Mandatory field validation
- Rule-based claim routing
- Explainable JSON output

## Routing Rules
- Estimated damage < 25,000 → Fast-track
- Missing mandatory fields → Manual Review
- Keywords like "fraud", "inconsistent", "staged" → Investigation Flag
- Claim type = Injury → Specialist Queue

## Technologies Used
- Python 3.9+
- Standard Python libraries
- Rule-based text parsing
- Modular architecture
- AI tools used during development for faster prototyping

## Project Structure
Insurance-Claim-Agent/
├── data/
│   ├── FNOL1.txt
│   ├── FNOL2.txt
│   ├── FNOL3.txt
│   └── FNOL4.txt
├── src/
│   ├── agent.py
│   ├── extractor.py
│   ├── validator.py
│   ├── router.py
│   └── main.py
├── requirements.txt
└── README.md


## How to Run
python src/main.py data/FNOL1.txt

