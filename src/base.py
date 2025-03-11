from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from vars import Vars

Vars.initialize()
s = Vars.DB_TYPE + "://" + Vars.USER + ":" + Vars.PASS + "@" + Vars.HOST + ":" + Vars.PORT + "/" + Vars.DB_NAME
engine = create_engine(s)
Session = sessionmaker(bind=engine)

Base = declarative_base()


def get_session():
    Base.metadata.create_all(engine)
    return Session()

def clear_db():
    Base.metadata.drop_all(engine)

