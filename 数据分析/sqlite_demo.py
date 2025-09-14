import sqlite3


class OperateSqlite:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self, ):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        pass

    def insert(self):
        pass


if __name__ == '__main__':
    operator = OperateSqlite("test_db.db")
    operator.connect()
    
