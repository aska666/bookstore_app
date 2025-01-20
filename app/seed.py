from .database import db
from datetime import date
from app.models import (
    Member,
    Book,
    Order,
    OrderDetail,
    Store,
    Inventory,
    Purchase,
    PurchaseDetail,
)


def reset_database():
    db.drop_all()
    db.create_all()


def create_sample_members():
    member1 = Member(
        name="山田太郎",
        name_kana="ヤマダタロウ",
        date_of_birth=date(1990, 5, 1),
        phone_number="09012345678",
        email="yamada@example.com",
        registration_date=date(2025, 1, 1),
    )
    member2 = Member(
        name="佐藤花子",
        name_kana="サトウハナコ",
        date_of_birth=date(1985, 6, 15),
        phone_number="09023456789",
        email="sato@example.com",
        registration_date=date(2025, 1, 1),
    )
    db.session.add_all([member1, member2])


def create_sample_books():
    book1 = Book(
        isbn="978-1234567890",
        title="Python入門",
        genre="プログラミング",
        publisher="技術評論社",
        publication_date=date(2025, 1, 1),
        pages=300,
        size="A5",
        series=None,
        retail_price=3000,
    )
    book2 = Book(
        isbn="978-0987654321",
        title="Flaskの使い方",
        genre="プログラミング",
        publisher="技術評論社",
        publication_date=date(2025, 1, 1),
        pages=250,
        size="A5",
        series=None,
        retail_price=2500,
    )
    db.session.add_all([book1, book2])


def create_sample_stores():
    store1 = Store(store_id=1, store_name="オンラインショップ")
    store2 = Store(store_id=2, store_name="書店ABC")
    db.session.add_all([store1, store2])


def create_sample_orders():
    order1 = Order(
        order_date=date(2025, 1, 1),
        total_amount=5500,
        payment_method="クレジットカード",
        store_id=1,
        member_id=1,
    )
    db.session.add(order1)


def create_sample_order_details():
    order_detail1 = OrderDetail(
        order_id=1, order_number=1, quantity=1, isbn="978-1234567890", status="検品中"
    )
    order_detail2 = OrderDetail(
        order_id=1, order_number=2, quantity=1, isbn="978-0987654321", status="検品中"
    )
    db.session.add_all([order_detail1, order_detail2])


def create_sample_purchases():
    purchase1 = Purchase(
        store_id=1,
        purchase_date=date(2025, 1, 1),
        supplier="Supplier A",
        total_amount=10000,
    )
    purchase2 = Purchase(
        store_id=2,
        purchase_date=date(2025, 1, 2),
        supplier="Supplier B",
        total_amount=8000,
    )
    db.session.add_all([purchase1, purchase2])


def create_sample_purchase_details():
    purchase_detail1 = PurchaseDetail(
        purchase_id=1,
        purchase_number=1,
        isbn="978-1234567890",
        quantity=5,
        status="配送中",
    )
    purchase_detail2 = PurchaseDetail(
        purchase_id=1,
        purchase_number=2,
        isbn="978-0987654321",
        quantity=3,
        status="検品中",
    )
    purchase_detail3 = PurchaseDetail(
        purchase_id=2,
        purchase_number=1,
        isbn="978-1234567890",
        quantity=10,
        status="配送中",
    )
    db.session.add_all([purchase_detail1, purchase_detail2, purchase_detail3])


def create_sample_inventories():
    inventory1 = Inventory(store_id=1, isbn="978-1234567890", quantity=50)
    inventory2 = Inventory(store_id=1, isbn="978-0987654321", quantity=30)
    inventory3 = Inventory(store_id=2, isbn="978-1234567890", quantity=20)
    inventory4 = Inventory(store_id=2, isbn="978-0987654321", quantity=10)
    db.session.add_all([inventory1, inventory2, inventory3, inventory4])


def initialize_data():
    create_sample_members()
    create_sample_books()
    create_sample_stores()
    create_sample_orders()
    create_sample_order_details()
    create_sample_purchases()
    create_sample_purchase_details()
    create_sample_inventories()
    db.session.commit()
