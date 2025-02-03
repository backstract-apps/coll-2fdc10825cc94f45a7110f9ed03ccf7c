from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password = Column(String, primary_key=False)

class Hackathons(Base):
    __tablename__ = 'hackathons'
    id = Column(Integer, primary_key=True)
    title = Column(String, primary_key=False)
    description = Column(String, primary_key=False)
    start_date = Column(Time, primary_key=False)
    end_date = Column(Time, primary_key=False)
    status = Column(String, primary_key=False)

class TeamMembers(Base):
    __tablename__ = 'team_members'
    id = Column(UUID, primary_key=True)
    team_id = Column(UUID, primary_key=True)
    user_id = Column(UUID, primary_key=True)

class Winners(Base):
    __tablename__ = 'winners'
    id = Column(UUID, primary_key=True)
    hackathon_id = Column(UUID, primary_key=False)
    team_id = Column(UUID, primary_key=False)

class Submissions(Base):
    __tablename__ = 'submissions'
    id = Column(UUID, primary_key=True)
    team_id = Column(UUID, primary_key=False)
    hackathon_id = Column(UUID, primary_key=False)
    project_title = Column(String, primary_key=False)
    project_link = Column(String, primary_key=False)

