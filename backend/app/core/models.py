from pydantic import BaseModel
from typing import List, Optional

class Issue(BaseModel):
    issue_type: str
    message: str
    line_number: Optional[int]

class CodeReviewRequest(BaseModel):
    code: str

class CodeReviewResponse(BaseModel):
    status: str
    issues: List[Issue]
    confidence_score: float
