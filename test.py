from sqlalchemy import create_engine, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Boolean, Column, ForeignKey, BigInteger, Integer, String, TIMESTAMP, Table, MetaData, update, text, UniqueConstraint
from dotenv import load_dotenv

# 開一個 .env file 去存取敏感資料
from os import getenv as env

# .env file 的內容示範
"""
HOST = host.docker.internal:5432
DATABASE = postgres
USER = postgres
PASSWORD = postgres
"""

# Load .env 的資料
load_dotenv()
db_user = env("USER")
db_password = env("PASSWORD")
db_hostname = env("HOST")
db_database_name = env("DATABASE")

# 連接資料庫URL (此為postgres的預設URL, 使用其他資料庫請更改URL)
engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_hostname}/{db_database_name}", future=True)

metadata = MetaData()
conn = engine.raw_connection()
cursor = conn.cursor()
print(engine)

# 建立 Database Table 示範
# Table名: users
# Column: Column名 (資料類型)
# Column: id (int)
# Column: username (str)
# Column: displayname (str)
# Column: email (str)
# Column: password (str)
# Column: role (str)
# Column: img (str)
users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String, unique=True), 
    Column("displayname", String), 
    Column("email", String), 
    Column("password", String),
)

forums = Table(
    "forums", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("writer", None, ForeignKey("users.id")),
    Column("title", String),
    Column("content", String),
    Column("create_time", TIMESTAMP, server_default=text("now()")),
)

replies = Table(
    "replies", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("writer", None, ForeignKey("users.id")),
    Column("content", String),
    Column("forum_id", None, ForeignKey("forums.id")),
    Column("create_time", TIMESTAMP, server_default=text("now()")),
)

likes = Table(
    "likes", metadata,
    Column("user_id", None, ForeignKey("users.id")),
    Column("forum_id", None, ForeignKey("forums.id")),
    Column("replies_id", None, ForeignKey("replies.id")),
    Column("like", Boolean),
    Column("create_time", TIMESTAMP, server_default=text("now()")),
    UniqueConstraint("user_id", "forum_id", "replies_id", name="likes_pk"),
)

# 如果SQL中 Database Table不存在則建立
metadata.create_all(engine)
#[17:47]
# 用SQL語法來新加資料示範
stmt = text(f"INSERT INTO likes VALUES({like_user_id}, {like_forum_id}, {like_reply_id}, NULL, {like})")
with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()