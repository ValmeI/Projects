import sqlite3


def connect_db(database_name):
    conn = sqlite3.connect(database_name)
    return conn


def table_exists(table_name):
    c = connect_db("Calender.db")
    c.cursor()
    all_tables = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #print(all_tables.fetchall())
    for tb in all_tables.fetchall():
        for new_tab in range(0, len(tb)):
            if table_name in tb[new_tab]:
                #print(tb[new_tab])
                return True
            else:
                return False
    c.close()


def create_table(table_name):
    c = connect_db("Calender.db")
    c.cursor()
    c.execute("""CREATE TABLE """ + table_name + """ (
                Sisestus_kuupäev TEXT ,
                Algus_kuupäev TEXT  ,
                Lõpp_kuupäev TEXT  
                )""")

    c.commit()
    c.close()


def insert_data(insert_date, begin_date, end_date, table_name):
    c = connect_db("Calender.db")
    c.cursor()
    #print(insert_date, begin_date, end_date, table_name)
    c.execute("INSERT INTO " + str(table_name) +
              " VALUES (" + "'" + str(insert_date) + "'" + ", " +
              "'" + str(begin_date) + "'" + ", " +
              "'" + str(end_date) + "'" +
              ")")
    select = c.execute("Select * from " + str(table_name))
    print(select.fetchall())
    c.commit()
    c.close()
