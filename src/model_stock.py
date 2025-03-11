import sqlalchemy as sq
from global_vars import GlobalVars
from src.method_sale import Sale
from sqlalchemy.orm import relationship


class Stock(GlobalVars.Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer)

    sale = relationship(Sale, backref="sale")

