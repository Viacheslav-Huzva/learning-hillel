notes = []


def add_note():
    """Додавання нотатки"""
    note = input("Enter note: ")
    if not note.isdigit():
        notes.append(note)
    else:
        print("Invalid note.")


def show_notes(order_func):
    """Виведення нотаток у заданому порядку"""
    sorted_notes = order_func(notes)
    num_notes = int(input("How many notes do you want to see? "))
    for note in sorted_notes[:num_notes]:
        print(note)


def order_earliest(notes):
    """Повертає список нотаток у хронологічному порядку - від найранішої до найпізнішої"""
    return notes


def order_latest(notes):
    """Повертає список нотаток у хронологічному порядку - від найпізнішої до найранішої"""
    return reversed(notes)


def order_longest(notes):
    """Повертає список нотаток у порядку їх довжини - від найдовшої до найкоротшої"""
    return sorted(notes, key=len, reverse=True)


def order_shortest(notes):
    """Повертає список нотаток у порядку їх довжини - від найкоротшої до найдовшої"""
    return sorted(notes, key=len)


def exit_program():
    """Вихід з програми"""
    print("Exiting program...")
    quit()


while True:
    command = input("Enter command (add/earliest/latest/longest/shortest/exit): ")
    if command == "add":
        add_note()
    elif command == "earliest":
        show_notes(order_earliest)
    elif command == "latest":
        show_notes(order_latest)
    elif command == "longest":
        show_notes(order_longest)
    elif command == "shortest":
        show_notes(order_shortest)
    elif command == "exit":
        exit_program()
    else:
        print("Invalid command.")
