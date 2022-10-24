import telebot
from telebot import types
bot = telebot.TeleBot("5202477338:AAFFgxbKRs1Oh23TU7OxnbkWaLaxMpaUrJI")
permission = True


@bot.message_handler(commands=["start", "старт"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Команди", url="https://www.youtube.com/watch?v=HodO2eBEz_8"))
    if message.from_user.last_name is None:
        message.from_user.last_name = ""
    bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name} {message.from_user.last_name}! Цього"
                                      f" бота створив Хоренко Михайло, учень 7-Б класу у 2022 році. "
                                      f"Цей бот був створений для контролювання чату та розважальних цілей. "
                                      f"Нижче ти можеш передивитися усі команди цього бота та почати користуватися їм"
                                      f".", reply_markup=markup)


@bot.message_handler(commands=["help"])
def helping(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Потрібно відповісти на повідомлення!")
    else:
        # bot.delete_message(message.chat.id, message.message_id)
        bot.kick_chat_member(message.chat.id, message.reply_to_message.id)


@bot.message_handler(commands=["-мати"])
def off_mat(message):
    global permission
    permission = True
    bot.reply_to(message, "Фільтр матів включено!")


@bot.message_handler(commands=["+мати"])
def on_mat(message):
    global permission
    permission = False
    bot.reply_to(message, "Фільтр матів виключено!")


@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text == "Привіт":
        bot.send_message(message.chat.id, "Привіт")
    if message.text == "Пока":
        bot.send_message(message.chat.id, "Пока")
    if message.text == "Як справи?":
        bot.send_message(message.chat.id, "Добре, а в тебе?")
    if message.text == "Погано":
        bot.send_message(message.chat.id, "Чому?")
    if message.text == "Зрозумів?":
        bot.send_message(message.chat.id, "Так")
    if message.text == "З днем народження!":
        bot.send_message(message.chat.id, "Дякую!")
    if message.text == "Ура!":
        bot.send_message(message.chat.id, "Ура!")
    if message.text == "Дивись":
        bot.send_message(message.chat.id, "Дивлюся")
    if message.text == "Бачиш?":
        bot.send_message(message.chat.id, "Бачу")
    else:
        if message.text == "Тому":
            bot.send_message(message.chat.id, "Кукаренду")
        if message.text == "Чого?":
            bot.send_message(message.chat.id, "Того")
        if message.text == "Чому?":
            bot.send_message(message.chat.id, "Тому")
        if message.text == "Скільки?":
            bot.send_message(message.chat.id, "Багато")
        if message.text == "Кого?":
            bot.send_message(message.chat.id, "Курей")
        if message.text == "Як в тебе справи?":
            bot.send_message(message.chat.id, "Добре, а в тебе?")
        if message.text == "Скільки тобі років?":
            bot.send_message(message.chat.id, "267")
        if message.text == "Ого":
            bot.send_message(message.chat.id, "Чого ти?")
        else:
            if message.text == "Та нічого":
                bot.send_message(message.chat.id, "Добре")
            if message.text == "Забудь":
                bot.send_message(message.chat.id, "Ні")
            if message.text == "Бот":
                bot.send_message(message.chat.id, "Я тут")
            if permission == True:
                if message.text == "бля":
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, "УВАГА! Заборонено матюкатися в нашому чаті!")
                if message.text == "сука":
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, "УВАГА! Заборонено матюкатися в нашому чаті!")
                if message.text == "ебать":
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, "УВАГА! Заборонено матюкатися в нашому чаті!")


# @bot.message_handler(commands=["+вихід"])
# def start(message):
#   markup = types.InlineKeyboardMarkup()
#   markup.add(types.InlineKeyboardButton("Команди", url="https://www.youtube.com/watch?v=HodO2eBEz_8"))
#   bot.send_message(message.chat.id, "Привіт! Цього бота створив Хоренко Михайло, учень 7-Б класу у 2022 році. "
#                                     "Цей бот був створений для контролювання чату та розважальних цілей. "
#                                     "Нижче ти можеш передивитися усі команди цього бота та почати користуватися їм"
#                                     ".", reply_markup=markup)
#

bot.polling(none_stop=True)