#!/usr/local/bin/python
from __future__ import print_function
from contextlib import contextmanager
import argparse
import string
import random
import threading

import pymysql as db


DB_NAME = 'test_insert_data_db'
TABLE_NAME = 'test_insert_data_table'
CREATE_TABLE_STATEMENT = """create table {0} (id int(10) NOT NULL AUTO_INCREMENT, name varchar(255) NOT NULL,datetime double NOT NULL, PRIMARY KEY (`id`))""".format(TABLE_NAME)


def _argparse():
    parser = argparse.ArgumentParser(description='health checker for MySQL database')
    parser.add_argument('--host', action='store', dest='host', required=True, help='connect to host')
    parser.add_argument('--user', action='store', dest='user', required=True, help='user for login')
    parser.add_argument('--password', action='store', dest='password', required=True, help='password to use when connecting to server')
    parser.add_argument('--port', action='store', dest='port', default=3306, type=int, help='port number to use for connection or 3306 for default')
    parser.add_argument('--row_size', action='store', dest='row_size', default=5000, type=int, help='how much rows')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--thread_size', action='store', dest='thread_size', default=1, type=int, help='how much thread')
    return parser.parse_args()


@contextmanager
def get_conn(**kwargs):
    conn=db.connect(host=kwargs.get('host', 'localhost'),user=kwargs.get('user'),passwd=kwargs.get('passwd'),port=kwargs.get('port', 3306))
    try:
        yield conn
    
    finally:
        conn.close()



def create_and_create_table(conn):
    with conn as cur:
        for sql in ["drop database if exists {0}".format(DB_NAME),"create database {0}".format(DB_NAME),"use {0}".format(DB_NAME),CREATE_TABLE_STATEMENT]:
            print(sql)
            cur.execute(sql)

def add_data(cur):
    source=string.ascii_letters
    NAME="".join(random.sample(source,10))
    insert_sql="insert into {0} (name,datetime) values('{1}',current_timestamp())".format(TABLE_NAME,NAME)
    cur.execute(insert_sql)
   
 
def insert_data(conn_args,rows):
    with get_conn(**conn_args) as conn:
        with conn as cur:
            cur.execute("use test_insert_data_db")
            for i in range(rows):
                add_data(cur)
                if i % 10000 ==0:
                    conn.commit()


def main():
    parser = _argparse()
    rows = parser.row_size
    thread_size = parser.thread_size
    conn_args=dict(host=parser.host, user=parser.user, passwd=parser.password, port=parser.port)
    with get_conn(**conn_args) as conn:
        create_and_create_table(conn)

    threads=[] 
    for i in range(thread_size):
        t=threading.Thread(target=insert_data,args=(conn_args,rows))
        threads.append(t)
        t.start()
    
    for  t in threads:
        t.join()

if __name__ == '__main__':
    main()
