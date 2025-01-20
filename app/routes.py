from flask import Blueprint, render_template, redirect, url_for, session, request
from .models import PurchaseDetail, Store, Book, Purchase, OrderDetail, Order
from .database import db
from sqlalchemy.orm import joinedload

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("login.html")


@main.route("/login", methods=["POST"])
def login():
    session["logged_in"] = True
    return redirect(url_for("main.home"))


@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/order-form")
def order_form():
    pass


@main.route("/order-progress", methods=["POST", "GET"])
def order_progress():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    query = (
        db.session.query(PurchaseDetail, Purchase, Store, Book)
        .select_from(PurchaseDetail)
        .join(Purchase, PurchaseDetail.purchase_id == Purchase.purchase_id)
        .join(Store, Purchase.store_id == Store.store_id)
        .join(Book, PurchaseDetail.isbn == Book.isbn)
        .order_by(PurchaseDetail.purchase_id, PurchaseDetail.purchase_number)
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    details = query.items

    return render_template(
        "order_progress.html",
        details=details,
        pagination=query,
        per_page=per_page,
    )


@main.route("/order-requests", methods=["POST", "GET"])
def order_requests():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    query = (
        db.session.query(Order, OrderDetail, Book, Store)
        .join(OrderDetail, Order.order_id == OrderDetail.order_id)
        .join(Book, OrderDetail.isbn == Book.isbn)
        .join(Store, Order.store_id == Store.store_id)
        .filter(OrderDetail.status == "検品中")
        .options(joinedload(OrderDetail.order))
        .order_by(OrderDetail.order_id, OrderDetail.order_number)
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    details = query.items

    return render_template(
        "order_requests.html",
        details=details,
        pagination=query,
        per_page=per_page,
    )
