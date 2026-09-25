import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .inference import predict
from .species_info import SPECIES_DATA

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Fish Species Detection API", version="0.1-mock")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("Loading Fish Detection Model v0.1-mock... Model loaded successfully.")

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "model_version": "v0.1-mock",
        "supported_species_count": len(SPECIES_DATA)
    }

@app.get("/species")
async def get_all_species():
    return SPECIES_DATA

@app.post("/predict")
async def predict_endpoint(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    
    # Validate image extension
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp"}
    is_valid = any(file.filename.lower().endswith(ext) for ext in allowed_extensions)
    if not is_valid:
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Only JPG, PNG, and WEBP are supported."
        )
    
    try:
        contents = await file.read()
        result = await predict(contents)
        return result
    except Exception as e:
        logger.error(f"Inference error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during inference")
