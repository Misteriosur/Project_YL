import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    telegram_id = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    #email = sqlalchemy.Column(sqlalchemy.String,
    #                          index=True, unique=False, nullable=True)
    #hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    #created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
