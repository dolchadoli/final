from library import Library

def main():
    library = Library()

    while True:
        try:
            #asarchevi menu
            operation = int(input('''Welcome to our bookstore! What would you like to do?
                        1. Add book
                        2. Issue book
                        3. Return book
                        4. View available books
                        5. Exit
                        Enter your choice: '''))
            
            if operation == 1:
                #axali wignis damateba
                title = input("Enter the book title: ")
                author = input("Enter the book author: ")
                library.add_book(title, author)
            
            elif operation == 2:
                #wignis ageba
                title = input("Enter the book title to issue: ")
                library.issue_book(title)
            
            elif operation == 3:
                #wignis dabruneba
                title = input("Enter the book title to return: ")
                library.return_book(title)
            
            elif operation == 4:
                #wignebis naxva
                library.view_books()
            
            elif operation == 5:
                #programis gatishva
                print("Exiting the system. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
