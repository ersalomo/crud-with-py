import random as rm
import string
import time


def nanoid(length):
    random_str = ''.join(rm.choice(string.ascii_letters)
                         for i in range(length))
    return random_str


def time_add():
    str_time = time.strftime('%Y-%m-%d %H:%M:%S%z', time.gmtime())
    return str_time


def read_view():
    print('''
    -----------------------
    |    Welcome to Read   |
    ------------------------
    ''')


def template_welcome():
    print("""
            |----------------------|
            | WELCOME EVERYBODY    |
            | DATABASE PERPUTAKAAN | 
            | ---------------------|
        """)


def template_menu(): print("""
        Menu available
        1.Read Data
        2.Create Data
        3.Update Data
        4.Delete Data
        """)
