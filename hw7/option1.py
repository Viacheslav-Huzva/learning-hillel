if __name__ == "__main__":
    notes = []

while True:
    # Виводимо повідомлення користувачу та чекаємо введення команди
    command = input("Enter command (add/earliest/latest/longest/shortest/exit): ")

    if command == "add":
        # Запитуємо користувача про текст нотатки
        note = input("Enter note: ")
        # Перевіряємо, що текст нотатки не містить цифри
        if not note.isdigit():
            # Додаємо нотатку до списку нотаток
            notes.append(note)
        else:
            # Виводимо повідомлення про помилку, якщо текст нотатки містить цифри
            print("Invalid note.")
    elif command == "earliest":
        # Виводимо нотатки у хронологічному порядку - від найранішої до найпізнішої
        for note in notes:
            print(note)
    elif command == "latest":
        # Виводимо нотатки у хронологічному порядку - від найпізнішої до найранішої
        for note in reversed(notes):
            print(note)
    elif command == "longest":
        # Виводимо нотатки у порядку їх довжини - від найдовшої до найкоротшої
        sorted_notes = sorted(notes, key=len, reverse=True)
        for note in sorted_notes:
            print(note)
    elif command == "shortest":
        # Виводимо нотатки у порядку їх довжини - від найкоротшоїдо найдовшої
        sorted_notes = sorted(notes, key=len)
        for note in sorted_notes:
            print(note)
    elif command == "exit":
        # Виводимо повідомлення про вихід з програми та виходимо з циклу
        print("Exiting program...")
        break
    else:
        # Виводимо повідомлення про помилку, якщо користувач ввів неправильну команду
        print("Invalid command.")
