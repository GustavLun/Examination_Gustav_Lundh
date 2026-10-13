import pytest

from src.book_store import BookStore
from unittest.mock import Mock



def test_add_book():
    store = BookStore()

    book = store.addBook( "Chaplin", "Runway")


    assert book in store.book_list
    assert book.id == 1
    assert book.title == "Runway"


def test_add_book_id():
    store = BookStore()

    book = store.addBook( "Chaplin", "Runway")
    book2 = store.addBook( "starwars", "flyaway")


    assert book2 in store.book_list
    assert book2.id == 2


def test_togglefavorite_adds_book_to_favorites():
    fake_favorites = Mock()
    fake_favorites.Favorites = [ ]
    store = BookStore(fake_favorites)
    book = store.addBook( "Chaplin", "Runway")

    store.toggle_favorite(book.id)
    fake_favorites.add.assert_called_once_with(book)