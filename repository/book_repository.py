from typing import List, Optional
from model.book import Book
from model.book_dao import BookDao


class BookRepository:

    @staticmethod
    def get_all_books() -> List[Book]:
        return BookDao.load_all()

    @staticmethod
    def search(
        title: Optional[str] = None,
        author: Optional[str] = None,
        available: Optional[bool] = None
    ) -> List[Book]:
        """Search books applying optional filters"""
        results = BookRepository.get_all_books()

        if title:
            results = [b for b in results if title.lower() in b.title.lower()]

        if author:
            results = [b for b in results if author.lower() in b.author.name.lower()]

        if available is not None:
            if available:
                results = [b for b in results if b.quantity > 0]
            else:
                results = [b for b in results if b.quantity <= 0]

        return results
