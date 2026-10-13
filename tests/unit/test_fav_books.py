from src.book_store import Book
from src.book_store import BookStore
from src.fav_books import FavoriteBooks

def test_add_book_to_favorites():
    favorites = FavoriteBooks()
    store = BookStore()

    book = store.addBook("chaplin", "runaway")

    favorites.add(book)

    assert book in favorites.Favorites

def test_remove_book_from_favorites():
    favorites = FavoriteBooks()
    store = BookStore()

    book = store.addBook("chaplin", "runaway")

    favorites.add(book)
    favorites.remove(book)

    assert book not in favorites.Favorites
