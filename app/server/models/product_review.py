from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from beanie import Document

class ProductReview(Document):
    product: str
    review: str
    rating: float
    date: datetime = datetime.now()

    class Settings:
        name = 'product_review'

    class Config:
        schema_extra = {
            "example": {
                "product": "Fastapi beanie mongo tutorial",
                "rating": 4.5,
                "review": "Awesome Tutorial!",
                "date": datetime.now()
            }
        }

class UpdateProductReview(BaseModel):
    product: Optional[str]
    review: Optional[str]
    rating: Optional[float]
    date: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "product": "Fastapi-Beanie-Mongo-Tutorial",
                "rating": 4.9,
                "review": "Amazing!",
                "date": datetime.now()
            }
        }
    

