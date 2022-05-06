# Импортируем необходимые классы.
import logging
import datetime

import telegram
import asyncio

from bot_logic import *
from main_base import new_line, get_user_order, search_sell_orders

from my_telebot.auth import TOKEN

from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext import filters
from telegram.files import file
from product_test import product_test

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

MY_BOT = telegram.ext.ExtBot(TOKEN)
command_list = ["/start", "/help", "/address", "/phone", "/mail", "/work_time"]


def start(update, context):
    context.user_data["scene_num"] = "0"
    context.user_data["scene_2_test"] = 0
    update.message.reply_text("Добро пожаловать! Хотите ли вы, продолжить работу с ботом?", reply_markup=markup)
    update.message.reply_text(f"...", reply_markup=markup2)


def menu(update, context):
    name = "Ратмир"
    context.user_data["scene_num"] = "1"
    update.message.reply_text(f"Пользователь: {name}", reply_markup=markup1)
    #print(telegram.CallbackQuery, telegram.CallbackQuery.data)
    #print(markup2.inline_keyboard)


async def get_callback(callback, context):
    print(type(callback))
    print(callback.to_dict())
    print("main", context.user_data["scene_num"])
    last_message = callback.to_dict().get("callback_query").get("message").get("message_id")
    if context.user_data["scene_num"] == "0":
        if callback.to_dict().get("callback_query").get("data") == "btn00":
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn01":
            bot_logic(callback, context, last_message)

    elif context.user_data["scene_num"] == "1":
        if callback.to_dict().get("callback_query").get("data") == "btn1":
            # купить:
            context.user_data["scene_num"] = "4"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn2":
            # просмотр заказов:
            context.user_data["user_orders"] = get_user_order(context.user_data["user_id"])
            context.user_data["scene_num"] = "3"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn3":
            # продажа:
            context.user_data["scene_num"] = "02"
            bot_logic(callback, context, last_message)

    elif context.user_data["scene_num"] == "0000002":
        if callback.to_dict().get("callback_query").get("data") == "btn1":
            # название:
            context.user_data["scene_num"] = "-02"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn2":
            # описание:
            context.user_data["scene_num"] = "-002"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn3":
            # фото:
            context.user_data["scene_num"] = "-0002"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn4":
            # теги:
            context.user_data["scene_num"] = "-00002"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn5":
            # цена:
            context.user_data["scene_num"] = "-000002"
            bot_logic(callback, context, last_message)

        elif callback.to_dict().get("callback_query").get("data") == "btn6":
            with open("file.jpg", "wb") as my_file:
                if product_test(sell_tags=context.user_data["sell_tags"],
                                sell_cost=context.user_data["sell_cost"]):
                    # цена:
                    context.user_data["scene_num"] = "1"
                    context.user_data["scene_2_test"] = 0
                    new_line("products",
                             user_id=int(context.user_data["user_id"]),
                             title=context.user_data["sell_name"],
                             photo=context.user_data["sell_photo"],
                             tags=context.user_data["sell_tags"],
                             about=context.user_data["sell_about"],
                             cost=int(context.user_data["sell_cost"]))
                    bot_logic(callback, context, last_message)
                else:
                    callback.callback_query.edit_message_text(f"Название: {context.user_data['sell_name']} \n"
                                                              f"Описание: {context.user_data['sell_about']} \n"
                                                              f"Теги: {context.user_data['sell_tags']} \n"
                                                              f"Цена: {context.user_data['sell_cost']} \n"
                                                              f"Фото: фото \n"
                                                              f"ВЫ ВВЕЛИ НЕВЕРНУЮ ЦЕНУ, ВВЕДИТЕ ПРАВИЛЬНУЮ ЦЕНУ", reply_markup=markup3)
        else:
            bot_logic(callback, context, last_message)

    elif context.user_data["scene_num"] == "4":
        if callback.to_dict().get("callback_query").get("data") == "btn1":
            # редактирование тегов:
            context.user_data["scene_num"] = "04"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn2":
            # настройка фильтра:
            context.user_data["scene_num"] = "5"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn3":
            # поиск:
            context.user_data["search_list"] = search_sell_orders(context.user_data['user_name'],
                                                                  context.user_data['search_filtres'],
                                                                  context.user_data['search_tags'])
            context.user_data["search_list_index"] = 0
            context.user_data["scene_num"] = "6"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn4":
            # вернуться в меню:
            context.user_data["scene_num"] = "1"
            bot_logic(callback, context, last_message)

    elif context.user_data["scene_num"] == "5":
        if callback.to_dict().get("callback_query").get("data") == "btn1":
            # редактирование тегов:
            context.user_data["scene_num"] = "05"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn2":
            # настройка фильтра:
            context.user_data["scene_num"] = "005"
            bot_logic(callback, context, last_message)

    elif context.user_data["scene_num"] == "05":
        if callback.to_dict().get("callback_query").get("data") == "btn1":
            # мин цена:
            context.user_data["search_filtres"] = "мин_стоимость"
            context.user_data["scene_num"] = "4"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn2":
            # макс цена:
            context.user_data["search_filtres"] = "мин_стоимость"
            context.user_data["scene_num"] = "4"
            bot_logic(callback, context, last_message)

    elif context.user_data["scene_num"] == "005":
        if callback.to_dict().get("callback_query").get("data") == "btn1":
            # мин цена:
            context.user_data["search_filtres"] = "мин_популярность"
            context.user_data["scene_num"] = "4"
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn2":
            # макс цена:
            context.user_data["search_filtres"] = "макс_популярность"
            context.user_data["scene_num"] = "4"
            bot_logic(callback, context, last_message)

    elif context.user_data["scene_num"] == "6":
        if callback.to_dict().get("callback_query").get("data") == "btn1":
            # назад:
            if context.user_data["search_list_index"] != 0:
                context.user_data["search_list_index"] -= 1
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn2":
            # далее:
            if context.user_data["search_list_index"] != 30 and context.user_data["search_list_index"] != len(context.user_data["search_list"]) - 1:
                context.user_data["search_list_index"] += 1
            bot_logic(callback, context, last_message)
        elif callback.to_dict().get("callback_query").get("data") == "btn3":
            # в меню:
            context.user_data["scene_num"] = "4"
            bot_logic(callback, context, last_message)


