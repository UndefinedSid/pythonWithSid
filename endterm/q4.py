import csv


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print("Book removed successfully.")
                return

        print("Book with the given ISBN was not found.")

    def display_books(self):
        if not self.books:
            print("No books are currently available in the library.")
            return

        print("\nCurrent books in the library:")
        for book in self.books:
            print(book)

    def save_to_file(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "ISBN"])

            for book in self.books:
                writer.writerow([book.title, book.author, book.isbn])

        print(f"Library details saved to {filename}.")


library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add book")
    print("2. Remove book")
    print("3. Display books")
    print("4. Save to CSV file")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")

        book = Book(title, author, isbn)
        library.add_book(book)

    elif choice == "2":
        isbn = input("Enter ISBN of the book to remove: ")
        library.remove_book(isbn)

    elif choice == "3":
        library.display_books()

    elif choice == "4":
        filename = input("Enter CSV filename: ")
        library.save_to_file(filename)

    elif choice == "5":
        print("Exiting Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
