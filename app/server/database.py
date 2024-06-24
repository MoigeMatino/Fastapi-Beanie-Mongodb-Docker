from beanie import init_beanie
import motor.motor_asyncio

from app.server.models.product_review import ProductReview

# TODO: create an entrypoint script for docker to initialize db setup
async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://{MONGO_ROOT_USER}:{MONGO_ROOT_PASSWORD}@mongodb:27017/productreviews"
    )
    await init_beanie(database=client.db_name, document_models=[ProductReview])



