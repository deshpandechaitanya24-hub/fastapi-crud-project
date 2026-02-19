from db import Base
from sqlalchemy import Integer, String, Column


class Book(Base):
    # """
    # This class represents the Book table in the bookstore DB. In this class we declare the columns.
    # """
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)
