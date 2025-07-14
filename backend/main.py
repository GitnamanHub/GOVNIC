from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = FastAPI(
    title="GovBizConnect API",
    description="AI-powered NIC code prediction and government scheme recommendations",
    version="1.0.0"
)

# Pydantic models for request/response
class BusinessDescription(BaseModel):
    description: str

class NICResponse(BaseModel):
    nic_code: str
    confidence: float

class SchemeResponse(BaseModel):
    name: str
    description: str
    similarity: float

class SchemesResponse(BaseModel):
    schemes: list[SchemeResponse]

# Global variables for loaded models
nic_classifier = None
scheme_embeddings = None
scheme_metadata = None
sentence_model = None

def load_models():
    """Load all trained models and data"""
    global nic_classifier, scheme_embeddings, scheme_metadata, sentence_model
    
    try:
        # Load NIC classifier
        with open("models/nic_classifier.pkl", "rb") as f:
            nic_classifier = pickle.load(f)
        
        # Load scheme embeddings and metadata
        with open("models/scheme_embeddings.pkl", "rb") as f:
            scheme_embeddings = pickle.load(f)
        
        with open("models/scheme_metadata.pkl", "rb") as f:
            scheme_metadata = pickle.load(f)
        
        # Load sentence transformer model
        sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        print("All models loaded successfully!")
        
    except Exception as e:
        print(f"Error loading models: {e}")
        raise

@app.on_event("startup")
async def startup_event():
    """Load models on startup"""
    load_models()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "GovBizConnect API",
        "version": "1.0.0",
        "endpoints": {
            "get_nic": "/get_nic",
            "get_schemes": "/get_schemes"
        }
    }

@app.post("/get_nic", response_model=NICResponse)
async def get_nic_code(request: BusinessDescription):
    """
    Predict NIC code for a business description
    """
    if nic_classifier is None:
        raise HTTPException(status_code=500, detail="NIC classifier not loaded")
    
    try:
        # Get prediction
        prediction = nic_classifier.predict([request.description])[0]
        
        # Get confidence score
        decision_scores = nic_classifier.decision_function([request.description])
        confidence = float(np.max(decision_scores))
        
        return NICResponse(
            nic_code=str(prediction),
            confidence=confidence
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.post("/get_schemes", response_model=SchemesResponse)
async def get_schemes(request: BusinessDescription):
    """
    Get top 5 government schemes for a business description
    """
    if (scheme_embeddings is None or scheme_metadata is None or 
        sentence_model is None):
        raise HTTPException(status_code=500, detail="Scheme models not loaded")
    
    try:
        # Generate embedding for the input description
        query_embedding = sentence_model.encode([request.description])
        
        # Calculate cosine similarities
        similarities = cosine_similarity(query_embedding, scheme_embeddings)[0]
        
        # Get top 5 similar schemes
        top_indices = np.argsort(similarities)[::-1][:5]
        
        schemes = []
        for idx in top_indices:
            schemes.append(SchemeResponse(
                name=scheme_metadata['scheme_names'][idx],
                description=scheme_metadata['descriptions'][idx],
                similarity=float(similarities[idx])
            ))
        
        return SchemesResponse(schemes=schemes)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scheme recommendation error: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    models_loaded = all([
        nic_classifier is not None,
        scheme_embeddings is not None,
        scheme_metadata is not None,
        sentence_model is not None
    ])
    
    return {
        "status": "healthy" if models_loaded else "unhealthy",
        "models_loaded": models_loaded
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 