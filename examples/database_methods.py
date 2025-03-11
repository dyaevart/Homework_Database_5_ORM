# import sqlalchemy
# import sqlalchemy as sq
# from sqlalchemy.orm import declarative_base, relationship, sessionmaker
# from global_vars import GlobalVars
#
#
# class DatabaseMethods:
#
#     def create_tables(self, engine):
#         GlobalVars.Base.metadata.create_all(engine)
#         # GlobalVars.Base.metadata.create_all(engine,tables=[Publisher.__table__, Book.__table__])
#         # book = relationship("Book", back_populates="publisher")
#         # publisher = relationship("Publisher", back_populates="book")
#         # GlobalVars.Base.metadata.drop_all(engine)
#         # Publisher.__table__.drop(engine)
#         # Book.__table__.drop(engine)
#         # Shop.__table__.drop(engine)
#         # Stock.__table__.drop(engine)
#         # Sale.__table__.drop(engine)
#         # Publisher.__table__.create(engine)
#         # Book.__table__.create(engine)
#         # Shop.__table__.create(engine)
#         # Stock.__table__.create(engine)
#         # Sale.__table__.create(engine)
#
#     def get_db_session(self, engine):
#         return sessionmaker(bind=engine)()
#
#     def close_session(self, session):
#         session.close()
#
