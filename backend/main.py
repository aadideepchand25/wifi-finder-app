from fastapi import FastAPI, Response, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.database import get_new_session
import database.services.query as dq
import backend.schemas as s

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
    
@app.get("/wifi/nearby", response_model=list[s.read.wifi_id_read])
async def GET_wifi_nearby(location: s.create.wifi_location, radius: int, db: Session = Depends(get_new_session)):
    return    

@app.get("/wifi/info", response_model=s.read.wifi)
async def GET_wifi_info(id: int, db: Session = Depends(get_new_session)):
    return dq.query_wifi_info_by_id(db, id)