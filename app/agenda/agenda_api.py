from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from .schema import AddContactSchema, UpdateContactSchema
from .agenda_repo import ABCAgendaRepo, AgendaRepo
from app.database import get_db

router = APIRouter()

@router.post(
    "/agenda", response_model=AddContactSchema, status_code=status.HTTP_201_CREATED
)
def add_agenda(agenda: AddContactSchema, repo_agenda: ABCAgendaRepo = Depends(AgendaRepo), db: Session = Depends(get_db)):
    adding_contact = repo_agenda.agenda_repo_add(agenda, db)
    return adding_contact


@router.get("/agenda")
def get_agenda(repo_agenda: ABCAgendaRepo = Depends(AgendaRepo), db: Session = Depends(get_db)):
    getting_agenda = repo_agenda.agenda_repo_get(db)
    return getting_agenda

@router.delete("/agenda/{id}")
def delete_agenda(id: int, repo_agenda: ABCAgendaRepo = Depends(AgendaRepo), db: Session = Depends(get_db)):
    deleting_agenda = repo_agenda.agenda_repo_delete(db, id)
    return deleting_agenda

@router.patch("/agenda/{id}", response_model=UpdateContactSchema, status_code=status.HTTP_200_OK)
def update_agenda(id: int, agenda:UpdateContactSchema, repo_agenda: ABCAgendaRepo = Depends(AgendaRepo), db: Session = Depends(get_db)):
    updateing_agenda = repo_agenda.agenda_repo_update(agenda, db, id)
    return updateing_agenda
