from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).order_by(models.Users.id).all()
    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == id).first()
    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers , request: Request):
    id:str = raw_data.id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password

    auth:str = request.headers.get('auth')


    record_to_be_added = {'id': id, 'name': name, 'email': email, 'password': password}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users
    res = {
        'users_inserted_record': users_inserted_record,
        'header': auth,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:str = raw_data.id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'name': name, 'email': email, 'password': password}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete
    res = {
        'users_deleted': users_deleted,
    }
    return res

async def get_hackathons(db: Session):

    hackathons_all = db.query(models.Hackathons).order_by(models.Hackathons.id).all()
    res = {
        'hackathons_all': hackathons_all,
    }
    return res

async def get_hackathons_id(db: Session, id: int):

    hackathons_one = db.query(models.Hackathons).filter(models.Hackathons.id == id).first()
    res = {
        'hackathons_one': hackathons_one,
    }
    return res

async def post_hackathons(db: Session, raw_data: schemas.PostHackathons):
    id:str = raw_data.id
    title:str = raw_data.title
    description:str = raw_data.description
    start_date:str = raw_data.start_date
    end_date:str = raw_data.end_date
    status:str = raw_data.status


    record_to_be_added = {'id': id, 'title': title, 'description': description, 'start_date': start_date, 'end_date': end_date, 'status': status}
    new_hackathons = models.Hackathons(**record_to_be_added)
    db.add(new_hackathons)
    db.commit()
    db.refresh(new_hackathons)
    hackathons_inserted_record = new_hackathons
    res = {
        'hackathons_inserted_record': hackathons_inserted_record,
    }
    return res

async def put_hackathons_id(db: Session, raw_data: schemas.PutHackathonsId):
    id:str = raw_data.id
    title:str = raw_data.title
    description:str = raw_data.description
    start_date:str = raw_data.start_date
    end_date:str = raw_data.end_date
    status:str = raw_data.status


    hackathons_edited_record = db.query(models.Hackathons).filter(models.Hackathons.id == id).first()
    for key, value in {'id': id, 'title': title, 'description': description, 'start_date': start_date, 'end_date': end_date, 'status': status}.items():
          setattr(hackathons_edited_record, key, value)
    db.commit()
    db.refresh(hackathons_edited_record)
    hackathons_edited_record = hackathons_edited_record

    res = {
        'hackathons_edited_record': hackathons_edited_record,
    }
    return res

