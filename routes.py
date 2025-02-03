from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data, headers)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/hackathons/')
async def get_hackathons(db: Session = Depends(get_db)):
    try:
        return await service.get_hackathons(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/hackathons/id')
async def get_hackathons_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_hackathons_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/hackathons/')
async def post_hackathons(raw_data: schemas.PostHackathons, db: Session = Depends(get_db)):
    try:
        return await service.post_hackathons(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/hackathons/id/')
async def put_hackathons_id(raw_data: schemas.PutHackathonsId, db: Session = Depends(get_db)):
    try:
        return await service.put_hackathons_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/hackathons/id')
async def delete_hackathons_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_hackathons_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/team_members/')
async def get_team_members(db: Session = Depends(get_db)):
    try:
        return await service.get_team_members(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/team_members/id')
async def get_team_members_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_team_members_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/team_members/')
async def post_team_members(raw_data: schemas.PostTeamMembers, db: Session = Depends(get_db)):
    try:
        return await service.post_team_members(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/team_members/id/')
async def put_team_members_id(raw_data: schemas.PutTeamMembersId, db: Session = Depends(get_db)):
    try:
        return await service.put_team_members_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/team_members/id')
async def delete_team_members_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_team_members_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/winners/')
async def get_winners(db: Session = Depends(get_db)):
    try:
        return await service.get_winners(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/winners/id')
async def get_winners_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_winners_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/winners/')
async def post_winners(raw_data: schemas.PostWinners, db: Session = Depends(get_db)):
    try:
        return await service.post_winners(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/winners/id/')
async def put_winners_id(raw_data: schemas.PutWinnersId, db: Session = Depends(get_db)):
    try:
        return await service.put_winners_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/winners/id')
async def delete_winners_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_winners_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/submissions/')
async def get_submissions(db: Session = Depends(get_db)):
    try:
        return await service.get_submissions(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/submissions/id')
async def get_submissions_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_submissions_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/submissions/')
async def post_submissions(raw_data: schemas.PostSubmissions, db: Session = Depends(get_db)):
    try:
        return await service.post_submissions(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/submissions/id/')
async def put_submissions_id(raw_data: schemas.PutSubmissionsId, db: Session = Depends(get_db)):
    try:
        return await service.put_submissions_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/submissions/id')
async def delete_submissions_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_submissions_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

