
class FavoriteBooks:
    def __init__(self):
        self.Favorites = []

    def add(self,book):
            if book not in self.Favorites:
                self.Favorites.append(book)


    def remove(self,book):
            if book in self.Favorites:
             self.Favorites.remove(book)