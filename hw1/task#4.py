import telebot

bot = telebot.TeleBot('6106659280:AAHIyp4nN5ApxqnCzId0GzOcIFogvTt_CH0')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)

Fuel_consumption = float(input("витрачання палива автомобілем за 100 км"))
price_for_1_liter = float(input("сьогоднішня ціна 1 л палива"))
distance = float(input("скільки кілометрів треба здолати"))

Fuel_consumption = Fuel_consumption * distance / 100  # узнаем цену за 1 км
answer = Fuel_consumption * price_for_1_liter  # цена за всю поездку
print(f'{answer:.2f} грн')
