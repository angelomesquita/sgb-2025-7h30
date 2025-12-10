from model.author_dao import AuthorDao
from model.book_dao import BookDao
from model.publisher_dao import PublisherDao

if __name__ == '__main__':
    AuthorDao.create_table()
    print('Author table created successfully.')

    PublisherDao.create_table()
    print('Publisher table created successfully.')

    BookDao.create_table()
    print('Book table created successfully.')
