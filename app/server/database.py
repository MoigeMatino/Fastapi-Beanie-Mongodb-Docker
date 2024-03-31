from beanie import init_beanie
import motor.motor_asyncio

from .models.product_review import ProductReview

async def init_db():
    client = client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://mongodb:27017/productreviews"
    )
    await init_beanie(database=client.db_name, document_models=[ProductReview])



