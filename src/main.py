import json
from models.book import Book
from models.publisher import Publisher
from models.sale import Sale
from models.shop import Shop
from models.stock import Stock
from src.base import get_session
from src.base import clear_db


def import_test_data():
    session = get_session()

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
    session.close()


def get_data(a):
    session = get_session()
    q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Publisher).join(Book).join(
        Stock).join(Shop).join(Sale)
    if a.isdigit():
        x = q.filter(Publisher.id == a).all()
    else:
        x = q.filter(Publisher.name == a).all()

    for book_title, shop_name, sale_price, sale_date_sale in x:
        print(f"{book_title:<20}|{shop_name:<10}|{sale_price:<5}|{sale_date_sale}")
    session.close()


if __name__ == "__main__":
    import_test_data()
    get_data(a=input("Введите имя или ID: "))
    clear_db()
