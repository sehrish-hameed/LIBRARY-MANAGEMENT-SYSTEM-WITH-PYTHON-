dict = {
    1: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True, "edition": "6th"},
    2: {"title": "1984", "author": "George Orwell", "available": False, "edition": "6th"},
     3: {"title": "1985", "author": "George r.p", "available": False, "edition": "9th"},
}

T1 = input("Enter the book author: ")
T2 = input("Enter the book availability (True/False): ")
T3 = input("Enter the book title: ")
T4 = input("Enter the book edition: ")

while True:
    found = False
    
    # Searching  book information from dictionary
    for book_id, book_info in books_dict.items():
        if book_info["title"] == T3:
            print("Here is the book by title:", book_info)
            found = True
        elif book_info["author"] == T1:
            print("Here is the book by author:", book_info)
            found = True
        elif str(book_info["available"]) == T2:
            print("Here is the book by availability:", book_info)
            found = True
        elif book_info["edition"] == T4:
            print("Here is the book by edition:", book_info)
            found = True
    
    if not found:
        print("Invalid choice, no book found matching the criteria.")
    
    # Break the loop or allow the user to search again
    choice = input("Do you want to search again? (yes/no): ").lower()
    if choice != "yes":
        break
