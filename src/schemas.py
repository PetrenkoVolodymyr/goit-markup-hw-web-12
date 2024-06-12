from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, PastDate

class NoteBase(BaseModel):
    name: str = Field(max_length=50)
    familyname: str = Field(max_length=50)
    email: EmailStr
    phone: str = Field(min_length=10,max_length=10, default="0123456789")
    birthday: PastDate = None
    other: Optional[str] = None
    bd_soon: bool = False



class NoteModel(NoteBase):
    pass


class NoteResponse(NoteBase):
    id: int

    class Config:
        orm_mode = True