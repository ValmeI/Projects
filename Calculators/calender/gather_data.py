import sqlite3
from datetime import timedelta
from dateutil.parser import parse


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
                # print(tb[new_tab])
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


def get_data_from_table(db, table, column1, column2):
    c = connect_db(db)
    c.cursor()
    select_column = c.execute("SELECT {}, {} FROM {}".format(column1, column2, table))
    #print(select_column.fetchall())
    column_list = []
    for col in select_column:
        for x in range(0, len(col)):
            column_list.append(col[x])
    c.close()
    return column_list


def create_fictitious_dates(right_list):
    add_1_day = timedelta(days=0)
    add_2_day = timedelta(days=20)
    high_y = 5
    low_y = 2
    nr = 1
    fictitious_dates_list = []
    fictitious_values_list = []

    for x in right_list:
        #print(parse(x), nr, nr%2)
        nr += 1
        if nr % 2 == 1:
            fictitious_dates_list.append(parse(x))
            new_fictitious_date = parse(x) + add_1_day
            fictitious_dates_list.append(new_fictitious_date)
            fictitious_dates_list.append(new_fictitious_date + add_2_day)

            fictitious_values_list.append(high_y)
            fictitious_values_list.append(low_y)
            fictitious_values_list.append(low_y)

            '''print(parse(x), high_y)
            print(new_fictitious_date, low_y)
            print(new_fictitious_date + add_n_day, low_y)'''
        else:
            fictitious_dates_list.append(parse(x))
            fictitious_values_list.append(high_y)

            '''print(parse(x), high_y)'''

    return fictitious_dates_list, fictitious_values_list


#test = create_fictitious_dates(get_data_from_table("Calender.db", "Kuupaevad", "Begin_date", "End_date"))
#print(test[0])

print(get_data_from_table("Calender.db", "Kuupaevad", "Begin_date", "End_date"))
print(get_data_from_table("Calender.db", "Kuupaevad", "Predict_begin_date", "Predict_end_date"))

'''
[('2018-09-01', '2018-09-08'), 
('2018-09-29', '2018-10-06'), 
('2018-10-27', '2018-11-03'), 
('2018-11-24', '2018-12-01')]
'''
