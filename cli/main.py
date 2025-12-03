# main.py - simple menu to use the inventory
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    inv = LibraryInventory(json_path="books.json")

    while True:
        print("\n1 Add Book  2 Issue by ISBN  3 Return by ISBN  4 View All  5 Search Title  6 Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            t = input("Title: ").strip()
            a = input("Author: ").strip()
            i = input("ISBN: ").strip()
            if t and a and i:
                ok = inv.add_book(Book(t, a, i))
                if ok:
                    inv.save()
                    print("Added.")
                else:
                    print("ISBN exists.")
            else:
                print("All fields required.")

        elif choice == "2":
            isbn = input("ISBN to issue: ").strip()
            ok, msg = inv.issue_by_isbn(isbn)
            print(msg)

        elif choice == "3":
            isbn = input("ISBN to return: ").strip()
            ok, msg = inv.return_by_isbn(isbn)
            print(msg)

        elif choice == "4":
            books = inv.display_all()
            if not books:
                print("No books.")
            else:
                for b in books:
                    print(b)

        elif choice == "5":
            q = input("Search title: ").strip()
            res = inv.search_by_title(q)
            if res:
                for b in res:
                    print(b)
            else:
                print("No matches.")

        elif choice == "6":
            print("Exit.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
