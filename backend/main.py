from fastapi import FastAPI, Response, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.database import get_new_session

app = FastAPI()

@app.get("/")
async def GET_root():
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/status")
async def GET_status(db: Session = Depends(get_new_session)):
    try:
        db.query(text("SELECT 1"))
        return "Database is connected"
    except Exception as e:
        return "ERROR: Database is not connected - " + str(e)

@app.get("/wifi/nearby")
async def GET_wifi_nearby(lat: float, long: float, radius: int):
    return str(lat) + "," + str(long) + "," + str(radius)
