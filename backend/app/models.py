from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(String, nullable=False)

class Embedding(Base):
    __tablename__ = 'embeddings'
    id = Column(Integer, primary_key=True)
    vector = Column(LargeBinary, nullable=False)
    document_id = Column(Integer, ForeignKey('documents.id'))
    created_at = Column(String, nullable=False)
    document = relationship('Document', back_populates='embeddings')

Document.embeddings = relationship('Embedding', back_populates='document')
