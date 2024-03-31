# Sample book dataset
books = [
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Fiction'},
    {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian'},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Romance'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'Fiction'},
    {'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Dystopian'},
    {'title': 'Jane Eyre', 'author': 'Charlotte Brontë', 'genre': 'Romance'},
    {'title': 'Lord of the Flies', 'author': 'William Golding', 'genre': 'Fiction'},
    {'title': 'Animal Farm', 'author': 'George Orwell', 'genre': 'Dystopian'},
    {'title': 'Gone with the Wind', 'author': 'Margaret Mitchell', 'genre': 'Romance'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Fiction'}
]

# Function to get book recommendations based on user preferences
def get_book_recommendations(user_preferences, books):
    # Filter books based on user preferences (genre)
    recommended_books = [book for book in books if book['genre'] == user_preferences]
    return recommended_books

print("Welcome to Utkarsha's recommendation System!! \n")

# Get user preferences
user_preferences = input("Enter your preferred genre (e.g., Fiction, Romance, Dystopian): ")

print(f"Books are recommended based on {user_preferences} genre.")
# Get book recommendations based on user preferences
recommendations = get_book_recommendations(user_preferences, books)

# Print recommended books
if recommendations:
    print("Recommended Books:")
    for book in recommendations:
        print(f"{book['title']} by {book['author']}")
else:
    print("Sorry, no books found for the specified genre.")
