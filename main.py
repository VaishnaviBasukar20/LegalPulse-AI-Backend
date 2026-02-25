from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from utilities import extract_text_from_pdf, analyze_contract
from schemas import ContractAnalysis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://legalpulse-ai.vercel.app", 'http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "Contract Review API running"}

@app.post("/analyze", response_model=ContractAnalysis)
async def analyze(file: UploadFile = File(None), text: str = Form(None)):

    if file:
        contract_text = await extract_text_from_pdf(file)
    else:
        contract_text = text

    result = await analyze_contract(contract_text)

    return result