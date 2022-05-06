from my_telebot.menu import *
from main_base import new_line, test_user_id
from main2 import MY_BOT


def bot_logic(update, context, last_message_id=0):
    if context.user_data["scene_num"] in ["-02", "-002", "-0002", "-00002", "-000002", "-0000002"]:
        context.user_data["scene_2_test"] = 1
    if context.user_data["scene_num"] == "0":
        if context.user_data.get("auth_user") == "0":
            print("НУ И ИДИ НАФИГ")
        else:
            # в дальнейшем обращаемся к данным пользователя:
            id = update.to_dict()['callback_query']['message']['chat']["id"]
            username = update.to_dict()['callback_query']['message']['chat']["first_name"]
            if not test_user_id(id):
                new_line("users", username=username, telegram_id=id)
            context.user_data["user_id"] = id
            context.user_data["user_name"] = username
            context.user_data["scene_num"] = "1"
            context.user_data["search_tags"] = ["tag1", ""]
            context.user_data["search_filtres"] = "мин_цена"
            MY_BOT.edit_message_text(message_id=last_message_id, chat_id=context.user_data["user_id"], text=f"Пользователь: {username}", reply_markup=markup1)
    elif context.user_data["scene_num"] == "1":
        MY_BOT.edit_message_text(message_id=last_message_id, chat_id=context.user_data["user_id"], text=f"Пользователь:", reply_markup=markup1)

    elif context.user_data["scene_num"] == "02":
        MY_BOT.send_message(context.user_data["user_id"], f"Введите название товара")
    elif context.user_data["scene_num"] == "002":
        MY_BOT.send_message(context.user_data["user_id"], f"Создайте описание")
        #update.message.reply_text(f"Название: {context.user_data['sell_name']}",  reply_markup=InlineKeyboardMarkup(sell_keyboard[0:1]))
        #update.callback_query.edit_message_text(f"Название: {context.user_data['sell_name']}",  reply_markup=InlineKeyboardMarkup(sell_keyboard[0:1]))
    elif context.user_data["scene_num"] == "0002":
        MY_BOT.send_message(context.user_data["user_id"], f"Загрузите фото (только одно)")
    elif context.user_data["scene_num"] == "00002":
        MY_BOT.send_message(context.user_data["user_id"], f"Введите теги, каждый тег отдельно одним словом без запятых,"
                                    f" пробелов или других разделителей, в начале каждого тега ставьте # (#товар#веселье#НеТупи)\n"
                                    f"чем больше тегов будет, которые описывают товар, тем проще его будет потом найти",)
    elif context.user_data["scene_num"] == "000002":
        MY_BOT.send_message(context.user_data["user_id"], "Установите цену")

    elif context.user_data["scene_num"] == "0000002":
         MY_BOT.send_message(context.user_data["user_id"], f"Название: {context.user_data['sell_name']} \n"
                                                           f"Описание: {context.user_data['sell_about']} \n"
                                                           f"Теги: {context.user_data['sell_tags']} \n"
                                                           f"Цена: {context.user_data['sell_cost']} \n"
                                                           f"Фото: фото \n", reply_markup=markup3)

    elif context.user_data["scene_num"] == "-02":
        MY_BOT.send_message(context.user_data["user_id"], "Введите название товара")
        context.user_data["scene_num"] = "02"
    elif context.user_data["scene_num"] == "-002":
        MY_BOT.send_message(context.user_data["user_id"], f"создайте описание")
        context.user_data["scene_num"] = "002"
    elif context.user_data["scene_num"] == "-0002":
        MY_BOT.send_message(context.user_data["user_id"], f"Загрузите фото (только одно)")
        context.user_data["scene_num"] = "0002"
    elif context.user_data["scene_num"] == "-00002":
        MY_BOT.send_message(context.user_data["user_id"],
                            f"Введите теги, каждый тег отдельно одним словом без запятых,"
                            f" пробелов или других разделителей, в начале каждого тега ставьте #")
        context.user_data["scene_num"] = "00002"

    elif context.user_data["scene_num"] == "-000002":
        MY_BOT.send_message(context.user_data["user_id"], f"Установите цену")
        context.user_data["scene_num"] = "000002"
    elif context.user_data["scene_num"] == "-0000002":
        MY_BOT.send_message(context.user_data["user_id"], f"Название: {context.user_data['sell_name']} \n"
                                                          f"Описание: {context.user_data['sell_about']} \n"
                                                          f"Теги: {context.user_data['sell_tags']} \n"
                                                          f"Цена: {context.user_data['sell_cost']} \n"
                                                          f"Фото: фото \n", reply_markup=markup3)
    elif context.user_data["scene_num"] == "3":
        orders = context.user_data["user_orders"]
        if orders:
            for i in orders:
                MY_BOT.send_message(context.user_data["user_id"], i)
        else:
            MY_BOT.send_message(context.user_data["user_id"], "К сожалению сейчас заказы отсутствуют\n")
        context.user_data["scene_num"] = "1"
        MY_BOT.send_message(chat_id=context.user_data["user_id"],
                            text=f"Пользователь:", reply_markup=markup1)

    elif context.user_data["scene_num"] == "4":
        MY_BOT.editMessageText(message_id=last_message_id, chat_id=context.user_data["user_id"],
                               text=f"Пользователь: {context.user_data['user_name']}\n"
                                    f"Теги: {context.user_data['search_tags']}\n"
                                    f"Фильтр поиска: {context.user_data['search_filtres']}",
                               reply_markup=markup4)

    elif context.user_data["scene_num"] == "004":
        context.user_data["scene_num"] = "4"
        MY_BOT.send_message(chat_id=context.user_data["user_id"],
                               text=f"Пользователь: {context.user_data['user_name']}\n"
                                    f"Теги: {context.user_data['search_tags']}\n"
                                    f"Фильтр поиска: {context.user_data['search_filtres']}",
                               reply_markup=markup4)

    elif context.user_data["scene_num"] == "04":
        MY_BOT.send_message(chat_id=context.user_data["user_id"],
                               text=f"Теги сейчас: {len(context.user_data['search_tags'])} - {', '.join(context.user_data['search_tags'])}\n\n"
                                    f"Введите теги, каждый тег отдельно одним словом без запятых,"
                                    f" пробелов или других разделителей, в начале каждого тега ставьте # (#товар#веселье#НеТупи)\n"
                                    f"чем больше будет тегов, которые описывают товар, тем проще его будет потом найти")

    elif context.user_data["scene_num"] == "5":
        MY_BOT.editMessageText(message_id=last_message_id, chat_id=context.user_data["user_id"],
                               text=f"Фильтр сейчас: {context.user_data['search_filtres']}", reply_markup=markup6)

    elif context.user_data["scene_num"] == "05":
        MY_BOT.editMessageText(message_id=last_message_id, chat_id=context.user_data["user_id"],
                               text=f"Фильтр сейчас: {context.user_data['search_filtres']}", reply_markup=markup7)

    elif context.user_data["scene_num"] == "005":
        MY_BOT.editMessageText(message_id=last_message_id, chat_id=context.user_data["user_id"],
                               text=f"Фильтр сейчас: {context.user_data['search_filtres']}", reply_markup=markup8)

    elif context.user_data["scene_num"] == "6":
        orders = context.user_data["search_list"]
        if orders:
            product = orders[context.user_data["search_list_index"]]
            with open(f"{product.photo}", "rb") as my_file:
                MY_BOT.send_photo(context.user_data["user_id"], my_file.read())
            MY_BOT.send_message(context.user_data["user_id"], f"Заказ на продажу: {product.title}\n"
                                                              f"Описание: {product.about}\n"
                                                              f"Теги: {product.tags}\n"
                                                              f"Цена: {product.cost}\n"
                                                              f"telegram_id Продавца: {product.user_id}", reply_markup=markup9)
        else:
            MY_BOT.send_message(context.user_data["user_id"], "К сожалению сейчас заказы отсутствуют\n")
            context.user_data["scene_num"] = "4"
            MY_BOT.send_message(chat_id=context.user_data["user_id"],
                                   text=f"Пользователь: {context.user_data['user_name']}\n"
                                        f"Теги: {context.user_data['search_tags']}\n"
                                        f"Фильтр поиска: {context.user_data['search_filtres']}",
                                   reply_markup=markup4)