from fastapi import APIRouter, HTTPException
from .core.models import CodeReviewRequest, CodeReviewResponse
from .analysis.extractor import analyze_code
from joblib import load
import os
from .core.config import settings
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

# Load ML model and vectorizer
# model = load(os.path.join(settings.MODEL_PATH, "code_review_model.joblib"))
# vectorizer = load(os.path.join(settings.MODEL_PATH, "code_vectorizer.joblib"))
try:
    model = load(os.path.join(settings.MODEL_PATH, "code_review_model.joblib"))
    vectorizer = load(os.path.join(settings.MODEL_PATH, "code_vectorizer.joblib"))
except:
    model = None
    vectorizer = None


# @router.post("/review/", response_model=CodeReviewResponse)
# async def review_code(request: CodeReviewRequest):
#     try:
#         # Perform rules-based analysis
#         issues = analyze_code(request.code)
        
#         # Prepare features for ML model
#         # features = vectorizer.transform([{"code": request.code, "issues": len(issues)}])
#         features = vectorizer.transform([{"code_length": len(request.code), "num_issues": len(issues)}])
#         confidence_score = float(model.predict_proba(features)[0][0])  # Probability of being clean
        
#         return CodeReviewResponse(
#             status="Success",
#             issues=issues,
#             confidence_score=confidence_score
#         )
#     except Exception as e:
#         logger.error(f"Error processing code review: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# In api.py, ensure clean endpoint definition
@router.post("/review", response_model=CodeReviewResponse)  # Remove trailing slash if needed
async def review_code(request: CodeReviewRequest):
    try:
        # Perform rules-based analysis
        issues = analyze_code(request.code)
        
        # Use ML model if available
        if model and vectorizer:
            features = vectorizer.transform([{"code_length": len(request.code), "num_issues": len(issues)}])
            confidence_score = float(model.predict_proba(features)[0][0])
        else:
            confidence_score = 0.5  # Default confidence when no model
        
        return CodeReviewResponse(
            status="Success",
            issues=issues,
            confidence_score=confidence_score
        )
    except Exception as e:
        logger.error(f"Error processing code review: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
