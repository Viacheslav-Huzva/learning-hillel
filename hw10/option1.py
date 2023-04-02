import os


# Функція зчитування нотаток з файлу
def read_notes():
    filename = "notes.txt"
    notes = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            notes = [line.strip() for line in file.readlines()]
    return notes


# Функція запису нотаток до файлу
def write_notes(notes):
    filename = "notes.txt"
    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")


if __name__ == "__main__":
    # Зчитуємо нотатки з файлу при запуску програми
    notes = read_notes()

    # Виводимо вітання та пояснення команд користувачу
    print("Welcome to the notes app! Available commands: add, earliest, latest, longest, shortest, save & exit")
    print("Note: you cannot enter numbers.")

    # цикл для обробки команд користувача
    while True:
        command = input("Enter command: ")

        # Вихід з програми
        if command == "save & exit":
            # Записуємо нотатки до файлу та завершуємо роботу програми
            write_notes(notes)
            print("Notes saved to file. Goodbye!")
            break

        # Додавання нової нотатки
        elif command == "add":
            note = input("Enter note: ")
            # Додаємо нову нотатку до поточної пам'яті
            notes.append(note)
            # Додаємо нову нотатку до файлу
            write_notes(notes)
