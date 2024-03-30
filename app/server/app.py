from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["root"])
def read_root() -> dict:
    return {"mesage":"This is the root endpoint"}
