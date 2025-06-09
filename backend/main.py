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
        db.execute(text("SELECT 1"))
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@app.get("/wifi/nearby")
async def GET_wifi_nearby(lat: float, long: float, radius: int):
    return str(lat) + "," + str(long) + "," + str(radius)
