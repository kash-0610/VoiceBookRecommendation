books = {
    "Mystery": [
        ("The Silent Patient", "Alex Michaelides"),
        ("Gone Girl", "Gillian Flynn"),
        ("The Girl with the Dragon Tattoo", "Stieg Larsson")
    ],

    "Romance": [
        ("The Notebook", "Nicholas Sparks"),
        ("Pride and Prejudice", "Jane Austen"),
        ("Me Before You", "Jojo Moyes")
    ],

    "Fantasy": [
        ("Harry Potter", "J.K. Rowling"),
        ("The Hobbit", "J.R.R. Tolkien"),
        ("The Name of the Wind", "Patrick Rothfuss")
    ],

    "Sci-Fi": [
        ("Dune", "Frank Herbert"),
        ("Foundation", "Isaac Asimov"),
        ("Ender's Game", "Orson Scott Card")
    ],

    "Horror": [
        ("The Shining", "Stephen King"),
        ("Dracula", "Bram Stoker"),
        ("Frankenstein", "Mary Shelley")
    ]
}

# Display all books
for book_type, book_list in books.items():
    print("\n", book_type)
    print("----------------")

    for book_name, author in book_list:
        print("Book Name:", book_name)
        print("Author   :", author)