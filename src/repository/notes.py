import datetime
from datetime import datetime as dt

from typing import List

from sqlalchemy.orm import Session

from src.database.models import Note
from src.schemas import NoteModel


async def create_note(body: NoteModel, db: Session) -> Note:
    note = Note(name=body.name, familyname=body.familyname, email=body.email, phone=body.phone, birthday=body.birthday, other = body.other, bd_soon = body.bd_soon)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

async def get_notes(skip: int, limit: int, db: Session) -> List[Note]:
    return db.query(Note).offset(skip).limit(limit).all()


async def get_note(note_id: int, db: Session) -> Note:
    return db.query(Note).filter(Note.id == note_id).first()


async def update_note(note_id: int, body: NoteModel, db: Session) -> Note | None:
    print('ss')
    note = db.query(Note).filter(Note.id == note_id).first()
    print('ss')
    if note:
        print('rr')
        note.name=body.name
        note.familyname=body.familyname
        note.email=body.email
        note.phone=body.phone
        note.birthday=body.birthday
        note.other = body.other
        note.bd_soon = body.bd_soon
        db.commit()
    return note


async def remove_note(note_id: int, db: Session) -> Note | None:
    note = (
        db.query(Note)
        .filter(Note.id == note_id)
        .first()
    )
    if note:
        db.delete(note)
        db.commit()
    return note

async def get_familyname(note_familyname: str, db: Session) -> Note:
    return db.query(Note).filter(Note.familyname == note_familyname).first()


async def get_email(note_email: str, db: Session) -> Note:
    return db.query(Note).filter(Note.email == note_email).first()


async def get_name(note_name: str, db: Session) -> Note:
    return db.query(Note).filter(Note.name == note_name).first()


async def get_birthday(db: Session) -> List[Note]:
    print('ggx')
    for note in db.query(Note).all():
        today = datetime.date.today()
        today = dt(today.year, today.month, today.day)
        birthday = note.birthday.strftime(f"{datetime.date.today().year}-"+"%m-%d %H:%M:%S")
        birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d %H:%M:%S")
        if birthday < today:
            birthday = note.birthday.strftime(f"{datetime.date.today().year+1}-"+"%m-%d %H:%M:%S")
            birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d %H:%M:%S")
        if (birthday - today).days <= 7:
            note.bd_soon = True
            db.commit()
        else:
            note.bd_soon = False
            db.commit()
    return db.query(Note).filter(Note.bd_soon == True).all()