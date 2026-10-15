import pytest
from unittest.mock import Mock
from src.fav_books import FavoriteBooks

@pytest.mark.unit
@pytest.mark.unit_fav_books
def test_add_book_to_favorites():
    favorites = FavoriteBooks()
    fake_bookstore = Mock()

    book = fake_bookstore.addBook("chaplin", "runaway")

    favorites.add(book)

    assert book in favorites.Favorites


@pytest.mark.unit
@pytest.mark.unit_fav_books
def test_remove_book_from_favorites():
    favorites = FavoriteBooks()
    fake_bookstore = Mock()

    book = fake_bookstore.addBook("chaplin", "runaway")

    favorites.add(book)
    favorites.remove(book)

    assert book not in favorites.Favorites
