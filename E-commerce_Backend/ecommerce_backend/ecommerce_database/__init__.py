from beanie import init_beanie
import motor.motor_asyncio
from ecommerce_database.models import productReview
from config import settings
from pydantic import BaseModel


async def init_db():
    connection=settings.connection
    # MONGO_URI=settings.MONGO_URI
    client = motor.motor_asyncio.AsyncIOMotorClient(
        connection
        # MONGO_URI
    )
    await init_beanie(database=client.Sample, document_models=[productReview])
    
