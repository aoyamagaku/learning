from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

NOTES = {}
next_id = 1

class NoteCreate(BaseModel):
    title: str
    text: str

@app.get("/notes/{note_id}")
def read_note(note_id: int):
    if note_id not in NOTES:
        raise HTTPException(status_code=404, detail=f"Заметка {note_id} не найдена")
    return NOTES[note_id]

@app.post("/notes")
def create_note(operation: NoteCreate):
    global next_id
    note = {"id": next_id, "title": operation.title, "text": operation.text}
    NOTES[next_id] = note
    next_id +=1
    return note

@app.get("/notes")
def read_all_notes():
    return list(NOTES.values())

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in NOTES:
        raise HTTPException(
            status_code=404,
            detail=f"Заметка {note_id} не найдена"
        )
    deleted_note = NOTES.pop(note_id)
    return deleted_note
