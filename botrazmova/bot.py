# запускаем цыкл  и даем пользователю отправь сообщение
while True:
    text = input('Введіть повідомлення: ').lower()

    # ключевым словам - готовые ответы. Даем возможность закончить диалог в любой момент

    if 'привіт' in text or 'хай' in text or 'доброго дня' in text or 'прив' in text:
        print('хай, я бот з України')
    elif 'чим займаешся?' in text or 'що робиш?' in text or 'как дз?' in text:
        print('Вчусь програмувати на Python!')
    elif 'фільм' in text or 'кінотеатр' in text or 'серіал' in text:
        print(
            'Соррі, що втручаюсь, не знаю про що йдеться мова, але подивіться серіал "нужно звонить Солу", він дуже інтересний !')
    elif 'бувай' in text or 'надобраніч' in text or 'до зустрічі' in text:
        print('Побачимось у мережі, бувай!')
        break
    else:
        print('Дуже цікаво, але на жаль нічого не зрозуміло')