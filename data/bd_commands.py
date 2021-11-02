import sqlite3


class bd_work:
    def __init__(self):
        self.connect = sqlite3.connect('data/users.bd')
        self.cursor = self.connect.cursor()

    def get_rooted_user(self):
        self.cursor.execute("SELECT id FROM login_id")
        return (",".join([str(s) for s in list(self.cursor.fetchall())])).replace(',', '').replace('(', ' '). \
            replace(')', '').replace(' ', '', 1).split()

    def create(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(id INTEGER)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS banned_id(id INTEGER)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS admin_id(id INTEGER)""")
        self.connect.commit()

    def find(self, users_id):
        self.cursor.execute(f"SELECT id FROM login_id WHERE id = {users_id}")
        return self.cursor.fetchall()

    def add(self, users_id):
        self.cursor.execute("INSERT INTO login_id VALUES(?);", users_id)
        self.connect.commit()

    def add_banlist(self, users_id):
        self.cursor.execute("INSERT INTO banned_id VALUES(?);", users_id)
        self.connect.commit()

    def add_administrator(self, users_id):
        self.cursor.execute("INSERT INTO admin_id VALUES(?);", users_id)
        self.connect.commit()

    def delete_banlist(self, users_id):
        self.cursor.execute(f"DELETE FROM banned_id WHERE id = {users_id}")
        self.connect.commit()

    def delete_administrator(self, user_id):
        self.cursor.execute(f"DELETE FROM admin_id WHERE id = {user_id}")
        self.connect.commit()

    def banlist(self):
        self.cursor.execute(f"SELECT id FROM banned_id")
        return (",".join([str(s) for s in list(self.cursor.fetchall())])).replace(',', '').replace('(', ' '). \
            replace(')', '').replace(' ', '', 1).split()

    def admins(self):
        self.cursor.execute(f"SELECT id FROM admin_id")
        return (",".join([str(s) for s in list(self.cursor.fetchall())])).replace(',', '').replace('(', ' '). \
            replace(')', '').replace(' ', '', 1).split()

    def printInfo(self, array, type):
        if not array:
            return type + '\n' + 'список пуст'
        else:
            line = type + '\n'
            for i in range(len(array)):
                line = line + '[user ' + str(i+1) + '] ' + array[i] + '\n'
            return line;

