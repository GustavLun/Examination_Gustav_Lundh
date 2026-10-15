from src.book_store import BookStore
from src.fav_books import FavoriteBooks

def test_togglefavorite_adds_book_to_favorites():
    favorites = FavoriteBooks()
    store = BookStore(favorites)

    book = store.addBook( "Chaplin", "Runway")

    store.toggle_favorite(book.id)
    assert book in favorites.Favorites