from model.author_dao import AuthorDao
from controller.author_controller import AuthorController

if __name__ == '__main__':
    AuthorDao.create_table()

    controller = AuthorController()

    controller.register(author_id=100, name="George Orwell")
    controller.list()

    controller.update(100, name="G. Orwell")
    controller.list()

    controller.delete(100)
    controller.list()

    controller.restore(100)
    controller.list()

    AuthorDao.truncate()
