from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from .database import db
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from datetime import datetime

ORDER_STATUS = Enum("配送中", "検品中", name="status_enum")


class Member(db.Model):
    __tablename__ = "members"
    member_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    name_kana = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    registration_date = Column(Date, nullable=False)
    points = Column(Integer, default=0)
    qr_code = Column(String, nullable=True)

    reservations = relationship("Reservation", backref="member", lazy=True)
    borrow_histories = relationship("BorrowHistory", backref="member", lazy=True)
    orders = relationship("Order", backref="member", lazy=True)


class Order(db.Model):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)
    payment_method = Column(String, nullable=False)
    store_id = Column(Integer, ForeignKey("stores.store_id"), nullable=False)
    member_id = Column(Integer, ForeignKey("members.member_id"), nullable=False)

    details = relationship("OrderDetail", backref="order", lazy=True)


class OrderDetail(db.Model):
    __tablename__ = "order_details"
    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True)
    order_number = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    jan_code = Column(String, nullable=False)
    status = Column(ORDER_STATUS, nullable=False)


class Book(db.Model):
    __tablename__ = "books"
    jan_code = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    publication_date = Column(Date, nullable=False)
    pages = Column(Integer, nullable=False)
    size = Column(String, nullable=False)
    series = Column(String)
    retail_price = Column(Integer, nullable=False)


class CD(db.Model):
    __tablename__ = "cds"
    jan_code = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    label = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    retail_price = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)


class DVD(db.Model):
    __tablename__ = "dvds"
    jan_code = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    studio = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    runtime = Column(Integer, nullable=False)
    retail_price = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    rating = Column(String, nullable=False)


class Inventory(db.Model):
    __tablename__ = "inventories"
    store_id = Column(Integer, ForeignKey("stores.store_id"), primary_key=True)
    jan_code = Column(String, primary_key=True)
    quantity = Column(Integer, nullable=False)


class Store(db.Model):
    __tablename__ = "stores"
    store_id = Column(Integer, primary_key=True, autoincrement=True)
    store_name = Column(String, nullable=False)

    inventories = relationship("Inventory", backref="store", lazy=True)
    purchases = relationship("Purchase", backref="store", lazy=True)


class Purchase(db.Model):
    __tablename__ = "purchases"
    purchase_id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, ForeignKey("stores.store_id"), nullable=False)
    purchase_date = Column(Date, nullable=False)
    supplier = Column(String, nullable=False)
    total_amount = Column(Integer, nullable=False)

    details = relationship("PurchaseDetail", backref="purchase", lazy=True)


class PurchaseDetail(db.Model):
    __tablename__ = "purchase_details"
    purchase_id = Column(Integer, ForeignKey("purchases.purchase_id"), primary_key=True)
    purchase_number = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    jan_code = Column(String, nullable=False)
    status = Column(String, nullable=False)


class RentalItem(db.Model):
    __tablename__ = "rental_items"
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    jan_code = Column(String, ForeignKey("dvds.jan_code"), nullable=False)
    available = Column(Boolean, nullable=False)

    borrow_histories = relationship("BorrowHistory", backref="rental_item", lazy=True)


class Reservation(db.Model):
    __tablename__ = "reservations"
    reservation_id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column(Integer, ForeignKey("members.member_id"), nullable=False)
    store_id = Column(Integer, ForeignKey("stores.store_id"), nullable=False)
    reservation_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    pickup_deadline = Column(DateTime, nullable=False)

    details = relationship("ReservationDetail", backref="reservation", lazy=True)


class ReservationDetail(db.Model):
    __tablename__ = "reservation_details"
    reservation_id = Column(
        Integer, ForeignKey("reservations.reservation_id"), primary_key=True
    )
    reservation_number = Column(Integer, primary_key=True)
    jan_code = Column(String, ForeignKey("books.jan_code"), nullable=False)
    status = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)


class BorrowHistory(db.Model):
    __tablename__ = "borrow_histories"
    borrow_id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column(Integer, ForeignKey("members.member_id"), nullable=False)
    item_id = Column(Integer, ForeignKey("rental_items.item_id"), nullable=False)
    status = Column(Boolean, nullable=False)
    borrow_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
