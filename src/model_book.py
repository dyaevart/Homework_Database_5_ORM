import sqlalchemy as sq
from global_vars import GlobalVars
from src.model_stock import Stock
from sqlalchemy.orm import relationship


class Book(GlobalVars.Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    stock = relationship(Stock, backref="book_stock")
