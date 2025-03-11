from models import *
import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models.book import Book
from models.publisher import Publisher
from models.sale import Sale
from models.shop import Shop
from models.stock import Stock
from src.base import session_factory


def create_publisher():
    session = session_factory()
    p = Publisher(name="Eksmoo")
    b = Book(title="Misery", publisher=p)
    session.add(p)
    session.add(b)
    session.commit()
    session.close()

def import_test_data():
    session = session_factory()

    with open('../fixtures/tests_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


if __name__ == "__main__":
    # create_publisher()
    import_test_data()