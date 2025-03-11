import sqlalchemy
from sqlalchemy.orm import declarative_base
import psycopg2


class GlobalVars:

    Base = declarative_base()
    DSN = "postgresql://postgres:123gh45@localhost:5432/test_db"
    engine = sqlalchemy.create_engine(DSN)