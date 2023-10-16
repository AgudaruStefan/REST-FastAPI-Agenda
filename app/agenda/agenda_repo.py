import abc 

from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from .models import Agenda as AgendaModel
from .schema import AddContactSchema, UpdateContactSchema

class ContactNotFoundError(HTTPException):
    pass

class ABCAgendaRepo:
    @abc.abstractmethod
    def agenda_repo_add(self):
        pass

    @abc.abstractmethod
    def agenda_repo_get(self):
        pass

    @abc.abstractmethod
    def agenda_repo_delete(self):
        pass

    @abc.abstractmethod
    def agenda_repo_update(self):
        pass

class AgendaRepo(ABCAgendaRepo):
    def agenda_repo_add(self, add_schema: AddContactSchema, db: Session):
        adding_contact = AgendaModel(name=add_schema.name, phone=add_schema.phone, email=add_schema.email)
        db.add(adding_contact)
        db.commit()
        db.refresh(adding_contact)
        return adding_contact
    
    def agenda_repo_get(self, db: Session,  skip: int = 0, limit: int = 100):
            db_quary = db.query(AgendaModel).offset(skip).limit(limit).all()
            return db_quary if len(db_quary) > 0 else "No contact found!"
    
    def agenda_repo_delete(self, db: Session, id: int):
        deleted_contact = db.query(AgendaModel).filter_by(id = id)
        db_contact = deleted_contact.first()

        if not db_contact:
            raise ContactNotFoundError(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No contact with this id: {id} found!')
        deleted_contact.delete()
        db.commit()
        return f"Contact with id:{id} was deleted successfully!"

    def agenda_repo_update(self, update_schema: UpdateContactSchema, db: Session, id: int):
        contact_query = db.query(AgendaModel).filter(AgendaModel.id == id)
        db_contact = contact_query.first()
        if not db_contact:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No contact with this id: {id} found!')
        update_data = update_schema.model_dump(exclude_unset=True)
        contact_query.filter(AgendaModel.id == id).update(update_data,
                                                    synchronize_session=False)
        db.commit()
        db.refresh(db_contact)
        return {"status": "Contact was updated successfully!", "updated_contact": db_contact}