def get_messages(callback, context):
    print(type(callback))
    print(callback.to_dict())
    print("message", context.user_data["scene_num"])
    if context.user_data["scene_num"] == "02":

        context.user_data["sell_name"] = callback.to_dict()["message"]["text"]
        context.user_data["scene_num"] = "002"
        if context.user_data["scene_2_test"] == 1:
            context.user_data["scene_num"] = "0000002"
            context.user_data["scene_2_test"] = 0
        bot_logic(callback, context)

    elif context.user_data["scene_num"] == "002":
        context.user_data["sell_about"] = callback.to_dict()["message"]["text"]
        context.user_data["scene_num"] = "0002"
        if context.user_data["scene_2_test"] == 1:
            context.user_data["scene_num"] = "0000002"
            context.user_data["scene_2_test"] = 0
        bot_logic(callback, context)
    elif context.user_data["scene_num"] == "0002":
        print(callback.to_dict()["message"]["photo"][0]["file_id"])
        print(callback.message.photo)
        print(callback)
        bot = telegram.ext.ExtBot(TOKEN)
        print(bot.get_file(file_id=callback.to_dict()["message"]["photo"][0]["file_id"]))
        with open(f"data/photo<users>/{callback.to_dict()['message']['photo'][0]['file_id']}.jpg", "wb") as my_file:
            file.File.download(bot.get_file(file_id=callback.to_dict()["message"]["photo"][-1]["file_id"]), out=my_file)
        context.user_data["sell_photo"] = f"data/photo<users>/{callback.to_dict()['message']['photo'][0]['file_id']}.jpg"
        context.user_data["scene_num"] = "00002"
        if context.user_data["scene_2_test"] == 1:
            context.user_data["scene_num"] = "0000002"
            context.user_data["scene_2_test"] = 0
        bot_logic(callback, context)

    elif context.user_data["scene_num"] == "00002":
        context.user_data["sell_tags"] = callback.to_dict()["message"]["text"].split("#")[1:]
        context.user_data["sell_tags"].append("")
        context.user_data["scene_num"] = "000002"
        if context.user_data["scene_2_test"] == 1:
            context.user_data["scene_num"] = "0000002"
            context.user_data["scene_2_test"] = 0
        bot_logic(callback, context)

    elif context.user_data["scene_num"] == "000002":
        context.user_data["sell_cost"] = callback.to_dict()["message"]["text"]
        context.user_data["scene_num"] = "0000002"
        if context.user_data["scene_2_test"] == 1:
            context.user_data["scene_num"] = "0000002"
            context.user_data["scene_2_test"] = 0
        bot_logic(callback, context)

    elif context.user_data["scene_num"] == "0000002":
        if callback.to_dict().get("message").get("data") == "btn1":
            # название:
            context.user_data["scene_num"] = "-02"
            bot_logic(callback, context)
        elif callback.to_dict().get("message").get("data") == "btn2":
            # описание:
            context.user_data["scene_num"] = "-002"
            bot_logic(callback, context)
        elif callback.to_dict().get("message").get("data") == "btn3":
            # фото:
            context.user_data["scene_num"] = "-0002"
            bot_logic(callback, context)
        elif callback.to_dict().get("message").get("data") == "btn4":
            # теги:
            context.user_data["scene_num"] = "-00002"
            bot_logic(callback, context)
        elif callback.to_dict().get("message").get("data") == "btn5":
            # цена:
            context.user_data["scene_num"] = "-000002"
            context.user_data["scene_2_test"] = 0
            bot_logic(callback, context)

        elif callback.to_dict().get("message").get("data") == "btn6":
            with open("file.jpg", "wb") as my_file:
                product_test(sell_nane=context.user_data["sell_name"],
                             sell_about=context.user_data["sell_about"],
                             sell_photo=my_file,
                             sell_tags=context.user_data["sell_tags"],
                             sell_cost=context.user_data["sell_cost"])
            # цена:
            context.user_data["scene_num"] = "1"
            context.user_data["scene_2_test"] = 0
            bot_logic(callback, context)
        else:
            bot_logic(callback, context)
    elif context.user_data["scene_num"] == "04":
        context.user_data["search_tags"] = callback.to_dict()["message"]["text"].split("#")[1:]
        context.user_data["sell_tags"].append("")
        context.user_data["scene_num"] = "004"
        bot_logic(callback, context)


# Напишем соответствующие функции.
def help(update, context):
    update.message.reply_text("\n".join(command_list))


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("get_menu", menu))
    dp.add_handler(CallbackQueryHandler(get_callback))
    dp.add_handler(MessageHandler(filters.Filters.all, get_messages))
    updater.start_polling()
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()