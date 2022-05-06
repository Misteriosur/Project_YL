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
    if name_of_base == "products":
        print(line.cost)
    #user.name = "Пользователь 1"
    #user.about = "биография пользователя 1"
    #user.email = "email@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(line)
    db_sess.commit()
    db_sess.close()
    #app.run(host="127.0.0.1", port="5000")


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
    for i in list:
        print(i)
    return list

    db_sess.commit()
    db_sess.close()

    #app.run(host="127.0.0.1", port="5000")


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

    #app.run(host="127.0.0.1", port="5000")


def search_sell_orders(real_user_id, filter, my_tags):
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    a = 0
    list = []
    list2 = ["tag1"]
    #query = db_sess.query(Products, over(func.row_number(), partition_by=numpy.count_nonzero(numpy.in1d(my_tags, Products.tags))))
    #.filter(numpy.count_nonzero(numpy.in1d(my_tags, Products.tags)) > 0)
    print("Начало запроса:")
    #q.sort(key=numpy.count_nonzero(numpy.in1d(my_tags, Products.tags)))
    print(my_tags)
    print(Products.tags)
    if filter == "мин_цена":
        for product in db_sess.query(Products).filter(Products.tags == my_tags).order_by(Products.cost.asc()):
            list.append(product)
        #print(product.title)
        #a = numpy.in1d(product.tags, my_tags)
        #print(numpy.count_nonzero(a))
    elif filter == "макс_цена":
        for product in db_sess.query(Products).filter(Products.tags == my_tags).order_by(Products.cost.desc()):
            list.append(product)
    print("Конец запроса:")
    return list[0:30]

    db_sess.commit()
    db_sess.close()

    #app.run(host="127.0.0.1", port="5000")
