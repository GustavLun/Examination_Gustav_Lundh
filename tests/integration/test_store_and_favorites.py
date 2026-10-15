import pytest
from src.book_store import BookStore
from src.fav_books import FavoriteBooks


@pytest.mark.integration
@pytest.mark.integration_store_and_favorites
def test_togglefavorite_adds_book_to_favorites():
    favorites = FavoriteBooks()
    store = BookStore(favorites)

    book = store.addBook( "Chaplin", "Runway")

    store.toggle_favorite(book.id)
    assert book in favorites.Favorites

@pytest.mark.integration
@pytest.mark.integration_store_and_favorites
def test_toggle_favorite_twice_removes_book_from_favorites():
    favorites = FavoriteBooks()
    store = BookStore(favorites)

    book = store.addBook("Chaplin", "Runway")

    store.toggle_favorite(book.id)

    store.toggle_favorite(book.id)
    assert book not in favorites.Favorites