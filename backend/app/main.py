from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router
import logging
from .core.config import settings

app = FastAPI(title="AI Code Reviewer")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting AI Code Reviewer API")
    
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down AI Code Reviewer API")