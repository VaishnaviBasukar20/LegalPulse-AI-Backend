from dotenv import load_dotenv
import fitz
import os
import json
from google import genai
from constants import SYSTEM_PROMPT, MODEL
from schemas import ContractAnalysis

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)

async def analyze_contract(text):
    try:
        full_prompt = f"{SYSTEM_PROMPT}\n\nContract:\n{text}"

        response = client.models.generate_content(
            model=MODEL,
            contents=full_prompt
        )

        result_text = response.text.strip()
        result_text = result_text.replace("```json", "").replace("```", "").strip()
        try:
            data = json.loads(result_text)

            validated = ContractAnalysis(**data)
            return validated
        except:
            return {
  "parties": [],
  "contract_duration": "",
  "renewal_terms": "",
  "payment_terms": "",
  "termination_clauses": "",
  "confidentiality_terms": "",
  "liability_clauses": "",
  "ip_ownership": "",
  "plain_english_summary": f"LLM returned invalid JSON\n{result_text}",
  "risk_flags": {
      "auto_renewal_risk": {
          "level": "Low | Medium | High",
          "description": ""
      },
      "liability_risk": {
          "level": "Low | Medium | High",
          "description": ""
      },
      "missing_exit_clause": {
          "level": "Low | Medium | High",
          "description": ""
      },
      "indemnity_risk": {
          "level": "Low | Medium | High",
          "description": ""
      },
      "ip_ownership_risk": {
          "level": "Low | Medium | High",
          "description": ""
      },
      "other_risks": [
          {
              "level": "Low | Medium | High",
              "description": ""
          }
      ]
  }
}

    except Exception as e:
        return {"error": str(e)}

async def extract_text_from_pdf(file):
    pdf_bytes = await file.read()

    if not pdf_bytes:
        raise ValueError("Empty PDF file.")

    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    except Exception as e:
        raise ValueError(f"Invalid PDF file: {str(e)}")

    text = ""
    for page in doc:
        text += page.get_text()

    return text.strip()

def categorize_risks(data):
    risks = []

    if "automatic renewal" in data["renewal_terms"].lower():
        risks.append("AUTO-RENEWAL RISK")

    if "unlimited liability" in data["liability_clauses"].lower():
        risks.append("HIGH LIABILITY RISK")

    if data["termination_clauses"] == "Not specified":
        risks.append("MISSING EXIT CLAUSE")

    return risks