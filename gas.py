import telebot

# Создание экземпляра бота с указанием токена
bot = telebot.TeleBot("6106659280:AAHIyp4nN5ApxqnCzId0GzOcIFogvTt_CH0")

# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Привет! Я бот для расчета стоимости поездки.")
    bot.reply_to(message, "Пожалуйста, введи расход топлива на 100 км:")

# Функция для обработки сообщения с расходом топлива
@bot.message_handler(func=lambda message: True)
def fuel_consumption_handler(message):
    try:
        fuel_consumption = float(message.text)
        bot.reply_to(message, "Отлично! Теперь введи цену 1 литра топлива:")
        bot.register_next_step_handler(message, price_per_liter_handler, fuel_consumption)
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введи число.")

# Функция для обработки сообщения с ценой топлива
def price_per_liter_handler(message, fuel_consumption):
    try:
        price_per_liter = float(message.text)
        bot.reply_to(message, "Хорошо! Теперь введи расстояние, которое нужно преодолеть:")
        bot.register_next_step_handler(message, distance_handler, fuel_consumption, price_per_liter)
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введи число.")

# Функция для обработки сообщения с расстоянием
def distance_handler(message, fuel_consumption, price_per_liter):
    try:
        distance = float(message.text)
        total_cost = calculate_fuel_cost(fuel_consumption, price_per_liter, distance)
        bot.reply_to(message, f"Стоимость поездки: {total_cost:.2f} грн")
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введи число.")

# Функция для расчета стоимости поездки
def calculate_fuel_cost(fuel_consumption, price_per_liter, distance):
    fuel_consumption_per_km = fuel_consumption * distance / 100
    total_cost = fuel_consumption_per_km * price_per_liter
    return total_cost

# Запуск бота
bot.polling()
