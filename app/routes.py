from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    request,
)
from .models import (
    PurchaseDetail,
    Store,
    Book,
    Purchase,
    OrderDetail,
    Order,
    ReservationDetail,
    Reservation,
    DVD,
)
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


@main.route("/logout", methods=["GET"])
def logout():
    session["logged_in"] = False
    return redirect(url_for("main.index"))


@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/order-form")
def order_form():
    return render_template("order_form.html")


@main.route("/order-progress", methods=["POST", "GET"])
def order_progress():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    query = (
        db.session.query(PurchaseDetail, Purchase, Store, Book)
        .select_from(PurchaseDetail)
        .join(Purchase, PurchaseDetail.purchase_id == Purchase.purchase_id)
        .join(Store, Purchase.store_id == Store.store_id)
        .join(Book, PurchaseDetail.jan_code == Book.jan_code)
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
        .join(Book, OrderDetail.jan_code == Book.jan_code)
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


@main.route("/rental", methods=["POST", "GET"])
def rental():
    return render_template("rental.html")


@main.route("/reservation-list", methods=["POST", "GET"])
def reservation_list():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    query = (
        db.session.query(ReservationDetail, Reservation, Store, DVD)
        .select_from(ReservationDetail)
        .join(
            Reservation, ReservationDetail.reservation_id == Reservation.reservation_id
        )
        .join(Store, Reservation.store_id == Store.store_id)
        .join(DVD, ReservationDetail.jan_code == DVD.jan_code)
        .order_by(ReservationDetail.reservation_id, Reservation.member_id)
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    details = query.items

    return render_template(
        "reservation_list.html",
        details=details,
        pagination=query,
        per_page=per_page,
    )
