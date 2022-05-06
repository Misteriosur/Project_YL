import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Products(SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.telegram_id"))
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    photo = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tags = sqlalchemy.Column(sqlalchemy.JSON, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
