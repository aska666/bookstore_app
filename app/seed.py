from .database import db

from app.models import (
    Member,
    Book,
    Order,
    OrderDetail,
    Store,
    Inventory,
    RentalItem,
    Reservation,
    ReservationDetail,
    CD,
    DVD,
    Purchase,
    PurchaseDetail,
)
from random import random
import random as rdm
from datetime import date, timedelta

JAN_CODE = []


def reset_database():
    db.drop_all()
    db.create_all()


def generate_unique_email(last_name: str):
    while True:
        email = f"{rdm.choice(last_name).lower()}{rdm.randint(1, 999)}@example.com"

        existing_member = Member.query.filter_by(email=email).first()
        if not existing_member:
            return email


def generate_unique_jan_code():
    while True:
        jan_code = f"45{rdm.randint(1000000000, 9999999999)}"

        if jan_code not in JAN_CODE:
            JAN_CODE.append(jan_code)
            return jan_code


def create_members():
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
        first_name = rdm.choice(first_names)
        last_name = rdm.choice(last_names)
        birth_year = rdm.randint(1970, 2000)
        birth_month = rdm.randint(1, 12)
        birth_day = rdm.randint(1, 28)

        member = Member(
            name=f"{last_name}{first_name}",
            name_kana=f"{last_name}{first_name}".upper(),
            date_of_birth=date(birth_year, birth_month, birth_day),
            phone_number=f"0{rdm.randint(90, 99)}{rdm.randint(1000, 9999)}{rdm.randint(1000, 9999)}",
            email=generate_unique_email(last_name),
            registration_date=date(2025, 1, 1) - timedelta(days=rdm.randint(0, 365)),
        )
        members.append(member)

    db.session.add_all(members)
    db.session.commit()
    return members


def create_stores():
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
    db.session.commit()
    return stores


def create_books():
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
        jan_code = generate_unique_jan_code()
        book = Book(
            jan_code=jan_code,
            title=f"{rdm.choice(titles)} Vol.{i + 1}",
            genre=rdm.choice(genres),
            publisher=rdm.choice(publishers),
            publication_date=date(2025, 1, 1) - timedelta(days=rdm.randint(0, 1825)),
            pages=rdm.randint(200, 800),
            size=rdm.choice(["A4", "A5", "B5"]),
            series=None,
            retail_price=rdm.randint(1000, 5000),
        )
        books.append(book)

    db.session.add_all(books)
    db.session.commit()
    return books


def create_cds():
    titles = [
        "80年代ベストヒット",
        "クラシック名曲集",
        "ジャズの名盤",
        "ポップヒット 2025",
        "レトロダンスパーティー",
        "ワークアウトミックス",
        "アコースティックチル",
        "交響曲第9番",
        "グレイテストヒッツ100",
        "リラックスピアノ",
        "エレクトロニックバイブス",
        "インディープレイリスト",
        "サマーサウンドトラック",
        "ギターの伝説",
        "ナイトタイムチルアウト",
        "ピアノコレクション",
        "ヒップホップアンセム",
        "ライブコンサートパフォーマンス",
        "グレイテストラブソング",
        "ダンスフロアアンセム",
    ]
    artists = [
        "サカナクション",
        "RADWIMPS",
        "宇多田ヒカル",
        "星野源",
        "桑田佳祐",
        "B'z",
        "Perfume",
        "Official髭男dism",
        "EXILE",
        "米津玄師",
        "King Gnu",
        "Aimer",
        "いきものがかり",
        "ONE OK ROCK",
        "L'Arc~en~Ciel",
        "X JAPAN",
        "V6",
        "欅坂46",
        "AKB48",
        "MAN WITH A MISSION",
    ]
    labels = [
        "Sony Music Japan",
        "Universal Music Japan",
        "Warner Music Japan",
        "Victor Entertainment",
        "Avex Group",
        "King Records",
        "Epic Records Japan",
        "J Storm",
        "Toy's Factory",
        "Capitol Music Japan",
        "EMI Records Japan",
        "Toshiba EMI",
        "Lantis",
        "Space Shower Music",
        "Being Inc.",
        "Teichiku Records",
        "Walt Disney Records Japan",
        "Columbia Music Entertainment",
        "Pony Canyon",
        "Rockin' On",
    ]
    cds = [
        CD(
            jan_code=generate_unique_jan_code(),
            title=rdm.choice(titles),
            artist=rdm.choice(artists),
            label=rdm.choice(labels),
            release_date=date.today()
            - timedelta(days=365 * 10)
            + timedelta(days=rdm.randint(0, (timedelta(days=365 * 10)).days)),
            retail_price=rdm.randint(1500, 5000),
            genre=rdm.choice(["Pop", "Rock", "Jazz", "Classical"]),
        )
        for i in range(50)
    ]
    db.session.add_all(cds)
    db.session.commit()
    return cds


