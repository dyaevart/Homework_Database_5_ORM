import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from global_vars import GlobalVars

class DatabaseMethods:

    def create_tables(self, engine):
        GlobalVars.Base.metadata.create_all(engine)

    def get_db_session(self, engine):
        return sessionmaker(bind=engine)()

    def close_session(self, session):
        session.close()

