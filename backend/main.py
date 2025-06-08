from fastapi import FastAPI, Response, status

app = FastAPI()

@app.get("/")
async def GET_root():
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/status")
async def GET_status():
    return {"body": "status update"}
