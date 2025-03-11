import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from global_vars import GlobalVars
from model_publisher import Publisher
from database_methods import DatabaseMethods


f = DatabaseMethods()
session = f.get_db_session(GlobalVars.engine)
f.create_tables(GlobalVars.engine)

p = Publisher(name="Eksmo")
print(p.id)

session.add(p)
print(p.id)


session.commit()
print(p.id)