from flask import Flask
from data import db_session
from data.users import User
from data.products import Products
from sqlalchemy import over, func
import numpy
import base64


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def new_line(name_of_base, **kwargs):
    db_session.global_init("db/blogs.db")
    if name_of_base == "users":
        line = User()
    elif name_of_base == "products":
        line = Products()
    for key, val in kwargs.items():
        setattr(line, key, val)
    db_sess = db_session.create_session()
    db_sess.add(line)
    db_sess.commit()
    db_sess.close()


def get_user_order(real_user_id):
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    a = 0
    list = []
    for product in db_sess.query(Products).filter((Products.user_id == real_user_id)):
        list.append(f"Заказ на продажу: {product.title}\n"
                    f"Описание: {product.about}\n"
                    f"Теги: {product.tags}\n"
                    f"Цена: {product.cost}]")
    return list

    db_sess.commit()
    db_sess.close()


def test_user_id(real_user_id):
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    a = 0
    list = []
    for user in db_sess.query(User).filter((User.telegram_id == real_user_id)):
        db_sess.close()
        return False
    db_sess.close()
    return True


def search_sell_orders(real_user_id, filter, my_tags):
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    a = 0
    list = []
    if filter == "мин_цена":
        for product in db_sess.query(Products).filter(Products.tags == my_tags).order_by(Products.cost.asc()):
            list.append(product)
    elif filter == "макс_цена":
        for product in db_sess.query(Products).filter(Products.tags == my_tags).order_by(Products.cost.desc()):
            list.append(product)
    db_sess.close()
    return list[0:30]
