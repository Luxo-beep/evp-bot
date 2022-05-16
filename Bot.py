import telebot
from telebot import types
print('Бот запущен')
# Создаем экземпляр бота
bot = telebot.TeleBot('5309216038:AAFCgPEzMjDUer1vPunjfVkTwIfvMw_HRSI')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет. Бот для эйфории на связи, чтобы начать отправь мне свой код и получишь список промокодов".format(message.from_user), reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def get_text_messages(message):
 if(message.text == "❓ Задать вопрос"):
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   bot.send_message(message.chat.id, text="Hапиши @votsi_ken если хочешь получить помощь", reply_markup=markup)
 if message.text == "2284":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/1.xlsx', 'rb'))
 if message.text == "280990":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/2.xlsx', 'rb'))
 if message.text == "arisha34030":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/3.xlsx', 'rb'))
 if message.text == "27ko4ergin27":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/4.xlsx', 'rb'))
 if message.text == "7777777":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/5.xlsx', 'rb'))
 if message.text == "foom.naa15":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/6.xlsx', 'rb'))
 if message.text == "dora232919":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/7.xlsx', 'rb'))
 if message.text == "Dashka":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/8.xlsx', 'rb'))
 if message.text == "marrie669":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/9.xlsx', 'rb'))
 if message.text == "Artem1":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/10.xlsx', 'rb'))
 if message.text == "Artem2":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/11.xlsx', 'rb'))
 if message.text == "Andrey1":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/12.xlsx', 'rb'))
 if message.text == "Andrey2":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/13.xlsx', 'rb'))
 if message.text == "18963LmirryCM":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/14.xlsx', 'rb'))
 if message.text == "Testcode":
    bot.send_document(message.from_user.id, document=open('/evp-bot/1/15.xlsx', 'rb'))
 elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши @votsi_ken если есть вопросы")
# Запускаем бота
bot.polling(none_stop=True, interval=0)

print('Hello World')
