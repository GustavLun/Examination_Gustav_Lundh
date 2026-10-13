from src.fav_books import FavoriteBooks
class Book:
    def __init__(self, id, author, title):
        self.id = id
        self.title = title
        self.author = author



class BookStore:
    def __init__(self, favorites=None):
        self.book_list = []
        self.next_id = 1
        self.favorites = favorites if favorites is not None else FavoriteBooks()



    def addBook(self, author, title):
        book = Book(self.next_id, author, title)
        self.next_id += 1
        self.book_list.append(book)
        return book

    def toggle_favorite(self, book_id):
        for book in self.book_list:
            if book.id == book_id:
                if book in self.favorites.Favorites:
                    self.favorites.remove(book)
                else:
                    self.favorites.add(book)