def create_dvds():
    titles = [
        "ショーシャンクの空に",
        "ゴッドファーザー",
        "ダークナイト",
        "パルプ・フィクション",
        "フォレスト・ガンプ",
        "インセプション",
        "マトリックス",
        "ロード・オブ・ザ・リング　旅の仲間",
        "ファイト・クラブ",
        "帝国の逆襲",
        "荒野の七人",
        "羊たちの沈黙",
        "グラディエーター",
        "インターステラー",
        "プレステージ　精度",
        "ディパーテッド",
        "バック・トゥ・ザ・フューチャー",
        "ライオン・キング",
        "シンドラーのリスト",
        "ジュラシック・パーク",
    ]
    studios = [
        "ウォルト・ディズニー・スタジオ",
        "ワーナー・ブラザース",
        "ユニバーサル・ピクチャーズ",
        "20世紀フォックス",
        "ソニー・ピクチャーズ",
        "スタジオジブリ",
        "ピクサー・アニメーション・スタジオ",
        "ドリームワークス・アニメーション",
        "マーベル・スタジオ",
        "スタジオカラフル",
        "株式会社東映",
    ]
    dvds = [
        DVD(
            jan_code=generate_unique_jan_code(),
            title=rdm.choice(titles),
            studio=rdm.choice(studios),
            release_date=date.today()
            - timedelta(days=365 * 10)
            + timedelta(days=rdm.randint(0, (timedelta(days=365 * 10)).days)),
            runtime=rdm.randint(60, 180),
            retail_price=rdm.randint(2000, 6000),
            genre=rdm.choice(["Action", "Drama", "Comedy"]),
            rating=rdm.choice(["G", "PG", "R"]),
        )
        for i in range(50)
    ]
    db.session.add_all(dvds)
    db.session.commit()
    return dvds


def create_orders(stores, members):
    member = rdm.choice(members)
    orders = []
    for _ in range(50):
        if member:
            order = Order(
                order_date=date.today()
                - timedelta(days=365 * 10)
                + timedelta(days=rdm.randint(0, (timedelta(days=365 * 10)).days)),
                total_amount=rdm.randint(500, 10000),
                payment_method=rdm.choice(["Cash", "Credit Card", "Mobile Payment"]),
                store_id=rdm.choice(stores).store_id,
                member_id=member.member_id,
            )
            orders.append(order)
        else:
            print("Skipping order creation due to invalid member.")
    db.session.add_all(orders)
    db.session.commit()
    return orders


def create_order_details(orders, books, cds, dvds):
    order_details = []
    for order in orders:
        for order_number in range(rdm.randint(1, 5)):
            item = rdm.choice(books + cds + dvds)
            order_detail = OrderDetail(
                order_id=order.order_id,
                order_number=order_number,
                quantity=rdm.randint(1, 3),
                jan_code=item.jan_code,
                status=rdm.choice(["配送中", "検品中", "発送済み"]),
            )
            order_details.append(order_detail)
    db.session.add_all(order_details)
    db.session.commit()


