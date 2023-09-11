from sqlalchemy.orm import Session

from src.db.models import Contact
from src.schemas import ContactModel



async def get_contacts(db: Session):
    contacts = db.query(Contact).all()
    return contacts

async def create_contact(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

async def get_contact_by_id(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.birthday = body.birthday
        contact.email = body.email
        contact.phone = body.phone
        contact.favorite = body.favorite
        db.commit()
    return contact


async def remove_contact(contact_id:int, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact
