import sqlite3

DB_FILE = "phonebook.db"


def print_entries(rows):
    if not rows:
        print("No entries found.")
        return
    for name, phone in rows:
        print(f"{name:<20} Phone: {phone}")


def main():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    while True:
        print("\nPhonebook Menu")
        print("1. Add new entry")
        print("2. Look up phone number")
        print("3. Update phone number")
        print("4. Delete entry")
        print("5. List all entries")
        print(" type exit to Exit")

        choice = input("\nEnter a number: ")


        # choice number 1
        if choice == "1":
            name = input("Name: ").strip().lower()
            phone = input("Phone: ").strip().lower()
            #phone is lowered just in case (honistly i have no idea but it looks simertical this way)

            if name and phone:
                cursor.execute("INSERT INTO Entries (name, phone) VALUES (?, ?)", (name, phone))
                conn.commit()
                print(f"Added {name}: {phone}")
            else:
                print("Name and phone cannot be empty.")


        # choice number 2
        elif choice == "2":
            term = input("Search name or phone: ").strip()

            cursor.execute(
                "SELECT name, phone FROM Entries WHERE name LIKE ? OR phone LIKE ?",
                (f"%{term}%", f"%{term}%")
            )
            print("\nSearch results:")
            print_entries(cursor.fetchall())


        # choice number 3
        elif choice == "3":
            name = input("Name to update: ").strip()
            new_phone = input("New phone: ").strip()

            cursor.execute("UPDATE Entries SET phone=? WHERE name=?", (new_phone, name))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"Updated your entry.")
            else:
                print(f"No entry found for '{name}'.")


        # choice number 4
        elif choice == "4":
            name = input("Name to delete: ").strip()

            if input(f"Delete {name}? (y/n): ").lower() == "y":
                cursor.execute("DELETE FROM Entries WHERE name=?", (name,))
                conn.commit()

                if cursor.rowcount > 0:
                    print(f"Deleted your entry.")
                else:
                    print(f"No entry found for '{name}'.")
            else:
                print("Deletion canceled.")


        # choice number 5
        elif choice == "5":
            cursor.execute("SELECT name, phone FROM Entries ORDER BY name")
            print("\nAll entries:")
            print_entries(cursor.fetchall())

        elif choice.lower() == "exit":
            break

        else:
            print("Enter 1–5 or exit")

    conn.close()


if __name__ == "__main__":
    main()
