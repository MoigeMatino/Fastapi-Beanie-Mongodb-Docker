from fastapi import FastAPI
from app.server.database import init_db
from app.server.routes.product_review import router as Router

app = FastAPI()
app.include_router(Router, tags=["Product Reviews"], prefix="/reviews")

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/", tags=["root"])
def read_root() -> dict:
    return {"mesage":"This is the root endpoint"}


