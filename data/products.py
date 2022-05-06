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
    #created_date = sqlalchemy.Column(sqlalchemy.DateTime, defult=datetime.datetime.now)
    cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    views = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    #user = orm.relation('User')
    #news = orm.relation("News", back_populates='user')