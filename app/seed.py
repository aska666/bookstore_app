from .database import db
from datetime import date, timedelta
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
import random


def reset_database():
    db.drop_all()
    db.create_all()


def generate_unique_email(last_name: str):
    while True:
        # ランダムにemailを生成
        email = (
            f"{random.choice(last_name).lower()}{random.randint(1, 999)}@example.com"
        )

        existing_member = Member.query.filter_by(email=email).first()
        if not existing_member:
            return email


def create_sample_members():
    members = []
    first_names = [
        "太郎",
        "花子",
        "一郎",
        "美咲",
        "健一",
        "幸子",
        "翔太",
        "香織",
        "剛",
        "舞",
    ]
    last_names = [
        "山田",
        "佐藤",
        "鈴木",
        "田中",
        "高橋",
        "渡辺",
        "伊藤",
        "中村",
        "小林",
        "加藤",
    ]

    for i in range(50):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        birth_year = random.randint(1970, 2000)
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, 28)

        member = Member(
            name=f"{last_name}{first_name}",
            name_kana=f"{last_name}{first_name}".upper(),
            date_of_birth=date(birth_year, birth_month, birth_day),
            phone_number=f"0{random.randint(90, 99)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}",
            email=generate_unique_email(last_name),
            registration_date=date(2025, 1, 1) - timedelta(days=random.randint(0, 365)),
        )
        members.append(member)

    db.session.add_all(members)


def create_sample_books():
    books = []
    genres = [
        "プログラミング",
        "ビジネス",
        "文学",
        "科学",
        "歴史",
        "芸術",
        "自己啓発",
        "料理",
        "旅行",
        "教育",
    ]
    publishers = [
        "技術評論社",
        "翔泳社",
        "秀和システム",
        "オライリー・ジャパン",
        "日経BP",
    ]
    titles = [
        "Python実践入門",
        "データ分析の基礎",
        "機械学習入門",
        "Webアプリケーション開発",
        "経営戦略",
        "マーケティング入門",
        "プロジェクト管理",
        "チームビルディング",
        "日本の歴史",
        "世界の文学",
        "科学の謎",
        "現代アート入門",
        "成功への道",
        "おいしい料理の作り方",
        "世界遺産巡り",
        "効果的な学習法",
    ]

    for i in range(50):
        isbn = f"978-{random.randint(1000000000, 9999999999)}"
        book = Book(
            isbn=isbn,
            title=f"{random.choice(titles)} Vol.{i + 1}",
            genre=random.choice(genres),
            publisher=random.choice(publishers),
            publication_date=date(2025, 1, 1) - timedelta(days=random.randint(0, 1825)),
            pages=random.randint(200, 800),
            size=random.choice(["A4", "A5", "B5"]),
            series=None,
            retail_price=random.randint(1000, 5000),
        )
        books.append(book)

    db.session.add_all(books)


def create_sample_stores():
    stores = []
    store_names = [
        "オンラインショップ",
        "書店ABC",
        "ブックストアX",
        "本の森",
        "知識の泉",
        "未来書店",
        "駅前ブックス",
        "学園書店",
        "専門書店Y",
        "総合書店Z",
    ]

    for i in range(10):
        store = Store(store_id=i + 1, store_name=store_names[i])
        stores.append(store)

    db.session.add_all(stores)


def create_sample_orders():
    orders = []
    payment_methods = ["クレジットカード", "現金", "電子マネー", "代金引換"]

    for i in range(50):
        order = Order(
            order_date=date(2025, 1, 1) - timedelta(days=random.randint(0, 365)),
            total_amount=random.randint(1000, 50000),
            payment_method=random.choice(payment_methods),
            store_id=random.randint(1, 10),
            member_id=random.randint(1, 50),
        )
        orders.append(order)

    db.session.add_all(orders)


def create_sample_order_details():
    order_details = []
    statuses = ["検品中", "発送準備中", "発送済み", "配達完了"]

    for order_id in range(1, 51):
        num_items = random.randint(1, 3)
        for j in range(num_items):
            books = Book.query.all()
            order_detail = OrderDetail(
                order_id=order_id,
                order_number=j + 1,
                quantity=random.randint(1, 3),
                isbn=random.choice(books).isbn,
                status=random.choice(statuses),
            )
            order_details.append(order_detail)

    db.session.add_all(order_details)


def create_sample_purchases():
    purchases = []
    suppliers = ["Supplier A", "Supplier B", "Supplier C", "Supplier D", "Supplier E"]

    for i in range(50):
        purchase = Purchase(
            store_id=random.randint(1, 10),
            purchase_date=date(2025, 1, 1) - timedelta(days=random.randint(0, 365)),
            supplier=random.choice(suppliers),
            total_amount=random.randint(50000, 500000),
        )
        purchases.append(purchase)

    db.session.add_all(purchases)


def create_sample_purchase_details():
    purchase_details = []
    statuses = ["発注中", "配送中", "検品中", "完了"]

    for purchase_id in range(1, 51):
        num_items = random.randint(1, 5)
        for j in range(num_items):
            books = Book.query.all()
            purchase_detail = PurchaseDetail(
                purchase_id=purchase_id,
                purchase_number=j + 1,
                isbn=random.choice(books).isbn,
                quantity=random.randint(5, 50),
                status=random.choice(statuses),
            )
            purchase_details.append(purchase_detail)

    db.session.add_all(purchase_details)


def create_sample_inventories():
    inventories = []
    books = Book.query.all()
    stores = Store.query.all()

    for store in stores:
        for book in books:
            inventory = Inventory(
                store_id=store.store_id, isbn=book.isbn, quantity=random.randint(0, 100)
            )
            inventories.append(inventory)

    db.session.add_all(inventories)


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
