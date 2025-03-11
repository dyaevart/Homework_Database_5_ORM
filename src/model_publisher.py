import sqlalchemy as sq
from global_vars import GlobalVars
from sqlalchemy.orm import relationship
from src.model_book import Book


class Publisher(GlobalVars.Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=False)

    book = relationship(Book, backref="books")