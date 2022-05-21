import telebot
from telebot import types
print('Бот запущен')
# Создаем экземпляр бота
bot = telebot.TeleBot('5374854792:AAE1v9jSq2Y5ThRgCwPGP0S086m2ObPNq-g')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💩 Акция 5+1")
    btn2 = types.KeyboardButton("💀 Кончились коды")
    btn3 = types.KeyboardButton("🩸 Забыли код?")
    btn4 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Привет. Бот для эйфории на связи, чтобы начать отправь мне свой код и получишь список промокодов".format(message.from_user), reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def get_text_messages(message):
 if(message.text == "❓ Задать вопрос"):
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   bot.send_message(message.chat.id, text="Hапиши @evp_promo_support_bot если хочешь получить помощь ♥", reply_markup=markup)
if(message.text == "💀 Кончились коды"):
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
bot.send_message(message.chat.id, text="Просто напиши в @evp_promo_support_bot свой старый код с добавлением #НОВЫЙКОД ♥", reply_markup=markup)
if(message.text == "🩸 Забыли код?"):
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
bot.send_message(message.chat.id, text="Сразу пиши в @evp_promo_support_bot и жди ответа в течении часа ♥", reply_markup=markup)
if(message.text == "💩 Акция 5+1"):
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
bot.send_message(message.chat.id, text="Отправь все 5 номеров билетов одним сообщением в @evp_promo_support_bot с добавлением #5+1 ♥", reply_markup=markup)
if message.text == "2284":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/1.xlsx', 'rb'))
if message.text == "280990":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/2.xlsx', 'rb'))
if message.text == "arisha34030":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/3.xlsx', 'rb'))
if message.text == "27ko4ergin27":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/4.xlsx', 'rb'))
if message.text == "7777777":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/5.xlsx', 'rb'))
if message.text == "foom.naa15":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/6.xlsx', 'rb'))
if message.text == "dora232919":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/7.xlsx', 'rb'))
if message.text == "Dashka":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/8.xlsx', 'rb'))
if message.text == "marrie669":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/9.xlsx', 'rb'))
if message.text == "esssmiraldino":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/10.xlsx', 'rb'))
if message.text == "Testcode193032":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/11.xlsx', 'rb'))
if message.text == "Alcollitet12341":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/12.xlsx', 'rb'))
if message.text == "Testcode194587":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/13.xlsx', 'rb'))
if message.text == "18963LmirryCM":
    bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/14.xlsx', 'rb'))
if message.text == "polya1111":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/15.xlsx', 'rb'))
if message.text == "6877614":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/16.xlsx', 'rb'))
if message.text == "9883359":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/17.xlsx', 'rb'))
if message.text == "4334160":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/18.xlsx', 'rb'))
if message.text == "7258401":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/19.xlsx', 'rb'))
if message.text == "1008688":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/20.xlsx', 'rb'))
if message.text == "8563029":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/21.xlsx', 'rb'))
if message.text == "4628973":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/22.xlsx', 'rb'))
if message.text == "2537906":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/23.xlsx', 'rb'))
if message.text == "9241614":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/24.xlsx', 'rb'))
if message.text == "3936195":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/25.xlsx', 'rb'))
if message.text == "9328842":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/26.xlsx', 'rb'))
if message.text == "9382878":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/27.xlsx', 'rb'))
if message.text == "1031977":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/28.xlsx', 'rb'))
if message.text == "5674482":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/29.xlsx', 'rb'))
if message.text == "8229546":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/30.xlsx', 'rb'))
if message.text == "6123033":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/31.xlsx', 'rb'))
if message.text == "4106663":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/32.xlsx', 'rb'))
if message.text == "7448216":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/33.xlsx', 'rb'))
if message.text == "1979200":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/34.xlsx', 'rb'))
if message.text == "8829498":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/35.xlsx', 'rb'))
if message.text == "1556586":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/36.xlsx', 'rb'))
if message.text == "6234437":
       bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/37.xlsx', 'rb'))
if message.text == "2394158":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/38.xlsx', 'rb'))
if message.text == "9262047":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/39.xlsx', 'rb'))
if message.text == "8229554":
        bot.send_document(message.from_user.id, document=open('/home/ubuntu/evp-bot/Excel/40.xlsx', 'rb'))
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши @evp_promo_support_bot для создания запроса")
# Запускаем бота
bot.polling(none_stop=True, interval=0)

print('Hello World')
