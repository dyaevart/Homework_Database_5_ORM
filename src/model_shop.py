import sqlalchemy as sq
from global_vars import GlobalVars
from src.model_stock import Stock
from sqlalchemy.orm import relationship


class Shop(GlobalVars.Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=False)

    stock = relationship(Stock, backref="shop_stock")
