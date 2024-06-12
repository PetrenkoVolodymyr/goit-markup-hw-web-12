from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    familyname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(10), nullable=False)
    birthday = Column('created_at', DateTime, default=func.now())
    other = Column(String(150), nullable=True)
    bd_soon = Column(Boolean, default=False)

