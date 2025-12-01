import sqlite3

DB_FILE = "cities.db"


def print_city_list(rows):
    if not rows:
        print("No cities found.")
        return
    for city in rows:
        city_id, name, population = city
        print(f"{name:<20}  Population: {population}")

def main():
    cursor = sqlite3.connect(DB_FILE).cursor()

    while True:
        print("\nCity Database Menu")
        print("1. Display cities sorted by population (ascending)")
        print("2. Display cities sorted by population (descending)")
        print("3. Display cities sorted by name")
        print("4. Display total population")
        print("5. Display average population")
        print("6. Display city with highest population")
        print("7. Display city with lowest population")
        print(" type exit to Exit")

        numChoice = input("\nEnter a number: ")

        if numChoice == "1":
            cursor.execute("SELECT * FROM Cities ORDER BY Population ASC")
            print("\nCities sorted by population (ascending):")
            print_city_list(cursor.fetchall())

        elif numChoice == "2":
            cursor.execute("SELECT * FROM Cities ORDER BY Population DESC")
            print("\nCities sorted by population (descending):")
            print_city_list(cursor.fetchall())

        elif numChoice == "3":
            cursor.execute("SELECT * FROM Cities ORDER BY CityName ASC")
            print("\nCities sorted by name:")
            print_city_list(cursor.fetchall())

        elif numChoice == "4":
            cursor.execute("SELECT SUM(Population) FROM Cities")
            total = cursor.fetchone()[0]
            print(f"\nTotal population: {total}")

        elif numChoice == "5":
            cursor.execute("SELECT AVG(Population) FROM Cities")
            avg = cursor.fetchone()[0]
            print(f"\nAverage population: {avg}")

        elif numChoice == "6":
            cursor.execute("SELECT * FROM Cities ORDER BY Population DESC LIMIT 1")
            row = cursor.fetchone()
            print("\nCity with highest population:")
            print_city_list([row])

        elif numChoice == "7":
            cursor.execute("SELECT * FROM Cities ORDER BY Population ASC LIMIT 1")
            row = cursor.fetchone()
            print("\nCity with lowest population:")
            print_city_list([row])

        elif numChoice.lower() == "exit":
            break

        else:
            print("Invalid choice. Enter a number 1–8.")

    sqlite3.connect(DB_FILE).close()


if __name__ == "__main__":
    main()
