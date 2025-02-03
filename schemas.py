from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: int
    name: str
    email: str
    password: str


class ReadUsers(BaseModel):
    id: int
    name: str
    email: str
    password: str
    class Config:
        from_attributes = True


class Hackathons(BaseModel):
    id: int
    title: str
    description: str
    start_date: datetime.time
    end_date: datetime.time
    status: str


class ReadHackathons(BaseModel):
    id: int
    title: str
    description: str
    start_date: datetime.time
    end_date: datetime.time
    status: str
    class Config:
        from_attributes = True


class TeamMembers(BaseModel):
    id: uuid.UUID
    team_id: uuid.UUID
    user_id: uuid.UUID


class ReadTeamMembers(BaseModel):
    id: uuid.UUID
    team_id: uuid.UUID
    user_id: uuid.UUID
    class Config:
        from_attributes = True


class Winners(BaseModel):
    id: uuid.UUID
    hackathon_id: uuid.UUID
    team_id: uuid.UUID


class ReadWinners(BaseModel):
    id: uuid.UUID
    hackathon_id: uuid.UUID
    team_id: uuid.UUID
    class Config:
        from_attributes = True


class Submissions(BaseModel):
    id: uuid.UUID
    team_id: uuid.UUID
    hackathon_id: uuid.UUID
    project_title: str
    project_link: str


class ReadSubmissions(BaseModel):
    id: uuid.UUID
    team_id: uuid.UUID
    hackathon_id: uuid.UUID
    project_title: str
    project_link: str
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: str
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PostHackathons(BaseModel):
    id: str
    title: str
    description: str
    start_date: str
    end_date: str
    status: str

    class Config:
        from_attributes = True



class PutHackathonsId(BaseModel):
    id: str
    title: str
    description: str
    start_date: str
    end_date: str
    status: str

    class Config:
        from_attributes = True



class PostTeamMembers(BaseModel):
    id: str
    team_id: str
    user_id: str

    class Config:
        from_attributes = True



class PutTeamMembersId(BaseModel):
    id: str
    team_id: str
    user_id: str

    class Config:
        from_attributes = True



class PostWinners(BaseModel):
    id: str
    hackathon_id: str
    team_id: str

    class Config:
        from_attributes = True



class PutWinnersId(BaseModel):
    id: str
    hackathon_id: str
    team_id: str

    class Config:
        from_attributes = True



class PostSubmissions(BaseModel):
    id: str
    team_id: str
    hackathon_id: str
    project_title: str
    project_link: str

    class Config:
        from_attributes = True



class PutSubmissionsId(BaseModel):
    id: str
    team_id: str
    hackathon_id: str
    project_title: str
    project_link: str

    class Config:
        from_attributes = True

