from dbclass_main import Databases
# try: except has been abandoned


class ManageBook(Databases):
    def insert_db(self, *data):
        data = tuple(data) + ('대출 가능',)
        sql = f"insert into public.haegal_bookshelf values {data};"

        self.cursor.execute(sql)
        self.db.commit()

    def read_db(self, data):
        sql = (f"select location, name, number, rent from public.haegal_bookshelf\
                where name like '{data}' or byname like '{data}'\
                order by location, name, number;")

        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        new_result = []
        for book in result:
            db_loc, db_name, db_num, db_rent = book
            if db_num.is_integer():
                new_result.append((db_loc, db_name, int(db_num), db_rent))
            else:
                new_result.append(book)

        return new_result

    def is_same_db(self, db_name, db_num, db_type, db_lang):
        sql = (f"select name, number, type, language from public.haegal_bookshelf\
                where (name like '{db_name}' or byname like '{db_name}') \
                and number = {db_num} and type = '{db_type}' and language = '{db_lang}'\
                order by location, name, number;")

        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result

    def update_db(self, db_col, data, db_name, db_num):
        sql = (f"update public.haegal_bookshelf set {db_col} = '{data}'\
                where name = '{db_name}' and number = {db_num};")

        self.cursor.execute(sql)
        self.db.commit()

    def delete_db(self, db_name, db_num):
        sql = f'delete from public.haegal_bookshelf where name = {db_name} and number = {db_num};'

        self.cursor.execute(sql)
        self.db.commit()

    def get_all(self, schema, table, column):
        sql = (f"select {column} from {schema}.{table}\
                order by location, name, number;")

        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        new_result = []
        for book in result:
            area, book_name, num, b_types, byname, b_lang, rent = book
            if num.is_integer():
                num = int(num)
                book = (area, book_name, num, b_types, byname, b_lang, rent)
            new_result.append(book)

        return new_result

    def get_location(self, data):
        if data[-1] == '%':
            where = f"location like '{data}'"
        else:
            where = f"location = '{data}'"

        sql = (f"select location, name, number, rent from public.haegal_bookshelf\
                 where {where} order by location, name, number;")

        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        new_result = []
        for book in result:
            area, book_name, num, rent = book
            if num.is_integer():
                new_result.append((area, book_name, int(num), rent))
            else:
                new_result.append(book)

        return new_result


if __name__ == "__main__":
    # for test
    db = ManageBook()
    db_schema, db_table = 'public', 'haegal_bookshelf'

    print('=' * 38)
    flag = int(input('\t1. 입력\t2. 삭제\t3. 조회\t4. 변경\n' + '='*38 + '\n\t 어떤 명령을 입력하시겠습니까? > '))

    if flag == 1:
        location = input('책장 위치 > ')
        name = input('도서명 > ')
        number = int(input('도서 권수 > '))
        book_type = input('도서 타입(만화/소설/작법서) > ')
        by_name = input('축약어 > ')
        langauge = input('도서 언어 > ')

        db.insert_db(location, name, number, book_type, by_name, langauge)

    elif flag == 2:
        name = input('도서명 > ')
        number = int(input('도서 권수 > '))
        db.delete_db(db_schema, db_table, f"name = '{name}' and number = {number}")

    elif flag == 3:
        name = input('도서명 > ')
        name = f'%{name}%'
        print(db.read_db(name))

    elif flag == 4:
        db_id = input('ID > ')
        db_pw = input('PW > ')

        if db_id == 'haegal' and db_pw == 'inuitoko':
            pass
        else:
            print('신원이 확인되지 않아 변경이 불가합니다.')

    elif flag == 5:
        all_book = db.get_all(db_schema, db_table, '*')
        print(all_book)

    elif flag == 6:
        col = 'name, number, type, language'
        name = input()
        number = int(input())
        types = input()
        lang = input()
        print(db.is_same_db(name, number, types, lang))

    else:
        print('입력에 실패했습니다.')

    # db.read_db(db_schema, db_table, 'location, name')
    # db.insert_db('public', 'haegal_bookshelf', ("A-1", "test", 1, "test", "aaa", "jpn"))
    # db.delete_db('public', 'haegal_bookshelf', "name = 'test'")