def create_purchase(stores):
    suppliers = [
        "株式会社紀伊國屋書店",
        "株式会社山田書店",
        "株式会社日本書籍販売",
        "株式会社文藝春秋",
        "株式会社角川書店",
        "株式会社新潮社",
        "株式会社集英社",
        "株式会社講談社",
        "株式会社小学館",
        "株式会社リーダーズ・カフェ",
    ]
    purchases = []
    for _ in range(50):
        purchase = Purchase(
            store_id=rdm.choice(stores).store_id,
            purchase_date=date.today()
            - timedelta(days=365 * 10)
            + timedelta(days=rdm.randint(0, (timedelta(days=365 * 10)).days)),
            supplier=rdm.choice(suppliers),
            total_amount=rdm.randint(500, 10000),
        )
        purchases.append(purchase)
    db.session.add_all(purchases)
    db.session.commit()
    return purchases


def create_purchase_details(purchases, books, cds, dvds):
    purchase_details = []
    for purchase in purchases:
        for purchase_number in range(rdm.randint(1, 5)):
            item = rdm.choice(books + cds + dvds)
            purchase_detail = PurchaseDetail(
                purchase_id=purchase.purchase_id,
                purchase_number=purchase_number,
                quantity=rdm.randint(1, 3),
                jan_code=item.jan_code,
                status=rdm.choice(["配送中", "検品中", "発送済み"]),
            )
            purchase_details.append(purchase_detail)
    db.session.add_all(purchase_details)
    db.session.commit()


def create_inventories(stores, books, cds, dvds):
    all_products = books + cds + dvds
    existing_combinations = set()
    inventories = []

    while len(inventories) < 50:
        store = rdm.choice(stores)
        product = rdm.choice(all_products)

        if (store.store_id, product.jan_code) not in existing_combinations:
            inventory = Inventory(
                store_id=store.store_id,
                jan_code=product.jan_code,
                quantity=rdm.randint(0, 100),
            )
            inventories.append(inventory)
            existing_combinations.add((store.store_id, product.jan_code))

    db.session.add_all(inventories)
    db.session.commit()


def create_reservations(stores, members):
    reservations = [
        Reservation(
            member_id=rdm.choice(members).member_id,
            store_id=rdm.choice(stores).store_id,
            reservation_date=date.today()
            - timedelta(days=365 * 10)
            + timedelta(days=rdm.randint(0, (timedelta(days=365 * 10)).days)),
            pickup_deadline=lambda r_date: r_date + timedelta(days=rdm.randint(1, 20)),
        )
        for _ in range(50)
    ]

    for reservation in reservations:
        reservation.pickup_deadline = reservation.reservation_date + timedelta(
            days=rdm.randint(1, 20)
        )

    db.session.add_all(reservations)
    db.session.commit()
    return reservations


def create_reservation_details(reservations, books, cds, dvds):
    reservation_details = []
    for reservation in reservations:
        for reservation_number in range(rdm.randint(1, 5)):
            item = rdm.choice(books + cds + dvds)
            reservation_detail = ReservationDetail(
                reservation_id=reservation.reservation_id,
                reservation_number=reservation_number,
                jan_code=item.jan_code,
                status=rdm.choice(["Pending", "Completed", "Cancelled"]),
                quantity=rdm.randint(0, 100),
            )
            reservation_details.append(reservation_detail)
    db.session.add_all(reservation_details)
    db.session.commit()


def create_rental_items(dvds):
    rental_items = [
        RentalItem(
            jan_code=random.choice(dvds).jan_code,
            available=random.choice([True, False]),
        )
        for _ in range(50)
    ]
    db.session.add_all(rental_items)
    db.session.commit()
    return rental_items


def initialize_data():
    stores = create_stores()
    books = create_books()
    cds = create_cds()
    dvds = create_dvds()
    members = create_members()
    orders = create_orders(stores, members)
    purchase = create_purchase(stores)
    reservations = create_reservations(stores, members)

    create_purchase_details(purchase, books, cds, dvds)
    create_order_details(orders, books, cds, dvds)
    create_inventories(stores, books, cds, dvds)
    create_reservation_details(reservations, books, cds, dvds)
