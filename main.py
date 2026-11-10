from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Library AI Recommendation Service", version="1.0")

# Σωστός ορισμός Pydantic Model
class BookRecommendation(BaseModel):
    id: str
    title: str
    reason: str

@app.get("/")
def home():
    return {"message": "Welcome to the Lending Library AI Microservice!"}

@app.get("/api/ai/recommendations/{username}", response_model=List[BookRecommendation])
def get_recommendations(username: str):
    if username.lower() == "admin":
        raise HTTPException(status_code=404, detail="User not found")
        
    mock_recommendations = [
        {"id": "1", "title": "Python for Data Science", "reason": "Based on your interest in programming"},
        {"id": "2", "title": "Machine Learning Yearning", "reason": "Popular among active library members"}
    ]
    
    return mock_recommendations