# 書店管理システム

## 概要
本システムは書店チェーンの在庫管理、発注管理、および注文管理を行うためのWebアプリケーションです。店舗スタッフが使用することを想定し、書籍の発注から入荷までの一連の業務をサポートします。

## 主な機能
- 書籍発注管理
- 発注進捗の確認
- 在庫引当依頼の管理
- 店舗在庫の管理
- 会員情報の管理

## 技術スタック
- バックエンド: Python (Flask)
- データベース: SQLAlchemy (ORM)
- フロントエンド: HTML, TailwindCSS
- アイコン: Feather Icons

## 必要要件
- Python 3.7以上
- Flask
- Flask-SQLAlchemy
- その他requirements.txtに記載の依存パッケージ

## セットアップ手順

1. リポジトリのクローン
```bash
git clone https://github.com/yourusername/bookstore_app.git
cd bookstore_app
```

2. 仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Unix/macOS
venv\Scripts\activate     # Windows
```

3. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

4. データベースの初期化
```bash
flask db upgrade
```

5. アプリケーションの起動
```bash
python run.py
```

## データベース構造
```mermaid
erDiagram
    MEMBER {
        INTEGER member_id PK "会員ID"
        STRING name "名前"
        STRING name_kana "ふりがな"
        DATE date_of_birth "生年月日"
        STRING phone_number "電話番号"
        STRING email "メールアドレス"
        DATE registration_date "登録日"
        INTEGER points "ポイント"
        STRING qr_code "QRコード"
    }

    ORDER {
        INTEGER order_id PK "注文ID"
        DATE order_date "注文日"
        INTEGER total_amount "合計金額"
        STRING payment_method "支払い方法"
        INTEGER store_id FK "店舗ID"
        INTEGER member_id FK "会員ID"
    }

    ORDER_DETAIL {
        STRING order_id FK "注文ID"
        INTEGER order_number PK "注文番号"
        INTEGER quantity "数量"
        STRING isbn FK "ISBN"
        ENUM status "ステータス"
    }

    BOOK {
        STRING isbn PK "ISBN"
        STRING title "タイトル"
        STRING genre "ジャンル"
        STRING publisher "出版社"
        DATE publication_date "出版日"
        INTEGER pages "ページ数"
        STRING size "サイズ"
        STRING series "シリーズ"
        INTEGER retail_price "小売価格"
    }

    INVENTORY {
        INTEGER store_id FK "店舗ID"
        STRING isbn FK "ISBN"
        INTEGER quantity "在庫数"
    }

    STORE {
        INTEGER store_id PK "店舗ID"
        STRING store_name "店舗名"
    }

    PURCHASE {
        INTEGER purchase_id PK "仕入ID"
        INTEGER store_id FK "店舗ID"
        DATE purchase_date "仕入日"
        STRING supplier "仕入先"
        INTEGER total_amount "合計金額"
    }

    PURCHASE_DETAIL {
        INTEGER purchase_id FK "仕入ID"
        INTEGER purchase_number PK "仕入番号"
        INTEGER quantity "数量"
        STRING isbn FK "ISBN"
        STRING status "ステータス"
    }

    RENTAL_ITEM {
        INTEGER item_id PK "識別子"
        STRING product_id "商品識別子"
        BOOLEAN available "利用可能フラグ"
    }

    RESERVATION {
        INTEGER reservation_id PK "予約ID"
        INTEGER member_id FK "会員ID"
        INTEGER item_id FK "品目識別子"
        BOOLEAN status "ステータス"
        DATETIME reservation_date "予約日時"
    }

    BORROW_HISTORY {
        INTEGER borrow_id PK "貸出ID"
        INTEGER member_id FK "会員ID"
        INTEGER item_id FK "品目識別子"
        BOOLEAN status "ステータス"
        DATETIME borrow_date "貸出日時"
        DATETIME return_date "返却日時"
    }

    MEMBER ||--o{ ORDER : "注文する"
    MEMBER ||--o{ RESERVATION : "予約する"
    MEMBER ||--o{ BORROW_HISTORY : "貸出履歴を持つ"
    ORDER ||--o{ ORDER_DETAIL : "注文の詳細"
    BOOK ||--o{ ORDER_DETAIL : "注文品"
    BOOK ||--o{ INVENTORY : "在庫品"
    BOOK ||--o{ PURCHASE_DETAIL : "仕入品"
    STORE ||--o{ INVENTORY : "在庫を管理"
    STORE ||--o{ PURCHASE : "仕入を行う"
    PURCHASE ||--o{ PURCHASE_DETAIL : "仕入の詳細"
    RENTAL_ITEM ||--o{ RESERVATION : "予約対象"
    RENTAL_ITEM ||--o{ BORROW_HISTORY : "貸出対象"
```

### 主要テーブル
- members: 会員情報
- books: 書籍マスタ
- orders: 注文情報
- order_details: 注文明細
- stores: 店舗情報
- inventories: 在庫情報
- purchases: 仕入れ情報
- purchase_details: 仕入れ明細

## 機能詳細

### 発注管理
- 書籍検索と発注数量の指定
- 倉庫/店舗ごとの配送日数確認
- 発注進捗のステータス管理（配送中/検品中）

### 在庫引当
- 注文に対する在庫引当処理
- 在庫不足時の発注連携
- 引当状況の一覧表示

### 画面説明
- `/`: ログイン画面
- `/home`: ホーム画面
- `/order-form`: 発注入力画面
- `/order-progress`: 発注進捗確認画面
- `/order-requests`: 引当依頼一覧画面

## 開発ガイドライン

### コーディング規約
- PEP 8に準拠したPythonコード
- アプリケーションの構造はBlueprintパターンを使用
- データベース操作はSQLAlchemyのORMを使用

### テストについて
- ユニットテストはPytestを使用
- テストカバレッジの維持

## ライセンス
MIT License

## 注意事項
- 本システムは開発中のため、機能は随時更新される可能性があります
- 本番環境での使用前に、セキュリティ設定の確認を推奨します
