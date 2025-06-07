from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def GET_root():
    return {"message": "HELLOOOOOO BUM"}

@app.get("/status")
async def GET_status():
    return {"message": "status update"}
