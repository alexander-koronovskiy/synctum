import telebot
from router import parse_to_add

# Токен вашего телеграм бота
TOKEN = '6934425663:AAHPK8N7O_IRt2K98V78fCiF02yDWCqNwPM'
HELLO = 'Привет! Попытай удачу! Отправь свое имя и ставку от 1 до 10 в формате: Ваше Имя / Ставка!'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    if message.text == '/start':
        bot.send_message(chat_id, HELLO)
    else:
        try:
            parse_to_add(message)
            bot.send_message(chat_id, "Ставка сделана!")

        except Exception as e:
            bot.send_message(chat_id, "Ошибка! Попробуйте еще раз.")

bot.infinity_polling()
