def add_note(notes):
    """Функція додавання нової нотатки в список notes."""
    note = input("Enter note: ")
    if not note.isdigit():
        notes.append(note)
    else:
        print("Invalid note.")
    return notes


def show_earliest(notes):
    """Функція виведення всіх нотаток в хронологічному порядку (від найранішої до найпізнішої)."""
    for note in notes:
        print(note)


def show_latest(notes):
    """Функція виведення всіх нотаток в зворотньому хронологічному порядку (від найпізнішої до найранішої)."""
    for note in reversed(notes):
        print(note)


def show_longest(notes):
    """Функція виведення всіх нотаток у порядку їх довжини (від найдовшої до найкоротшої)."""
    sorted_notes = sorted(notes, key=len, reverse=True)
    for note in sorted_notes:
        print(note)


def show_shortest(notes):
    """Функція виведення всіх нотаток у порядку їх довжини (від найкоротшої до найдовшої)."""
    sorted_notes = sorted(notes, key=len)
    for note in sorted_notes:
        print(note)


def main():
    """Основна функція програми."""
    notes = []
    while True:
        command = input("Enter command (add/earliest/latest/longest/shortest/exit): ")
        if command == "add":
            notes = add_note(notes)
        elif command == "earliest":
            show_earliest(notes)
        elif command == "latest":
            show_latest(notes)
        elif command == "longest":
            show_longest(notes)
        elif command == "shortest":
            show_shortest(notes)
        elif command == "exit":
            print("Exiting program...")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
