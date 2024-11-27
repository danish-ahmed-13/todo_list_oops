books = []

def add_book(title):
    books.append(title)
    print(f"Book {title} has been added successfully")

def update_book(old_title, new_title):
    if old_title in books:
        books.remove(old_title)
        books.append(new_title)
        print(f"{old_title} updated to {new_title} successfully")
    else:
        print(f"Book {old_title} not found")

def delete_book(title):
    if title in books:
        books.remove(title)
        print(f"{title} has been deleted successfully")
    else:
        print(f"{title} book not found")

def view_book():
    for book in books:
        print(f"{book}")
    if not books:
        print("No books available.")


while True:
    print("\n-----Book management system------")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. View Book")
    print("5. Exit")

    choice = int(input("Enter the choice (1-5): "))

    if choice == 1:
        title = input("Enter book title: ")
        add_book(title)

    elif choice == 2:
        old_title = input("Enter the current title of the book: ")
        new_title = input("Enter the new title for the book: ")
        update_book(old_title, new_title)

    elif choice == 3:
        title = input("Enter the title of the book to delete: ")
        delete_book(title)

    elif choice == 4:
        view_book()

    elif choice == 5:
        print("Closing the program...")
        break

    else:
        print("Invalid choice. Please try again") 
