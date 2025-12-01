import sqlite3

DB_FILE = "phonebook.db"

def main():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    add_entries_table(cur)
    add_entries(cur)

    conn.commit()

    display_entries(cur)

    conn.close()


def add_entries_table(cur):
    cur.execute("DROP TABLE IF EXISTS Entries")

    cur.execute('''
        CREATE TABLE Entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

# i made sure to use phone numebrs that start with 555 as that is the number designated for fictional works like movies so you dont acdentaly use a real persons phone number
def add_entries(cur):
    entries = [
        ("alice", "555-354-1234"),
        ("bob", "555-223-2345"),
        ("charlie", "555-180-3456"),
        ("david", "555-112-4567"),
        ("eve", "555-225-5678")
    ]

    for name, phone in entries:
        cur.execute('''
            INSERT INTO Entries (name, phone)
            VALUES (?, ?)
        ''', (name.lower(), phone))


def display_entries(cur):
    print("Contents of phonebook.db / Entries table:")
    cur.execute("SELECT * FROM Entries")
    rows = cur.fetchall()

    for row in rows:
        _id, name, phone = row
        print(f"{_id:<3}{name:<20}{phone}")


if __name__ == "__main__":
    main()