async def delete_hackathons_id(db: Session, id: int):

    hackathons_deleted = None
    record_to_delete = db.query(models.Hackathons).filter(models.Hackathons.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        hackathons_deleted = record_to_delete
    res = {
        'hackathons_deleted': hackathons_deleted,
    }
    return res

async def get_team_members(db: Session):

    team_members_all = db.query(models.TeamMembers).order_by(models.TeamMembers.id).all()
    res = {
        'team_members_all': team_members_all,
    }
    return res

async def get_team_members_id(db: Session, id: int):

    team_members_one = db.query(models.TeamMembers).filter(models.TeamMembers.id == id).first()
    res = {
        'team_members_one': team_members_one,
    }
    return res

async def post_team_members(db: Session, raw_data: schemas.PostTeamMembers):
    id:str = raw_data.id
    team_id:str = raw_data.team_id
    user_id:str = raw_data.user_id


    record_to_be_added = {'id': id, 'team_id': team_id, 'user_id': user_id}
    new_team_members = models.TeamMembers(**record_to_be_added)
    db.add(new_team_members)
    db.commit()
    db.refresh(new_team_members)
    team_members_inserted_record = new_team_members
    res = {
        'team_members_inserted_record': team_members_inserted_record,
    }
    return res

async def put_team_members_id(db: Session, raw_data: schemas.PutTeamMembersId):
    id:str = raw_data.id
    team_id:str = raw_data.team_id
    user_id:str = raw_data.user_id


    team_members_edited_record = db.query(models.TeamMembers).filter(models.TeamMembers.id == id).first()
    for key, value in {'id': id, 'team_id': team_id, 'user_id': user_id}.items():
          setattr(team_members_edited_record, key, value)
    db.commit()
    db.refresh(team_members_edited_record)
    team_members_edited_record = team_members_edited_record

    res = {
        'team_members_edited_record': team_members_edited_record,
    }
    return res

async def delete_team_members_id(db: Session, id: int):

    team_members_deleted = None
    record_to_delete = db.query(models.TeamMembers).filter(models.TeamMembers.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        team_members_deleted = record_to_delete
    res = {
        'team_members_deleted': team_members_deleted,
    }
    return res

async def get_winners(db: Session):

    winners_all = db.query(models.Winners).order_by(models.Winners.id).all()
    res = {
        'winners_all': winners_all,
    }
    return res

async def get_winners_id(db: Session, id: int):

    winners_one = db.query(models.Winners).filter(models.Winners.id == id).first()
    res = {
        'winners_one': winners_one,
    }
    return res

async def post_winners(db: Session, raw_data: schemas.PostWinners):
    id:str = raw_data.id
    hackathon_id:str = raw_data.hackathon_id
    team_id:str = raw_data.team_id


    record_to_be_added = {'id': id, 'hackathon_id': hackathon_id, 'team_id': team_id}
    new_winners = models.Winners(**record_to_be_added)
    db.add(new_winners)
    db.commit()
    db.refresh(new_winners)
    winners_inserted_record = new_winners
    res = {
        'winners_inserted_record': winners_inserted_record,
    }
    return res

async def put_winners_id(db: Session, raw_data: schemas.PutWinnersId):
    id:str = raw_data.id
    hackathon_id:str = raw_data.hackathon_id
    team_id:str = raw_data.team_id


    winners_edited_record = db.query(models.Winners).filter(models.Winners.id == id).first()
    for key, value in {'id': id, 'hackathon_id': hackathon_id, 'team_id': team_id}.items():
          setattr(winners_edited_record, key, value)
    db.commit()
    db.refresh(winners_edited_record)
    winners_edited_record = winners_edited_record

    res = {
        'winners_edited_record': winners_edited_record,
    }
    return res

async def delete_winners_id(db: Session, id: int):

    winners_deleted = None
    record_to_delete = db.query(models.Winners).filter(models.Winners.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        winners_deleted = record_to_delete
    res = {
        'winners_deleted': winners_deleted,
    }
    return res

async def get_submissions(db: Session):

    submissions_all = db.query(models.Submissions).order_by(models.Submissions.id).all()
    res = {
        'submissions_all': submissions_all,
    }
    return res

async def get_submissions_id(db: Session, id: int):

    submissions_one = db.query(models.Submissions).filter(models.Submissions.id == id).first()
    res = {
        'submissions_one': submissions_one,
    }
    return res

async def post_submissions(db: Session, raw_data: schemas.PostSubmissions):
    id:str = raw_data.id
    team_id:str = raw_data.team_id
    hackathon_id:str = raw_data.hackathon_id
    project_title:str = raw_data.project_title
    project_link:str = raw_data.project_link


    record_to_be_added = {'id': id, 'team_id': team_id, 'hackathon_id': hackathon_id, 'project_title': project_title, 'project_link': project_link}
    new_submissions = models.Submissions(**record_to_be_added)
    db.add(new_submissions)
    db.commit()
    db.refresh(new_submissions)
    submissions_inserted_record = new_submissions
    res = {
        'submissions_inserted_record': submissions_inserted_record,
    }
    return res

async def put_submissions_id(db: Session, raw_data: schemas.PutSubmissionsId):
    id:str = raw_data.id
    team_id:str = raw_data.team_id
    hackathon_id:str = raw_data.hackathon_id
    project_title:str = raw_data.project_title
    project_link:str = raw_data.project_link


    submissions_edited_record = db.query(models.Submissions).filter(models.Submissions.id == id).first()
    for key, value in {'id': id, 'team_id': team_id, 'hackathon_id': hackathon_id, 'project_title': project_title, 'project_link': project_link}.items():
          setattr(submissions_edited_record, key, value)
    db.commit()
    db.refresh(submissions_edited_record)
    submissions_edited_record = submissions_edited_record

    res = {
        'submissions_edited_record': submissions_edited_record,
    }
    return res

async def delete_submissions_id(db: Session, id: int):

    submissions_deleted = None
    record_to_delete = db.query(models.Submissions).filter(models.Submissions.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        submissions_deleted = record_to_delete
    res = {
        'submissions_deleted': submissions_deleted,
    }
    return res

