import mysql.connector
from mysql.connector import Error
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
history = []
history1 = []

def store_as_history(inp, oup):
    res1 = [inp, oup]
    history.extend(res1)
    history1.append(inp)
    return history


def connect(res,category):
    conn = None

    try:
        conn = mysql.connector.connect(host=config['mysqlDB']['host'],
                                       port=config['mysqlDB']['port'],
                                       database=config['mysqlDB']['database'],
                                       user=config['mysqlDB']['user']
                                       )

        cur = conn.cursor()

        my_sql_insert_query = '''INSERT INTO CALC_HISTORY.history_Cat1(history_id, Input, Output,category) 
                                           VALUES (NOW(), %s, %s, %s) '''

        record = (history1[-1], res, category)
        cur.execute(my_sql_insert_query, record)
        conn.commit()
    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def getdata(typeof):
    try:
        conn = mysql.connector.connect(host=config['mysqlDB']['host'],
                                       port=config['mysqlDB']['port'],
                                       database=config['mysqlDB']['database'],
                                       user=config['mysqlDB']['user']

                                       )
        if conn.is_connected():
            print('Connected to MySQL database')

        cur = conn.cursor(buffered=True)

        query = '''SELECT Input,Output,category
                       FROM CALC_HISTORY.history_Cat1
                       WHERE category ='{0}'
                      ORDER BY history_id DESC
                       limit 3;'''.format(typeof)
        cur.execute(query)
        results = cur.fetchall()

        conn.commit()
    except Error as e:
        print(e)

    return results
