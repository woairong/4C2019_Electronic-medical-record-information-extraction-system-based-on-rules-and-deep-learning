# coding: utf8
import sqlite3
import hashlib
from dataHandler import csv_handler
import sql
def md5Sum(pword):
    return hashlib.md5(pword.encode()).hexdigest()

class DbHandler:
    def __init__(self, db):
        self.connect_db(db)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_db()

    def connect_db(self, db):
        self.conn = sqlite3.connect(db, isolation_level=None)
        self.conn.create_function("md5", 1, md5Sum)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def close_db(self):
        #self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)

    def get_all_records(self):
        return self.cursor.fetchall()

    def get_one_record(self):
        return self.cursor.fetchone()
  
  
def create_users_table():
    with DbHandler(sql.DB_NAME) as db:
        db.execute_sql( sql.CREATE_USERS_TABLE_SQL )
        #db.execute_sql( SEARCH_ROOT_SQL )
        #if not db.get_one_record():
        db.execute_sql(sql.INSERT_USER_SQL.format('root', md5Sum('root123'), 'users'))
    

def import_data_to_table(tableName, csvfile):
    with DbHandler(sql.DB_NAME) as db:
        isFirstLine = True
        execute_sql = db.execute_sql
        execute_sql(sql.SEARCH_ROOT_PWORD_SQL)
        rootPword = tuple(db.get_one_record())[0]
        # update the new table to 'users' table.
        execute_sql(sql.INSERT_USER_SQL.format('root', rootPword, tableName))
        for row in csv_handler(csvfile):
            if isFirstLine:		# we suppose the first line as table fields.
                execute_sql( sql.CREATE_TABLE_SQL %(tableName, "','".join(row)))
                insert_sql = sql.INSERT_DATA_SQL.format(tableName, ",".join(row))
                isFirstLine = False
                continue
            execute_sql(insert_sql %("','".join(row)))
            
def output_data_to_csv(tableName):
    with DbHandler(sql.DB_NAME) as db:
        isFirstLine = True
        execute_sql = db.execute_sql
    
        
