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
 if message.text == "123456":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/1.xlsx', 'rb'))
 if message.text == "918827":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/2.xlsx', 'rb'))
 if message.text == "243751":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/3.xlsx', 'rb'))
 if message.text == "258185":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/4.xlsx', 'rb'))
 if message.text == "954321":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/5.xlsx', 'rb'))
 if message.text == "145560":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/6.xlsx', 'rb'))
 if message.text == "326561":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/7.xlsx', 'rb'))
 if message.text == "890752":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/8.xlsx', 'rb'))
 if message.text == "662604":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/9.xlsx', 'rb'))
 if message.text == "856067":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/10.xlsx', 'rb'))
 if message.text == "653790":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/11.xlsx', 'rb'))
 if message.text == "716423":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/12.xlsx', 'rb'))
 if message.text == "293698":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/13.xlsx', 'rb'))
 if message.text == "537479":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/14.xlsx', 'rb'))
 if message.text == "345176":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/1/15.xlsx', 'rb'))
 elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши @votsi_ken если есть вопросы")
# Запускаем бота
bot.polling(none_stop=True, interval=0)

print('Hello World')