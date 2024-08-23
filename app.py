import telebot

TOKEN = '7536297476:AAEG3suBUyHNzi850eiMT9izYea4gDwN-Kk'

bot = telebot.TeleBot(TOKEN)

keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Для начала работы введите команду по следующему шаблону: \n <имя валюты> \
<в какую валюту перевести> <количество переводимой валюты> \n Увидеть список доступных валют:  /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


bot.polling()
