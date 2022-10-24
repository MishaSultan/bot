import logging
from aiogram import Bot, Dispatcher, executor
import time

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5202477338:AAFFgxbKRs1Oh23TU7OxnbkWaLaxMpaUrJI")
dp = Dispatcher(bot)
x = 0
ID = 0
NAME = ""


@dp.message_handler(content_types=["text"])
async def answer(message):
    if "бля" in message.text:
        global ID
        global NAME
        global x
        x = x + 1
        ID = message.from_user.id
        NAME = message.from_user.full_name
        mes = message.text
        await message.reply(f"На Вас поданна жалоба! \nСкоро админ решит: жить Вам или нет. \nПричина жалоби: Матюки")
        logger = logging.getLogger(str(x))
        logger.warning(f'Жалоба на: ID:{ID}, Имя: {NAME}. Причина жалоби: Матюки. Содержимое сообщения: {mes}. {time.asctime()}')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)