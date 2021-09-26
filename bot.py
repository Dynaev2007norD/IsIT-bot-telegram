import telebot
import random
from telebot import types
import time

bot = telebot.TeleBot('1941385343:AAH0kEv3JFAljg_1LTqduJL09R5CCVdt2ik')


@bot.message_handler(content_types=['text', 'url', 'switch'])
def get_text_messages(message):
    # приветствие
    if "прив" in message.text.lower():
        bot.send_message(message.from_user.id, "Привет")
    # код доступа к игре
    if "код доступа" in message.text.lower():
        bot.send_message(message.from_user.id, (''.join(
            [random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(32)])))
    # помощь
    if "баг" in message.text.lower():
        bot.send_message(message.from_user.id, "Опишите баг")
    elif "помо" in message.text.lower() and "баг" not in message.text.lower():
        bot.send_message(message.from_user.id, "Опишите проблему")

    # игра
    if "игр" in message.text.lower():
        bot.send_message(message.from_user.id, "Игра ещё в разработке")
    # прощание
    if "пок" in message.text.lower():
        bot.send_message(message.from_user.id, "Пока")
    # админ панель
    elif message.text == "АДМИН ПАНЕЛЬ":
        bot.send_message(message.from_user.id, "Введите код")
        if message.text == "adminpassword":
            time.sleep(10)
            bot.send_message(message.from_user.id, "Выберите действие")


bot.polling(none_stop=True, interval=0)
# идея на потом: сделать чтобы при покупке генерировался рандомный ключ из 32 символов и заносился в базу данных. Сделать админ - пане