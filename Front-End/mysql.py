from config.__init__ import Config
import pymysql as mysql

# 데이터베이스의 설정값을 지정하는 클래스를 생성한다. Python Dictionary 타입으로 생성한다.

class Config(object):
    DATABASE_CONFIG = {
        'host': 'localhost',
        'db': '10_week',
        'user': 'root',
        'password': 'bagx6g4869!',
        'charset': 'utf8mb4'
    }

# MySQL과의 연결을 생성하고 SQL을 실행하는 클래스를 지정한다.

class MySQL_Database:
    def __init__(self):  # 생성자 함수를 코딩한다. 위에서 지정한 Config 클래스를 이용하여 연결을 생성한다.
        self._conn = mysql.connect(
            host = Config.DATABASE_CONFIG['host'],
            db = Config.DATABASE_CONFIG['db'],
            user = Config.DATABASE_CONFIG['user'],
            password = Config.DATABASE_CONFIG['password'],
            charset = Config.DATABASE_CONFIG['charset']
            )

        self._cursor = self._conn.cursor()
        self._conn.autocommit(True)

    def __enter__(self): # 클래스의 시작에서 호출되는 마법함수를 구현한다.
        sql_drop_table = 'DROP TABLE IF EXISTS family'
        sql_create_table = '''
            CREATE TABLE family (
                EMP_ID VARCHAR(10) NOT NULL,
                EMP_PASSWD VARCHAR(10) NOT NULL,
                EMP_NAME VARCHAR(10) NOT NULL,
                EMP_AGE INT ,
                
                PRIMARY KEY(EMP_ID)
            )
        '''

        self._cursor.execute(sql_drop_table)
        self._cursor.execute(sql_create_table)   

        return self

    def __exit__(self, type, value, traceback): # 클래스의 마지막에서 호출되는 마법함수를 구현한다.
        self._cursor.close()
        self._conn.close()

    def execute(self, sql, params=None): # SQL문을 호출한다.
        self._cursor.execute(sql, params or ())

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()

    def query(self, sql, params=None):
        self._cursor.execute(sql, params or ())
        return self.fetchall()


if __name__ == "__main__":

    # MySQL에 저장될 값을 생성합니다.
    data = [('joseph', 'aaa', '슈퍼맨', 50),('jina', 'bbb', '원더우먼', 45),('julian', 'ccc', '배트맨', 20)]

    with MySQL_Database() as db:
        for i in data:
            db.execute('INSERT INTO family VALUES(%s,%s,%s,%s)', i)  # SQL INSERT 문

        # SQL SELECT 문 #2 
        db.execute('SELECT EMP_ID, EMP_NAME FROM family WHERE EMP_AGE > %s', [40])
        members = db.fetchall()
        print(members)