from typing import Optional
from pydantic import BaseModel, Field

class ClientCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class Client(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True

class MatterCreate(BaseModel):
    client_id: int
    name: str
    description: Optional[str] = None

class MatterUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class Matter(BaseModel):
    id: int
    client_id: int
    name: str
    description: Optional[str] = None
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True

class DocumentCreate(BaseModel):
    matter_id: int
    name: str
    content: str

class DocumentUpdate(BaseModel):
    name: Optional[str] = None
    content: Optional[str] = None

class Document(BaseModel):
    id: int
    matter_id: int
    name: str
    content: str
    version: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
