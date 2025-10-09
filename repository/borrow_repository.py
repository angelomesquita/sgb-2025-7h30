from typing import List

from model.borrow import Borrow
from model.borrow_dao import BorrowDao
from model.exceptions import BorrowNotFoundError


class BorrowRepository:

    @staticmethod
    def get_all_borrows() -> List[Borrow]:
        return BorrowDao.load_all()

    @staticmethod
    def get_borrow_by_id(borrow_id: str) -> Borrow:
        borrows = BorrowRepository.get_all_borrows()
        borrow = next((b for b in borrows if str(b.borrow_id) == borrow_id), None)
        if borrow is None:
            raise BorrowNotFoundError(f"Borrow with id {borrow_id} not found.")
        return borrow
