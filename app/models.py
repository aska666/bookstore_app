from sqlalchemy import Enum
from .database import db

ORDER_STATUS = Enum("配送中", "検品中", name="status_enum")


class Member(db.Model):
    __tablename__ = "members"
    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    name_kana = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    registration_date = db.Column(db.Date, nullable=False)

    orders = db.relationship("Order", backref="member", lazy=True)


class Order(db.Model):
    __tablename__ = "orders"
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.Date, nullable=False)
    total_amount = db.Column(db.Integer, nullable=False)
    payment_method = db.Column(db.String, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.store_id"), nullable=False)
    member_id = db.Column(
        db.Integer, db.ForeignKey("members.member_id"), nullable=False
    )

    details = db.relationship("OrderDetail", backref="order", lazy=True)


class OrderDetail(db.Model):
    __tablename__ = "order_details"
    order_id = db.Column(db.String, db.ForeignKey("orders.order_id"), primary_key=True)
    order_number = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String, db.ForeignKey("books.isbn"), nullable=False)
    status = db.Column(ORDER_STATUS, nullable=False)


class Book(db.Model):
    __tablename__ = "books"
    isbn = db.Column(db.String, primary_key=True, unique=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String, nullable=False)
    series = db.Column(db.String)
    retail_price = db.Column(db.Integer, nullable=False)

    inventories = db.relationship("Inventory", backref="book", lazy=True)
    order_details = db.relationship("OrderDetail", backref="book", lazy=True)


class Inventory(db.Model):
    __tablename__ = "inventories"
    store_id = db.Column(db.Integer, db.ForeignKey("stores.store_id"), primary_key=True)
    isbn = db.Column(db.String, db.ForeignKey("books.isbn"), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)


class Store(db.Model):
    __tablename__ = "stores"
    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String, nullable=False)

    inventories = db.relationship("Inventory", backref="store", lazy=True)
    purchases = db.relationship("Purchase", backref="store", lazy=True)


class Purchase(db.Model):
    __tablename__ = "purchases"
    purchase_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.store_id"), nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    supplier = db.Column(db.String, nullable=False)
    total_amount = db.Column(db.Integer, nullable=False)

    details = db.relationship("PurchaseDetail", backref="purchase", lazy=True)


class PurchaseDetail(db.Model):
    __tablename__ = "purchase_details"
    purchase_id = db.Column(
        db.Integer, db.ForeignKey("purchases.purchase_id"), primary_key=True
    )
    purchase_number = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String, db.ForeignKey("books.isbn"), nullable=False)
    status = db.Column(db.String, nullable=False)
