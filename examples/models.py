# import sqlalchemy as sq
# from sqlalchemy.orm import declarative_base, relationship, sessionmaker
#
# Base = declarative_base()
#
# class Publisher(Base):
#     __tablename__ = "publisher"
#
#     id = sq.Column(sq.Integer, primary_key=True)
#     name = sq.Column(sq.String(length=40), unique=False)
#
# class Book(Base):
#     __tablename__ = "book"
#
#     id = sq.Column(sq.Integer, primary_key=True)
#     title = sq.Column(sq.String(length=40), unique=False)
#     id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
#
#     publisher = relationship(Publisher, backref="publisher")
#
# class Shop(Base):
#     __tablename__ = "shop"
#
#     id = sq.Column(sq.Integer, primary_key=True)
#     name = sq.Column(sq.String(length=40), unique=False)
#
# class Stock(Base):
#     __tablename__ = "stock"
#
#     id = sq.Column(sq.Integer, primary_key=True)
#     id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
#     id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
#     count = sq.Column(sq.Integer)
#
#     book = relationship(Book, backref="book")
#     shop = relationship(Shop, backref="shop")
#
#
# class Sale(Base):
#     __tablename__ = "sale"
#
#     id = sq.Column(sq.Integer, primary_key=True)
#     price = sq.Column(sq.Integer, nullable=False)
#     date_sale = sq.Column(sq.Date)
#     id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
#     count = sq.Column(sq.Integer)
#
#     stock = relationship(Stock, backref="stock")
#
#
# DSN = "postgresql://postgres:123gh45@localhost:5432/some_db"
# engine = sq.create_engine(DSN, echo=True)
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# p = Publisher(name="Eksmo")
# print(p.id)
#
# session.add(p)
# print(p.id)
#
# session.commit()
# print(p.id)
#
# session.close()
#
