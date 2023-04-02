import re

NOTES_FILE = "notes.txt"

def save_notes(notes):
    with open(NOTES_FILE, "a") as f:
        for note in notes:
            f.write(note + "\n")

def load_notes():
    notes = []
    try:
        with open(NOTES_FILE, "r") as f:
            for line in f:
                note = line.strip()
                if note:
                    notes.append(note)
    except FileNotFoundError:
        pass
    return notes

def add_note():
    note = input("Enter your note: ")
    while re.search(r'\d', note):
        print("Error: Note should not contain digits")
        note = input("Enter your note: ")
    notes.append(note)

def display_notes(sort_key):
    sorted_notes = sorted(notes, key=sort_key)
    print("\n".join(sorted_notes))

def main():
    global notes
    notes = load_notes()
    print("Welcome to Notes App!")
    while True:
        command = input("Enter command (add, earliest, latest, longest, shortest, or save & exit): ")
        if command == "add":
            add_note()
        elif command == "earliest":
            display_notes(lambda note: notes.index(note))
        elif command == "latest":
            display_notes(lambda note: -notes.index(note))
        elif command == "longest":
            display_notes(lambda note: len(note))
        elif command == "shortest":
            display_notes(lambda note: -len(note))
        elif command == "save & exit":
            save_notes(notes)
            print("Notes saved to file. Exiting...")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
