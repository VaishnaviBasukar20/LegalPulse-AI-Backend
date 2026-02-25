from pydantic import BaseModel, Field
from typing import List, Optional, Literal


# ---------------------------
# Risk Detail Schema
# ---------------------------

class RiskDetail(BaseModel):
    level: Literal["Low", "Medium", "High"] = Field(
        description="Severity level of the identified risk."
    )
    description: str = Field(
        description="Clear explanation of the risk and why it matters."
    )


# ---------------------------
# Risk Flags Container
# ---------------------------

class RiskFlags(BaseModel):
    auto_renewal_risk: Optional[RiskDetail] = None
    liability_risk: Optional[RiskDetail] = None
    missing_exit_clause: Optional[RiskDetail] = None
    indemnity_risk: Optional[RiskDetail] = None
    ip_ownership_risk: Optional[RiskDetail] = None
    other_risks: List[RiskDetail] = Field(default_factory=list)


# ---------------------------
# Main Contract Analysis Schema
# ---------------------------

class ContractAnalysis(BaseModel):
    parties: List[str] = Field(
        default_factory=list,
        description="Names of the parties involved in the agreement."
    )

    contract_duration: Optional[str] = Field(
        default=None,
        description="Effective date and duration of the contract."
    )

    renewal_terms: Optional[str] = Field(
        default=None,
        description="Details of renewal clauses, including auto-renewal."
    )

    payment_terms: Optional[str] = Field(
        default=None,
        description="Payment amounts, schedule, penalties, and late fees."
    )

    termination_clauses: Optional[str] = Field(
        default=None,
        description="Conditions and process for terminating the agreement."
    )

    confidentiality_terms: Optional[str] = Field(
        default=None,
        description="Obligations regarding confidential information."
    )

    liability_clauses: Optional[str] = Field(
        default=None,
        description="Liability limitations, caps, and indemnification."
    )

    ip_ownership: Optional[str] = Field(
        default=None,
        description="Ownership of intellectual property."
    )

    plain_english_summary: str = Field(
        description="A short, simple explanation understandable by a non-lawyer."
    )

    risk_flags: RiskFlags