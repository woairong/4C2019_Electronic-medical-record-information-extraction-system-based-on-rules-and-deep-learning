# coding: utf8
import os.path
from views import app as webdb
from dbHandler import create_users_table
from sql import DB_NAME
import sys
sys.path.append(r"./ComputerContest_BigData_EMR")
import matplotlib as mtp
mtp.use("Agg")

def init_env():
    webdb.secret_key = 'chEb0a69cf(b19e6f282d501,g8b'
    if not os.path.exists(DB_NAME):
        create_users_table()


if __name__ == '__main__':
    init_env()
    webdb.run(debug=True, host='0.0.0.0')
    '''import logging
    logging.basicConfig(filename='error.log',
                        format='%(asctime)s %(message)s',
                        level=logging.WARNING)
    while True:
        try:
            webdb.run(host='0.0.0.0')
        except Exception as e:
            logging.warning(e)
    '''