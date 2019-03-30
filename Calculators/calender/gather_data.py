import sqlite3


def connect_db(database_name):
    """connect or create database"""
    conn = sqlite3.connect(database_name)
    return conn


def table_exists(table_name):
    """find all tables form database and if needed table exist then True"""
    c = connect_db("Calender.db")
    c.cursor()
    all_tables = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for tb in all_tables.fetchall():
        for new_tab in range(0, len(tb)):
            if table_name in tb[new_tab]:
                #print(tb[new_tab])
                return True
            else:
                return False
    c.close()


def create_table(table_name):
    """create table but cant change columns"""
    c = connect_db("Calender.db")
    c.cursor()
    c.execute("""CREATE TABLE """ + table_name + """ (
                Insert_date TEXT ,
                Begin_date TEXT  ,
                End_date TEXT ,
                Predict_begin_date TEXT,
                Predict_end_date TEXT
                )""")

    c.commit()
    c.close()


def insert_data(table_name, insert_date, begin_date, end_date, predict_begin, predict_end):
    """insert data to table but cant change columns"""
    c = connect_db("Calender.db")
    c.cursor()
    c.execute("INSERT INTO {} VALUES ('{}', '{}', '{}','{}','{}')"
              .format(table_name, insert_date, begin_date, end_date, predict_begin, predict_end))
    select = c.execute("Select * from " + str(table_name))
    print(select.fetchall())
    c.commit()
    c.close()
