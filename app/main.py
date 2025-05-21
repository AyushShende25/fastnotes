from fastapi import FastAPI
from app.notes.schemas import NoteOut, NoteCreate, NoteUpdate
from app.notes import services as notes_services
from typing import List
from app.core.database import SessionDep

app = FastAPI()


@app.post("/notes", response_model=NoteOut)
async def create_note(session: SessionDep, new_note: NoteCreate):
    note = await notes_services.create_note(session, new_note)
    return note


@app.get("/notes/{note_id}", response_model=NoteOut)
async def get_note(session: SessionDep, note_id: int):
    note = await notes_services.get_note(session, note_id)
    return note


@app.get("/notes", response_model=List[NoteOut])
async def get_notes(session: SessionDep):
    notes = await notes_services.get_all_notes(session)
    return notes


@app.patch("/notes/{note_id}", response_model=NoteOut)
async def update_note(session: SessionDep, note_id: int, new_note: NoteUpdate):
    note = await notes_services.update_note(session, note_id, new_note)
    return note


@app.delete("/notes/{note_id}")
async def delete_note(session: SessionDep, note_id: int):
    response = await notes_services.delete_note(session, note_id)
    return response
