from dbclass_login import DatabasesLogin


class ManageLogin(DatabasesLogin):
    def login_db(self, input_id, input_pw):
        sql = (f"select * from public.login\
                where id = '{input_id}' and pw = '{input_pw}';")
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()

        except Exception as e:
            result = ('err', e)

        return result

    def change_db_id(self, input_id):
        sql = f"update public.login set id = '{input_id}';"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            return 'err', e

    def change_db_pw(self, input_pw):
        sql = f"update public.login set pw = '{input_pw}';"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            return 'err', e

    def get_login_info(self):
        sql = f"select * from public.login;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0]


if __name__ == "__main__":
    # for test
    lgn_db = ManageLogin()
    s = int(input('> '))

    if s == 1:
        id_db, pw_db = lgn_db.get_login_info()
        print(f'id: {id_db}, pw: {pw_db}')
    elif s == 2:
        n_i = input('> ')
        lgn_db.change_id(n_i)
    else:
        n_p = input('> ')
        lgn_db.change_pw(n_p)
