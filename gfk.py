library = []  
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    book = {"title": title, "author": author, "year": year}
    library.append(book)
    print("Book added successfully!\n")

def show_books():
    if not library:
        print("No books in the library.\n")
    else:
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']})")
        print()

def search_book():
    keyword = input("Enter title to search: ").lower()
    found = False
    for book in library:
        if keyword in book['title'].lower():
            print(f"Found: {book['title']} by {book['author']} ({book['year']})")
            found = True
    if not found:
        print("Book not found.\n")

def delete_book():
    title = input("Enter the title of the book to delete: ").lower()
    for book in library:
        if book['title'].lower() == title:
            library.remove(book)
            print("Book deleted successfully!\n")
            return
    print("Book not found.\n")

def main():
    while True:
        print("=== Library Management System ===")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Search for a book")
        print("4. Delete a book")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


    main()
