from sqlalchemy.orm import Session
from models import Client
from schemas import ClientCreate, ClientUpdate

def create_client(db: Session, client: ClientCreate) -> Client:
    db_client = Client(name=client.name, email=client.email, phone=client.phone)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int) -> Client:
    return db.query(Client).filter(Client.id == client_id).first()

def update_client(db: Session, client_id: int, client: ClientUpdate) -> Client:
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        if client.name:
            db_client.name = client.name
        if client.email:
            db_client.email = client.email
        if client.phone:
            db_client.phone = client.phone
        db.commit()
        db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
