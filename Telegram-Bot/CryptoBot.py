import telebot
from telebot import types

API_TOKEN = '6997973770:AAGOeUfGvqufYta2pesvyUddVFS-zxB5fS8'
bot = telebot.TeleBot(API_TOKEN)

ADMIN_CHAT_ID = '@clients_46'

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Я бот-помощник по обмену криптовалюты.")
    bot.send_message(message.chat.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, process_name_step)

def process_name_step(message):
    user_name = message.text
    bot.send_message(message.chat.id, f"Отлично! Тебя зовут {user_name}.")
    bot.send_message(message.chat.id, "Какую криптовалюту ты хочешь обменять?")
    bot.register_next_step_handler(message, process_currency_step, user_name)

def process_currency_step(message, user_name):
    currency = message.text
    bot.send_message(message.chat.id, "Все готово для обмена! Ожидайте ответа администратора.")


    admin_message = f"Пользователь @{message.from_user.username} ({user_name}) хочет обменять {currency}."
    bot.send_message(ADMIN_CHAT_ID, admin_message)

bot.polling(none_stop=True)
