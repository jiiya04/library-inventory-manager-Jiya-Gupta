import json
from pathlib import Path
from library_manager.book import Book

class LibraryInventory:
    def __init__(self, json_path="books.json"):
        self.json_path = Path(json_path)
        self.books = []
        self.load()

    def add_book(self, book):
        # avoid duplicate ISBN
        if self.search_by_isbn(book.isbn):
            return False
        self.books.append(book)
        return True

    def search_by_title(self, title):
        title = title.lower()
        return [b for b in self.books if title in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return self.books

    # ---------- JSON SAVE & LOAD ----------
    def save(self):
        data = [b.to_dict() for b in self.books]
        self.json_path.write_text(json.dumps(data, indent=2))

    def load(self):
        if not self.json_path.exists():
            return
        try:
            data = json.loads(self.json_path.read_text())
            self.books = [
                Book(d["title"], d["author"], d["isbn"], d.get("status", "available"))
                for d in data
            ]
        except:
            # corrupted file → start empty
            self.books = []
