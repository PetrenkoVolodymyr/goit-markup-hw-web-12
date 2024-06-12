from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import NoteModel, NoteResponse
from src.repository import notes as repository_notes


router = APIRouter(prefix="/notes")


@router.post("/", response_model=NoteResponse)
async def create_note(body: NoteModel, db: Session = Depends(get_db)):
    return await repository_notes.create_note(body, db)


@router.get("/", response_model=List[NoteResponse])
async def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notes = await repository_notes.get_notes(skip, limit, db)
    return notes


@router.get("/{note_id}", response_model=NoteResponse)
async def read_note_id(note_id: int, db: Session = Depends(get_db)):
    print('1')
    note = await repository_notes.get_note(note_id, db)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found3"
        )
    return note


@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(body: NoteModel, note_id: int, db: Session = Depends(get_db)):
    print('q')
    note = await repository_notes.update_note(note_id, body, db)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note


@router.delete("/{note_id}", response_model=NoteResponse)
async def remove_note(note_id: int, db: Session = Depends(get_db)):
    note = await repository_notes.remove_note(note_id, db)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note

#
@router.get("/name/{note_name}", response_model=NoteResponse)
async def find_note_by_name(note_name: str, db: Session = Depends(get_db)):
    print('2')
    note = await repository_notes.get_name(note_name, db)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note


@router.get("/familyname/{note_familyname}", response_model=NoteResponse)
async def find_note_by_familyname(note_familyname: str, db: Session = Depends(get_db)):
    print('3')
    note = await repository_notes.get_familyname(note_familyname, db)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note


@router.get("/email/{note_email}", response_model=NoteResponse)
async def find_note_by_email(note_email: str, db: Session = Depends(get_db)):
    print('4')
    note = await repository_notes.get_email(note_email, db)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note


@router.get("/birthdays", response_model=List[NoteResponse])
async def show_time(db: Session = Depends(get_db)):
    print('ww')
    notes = await repository_notes.get_birthday(db)
    return notes
