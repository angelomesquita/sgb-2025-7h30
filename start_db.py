from model.author_dao import AuthorDao

if __name__ == '__main__':
    AuthorDao.create_table()
    print('Author table created successfully.')
