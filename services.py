"""
This module has the utilities functions for CRUD operations - for bookstore database
"""

from models import Base, Book
from sqlalchemy.orm import Session
from schemas import BookCreate


def create_book(db: Session, data: BookCreate):
    """
    This function creates an instance of Book in the db. 
    It uses the 'db' session and the BookCreate schema 
    to create the instance i.e a book entry into the db 
    
    model.dump() helps validate the data in the case that we do not get the data of type BookCreate
    
    :param db: DB Session object
    :param data: BookCreate class object
    """
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance


def get_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id==book_id).first()


def update_book(db: Session, book: BookCreate, book_id: int):
    book_queryset = db.query(Book).filter(Book.id==book_id).first()
    if book_queryset:
        for key, value in book.model_dump().items():
            setattr(book_queryset, key, value)
        db.commit()
        db.refresh(book_queryset)
    return book_queryset


def delete_book(db: Session, id: int):
    book_queryset = db.query(Book).filter(Book.id==id).first()
    if book_queryset:
        db.delete(book_queryset)
        db.commit()
    return book_queryset



