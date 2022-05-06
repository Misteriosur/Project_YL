from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton

# кнопочки вспомогашки:
reply_keyboard = [["/start"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)

# стандартное меню в свернутом виде:
menu_keyboard = [[InlineKeyboardButton("Купить", callback_data='btn1'), InlineKeyboardButton("Мои заказы", callback_data='btn2'), InlineKeyboardButton("Продать", callback_data='btn3')]]
markup1 = InlineKeyboardMarkup(menu_keyboard)

# данетка:
yes_no_key = [[InlineKeyboardButton("Да", callback_data='btn01'), InlineKeyboardButton("Нет", callback_data='btn00')]]
markup2 = InlineKeyboardMarkup(yes_no_key)

# меню продажника:
sell_keyboard = [[InlineKeyboardButton("Редактировать название", callback_data='btn1')],
                 [InlineKeyboardButton("Редактировать описание", callback_data='btn2')],
                 [InlineKeyboardButton("Редактировать фото", callback_data='btn3')],
                 [InlineKeyboardButton("Редактировать теги", callback_data='btn4')],
                 [InlineKeyboardButton("Редактировать цену", callback_data='btn5')],
                 [InlineKeyboardButton("Сохранить заказ", callback_data='btn6')]]
markup3 = InlineKeyboardMarkup(sell_keyboard)

# меню скупщика:

buy_keyboard = [[InlineKeyboardButton("Редактировать теги", callback_data='btn1'), InlineKeyboardButton("Фильтры", callback_data='btn2')], [InlineKeyboardButton("Поиск", callback_data='btn3'), InlineKeyboardButton("Назад >", callback_data='btn4')]]
markup4 = InlineKeyboardMarkup(buy_keyboard)

# редактирование тегов:
buy_keyboard = [[InlineKeyboardButton("Сохранить теги", callback_data='btn1')]]
markup5 = InlineKeyboardMarkup(buy_keyboard)

# фильтры:
filtres_keyboard = [[InlineKeyboardButton("Цена", callback_data='btn1')]] #,[InlineKeyboardButton("Популярность", callback_data='btn2')]]
markup6 = InlineKeyboardMarkup(filtres_keyboard)

# фильтры цены:
cost_filter_keyboard = [[InlineKeyboardButton("мин_цена", callback_data='btn1')], [InlineKeyboardButton("макс_цена", callback_data='btn2')]]
markup7 = InlineKeyboardMarkup(cost_filter_keyboard)

# фильтры популярности:
population_filter_keyboard = [[InlineKeyboardButton("мин_популярность", callback_data='btn1')], [InlineKeyboardButton("макс_популярность", callback_data='btn2')]]
markup8 = InlineKeyboardMarkup(population_filter_keyboard)


# назад/дальше:
last_new_keyboard = [[InlineKeyboardButton("< Назад", callback_data='btn1'), InlineKeyboardButton("Далее >", callback_data='btn2')], [InlineKeyboardButton("Выйти в меню поиска", callback_data='btn3')]]
markup9 = InlineKeyboardMarkup(last_new_keyboard)

