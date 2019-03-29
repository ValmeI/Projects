import sqlite3

conn = sqlite3.connect("Calender.db")


def table_existst(table_name):
    table = c.execute("SELECT * FROM " + str(table_name))
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())
    print(table)
    if len(table):
        return True
    else:
        return False


def create_table(table_name):
    c.execute("""CREATE TABLE""" + table_name + """ (
                Sisestus_kuupäev TEXT,
                Algus_kuupäev TEXT ,
                Lõpp_kuupäev TEXT 
                )""")



c = conn.cursor()
'''
c.execute("""CREATE TABLE Kuupaevad (
            Sisestus_kuupäev TEXT,
            Algus_kuupäev TEXT ,
            Lõpp_kuupäev TEXT 
            )""")'''


table_existst("Kuupaevad")


#c.execute("INSERT INTO Kuupaevad VALUES ('1.1.2019','1.1.2019' , '1.1.2019')")
c.execute("SELECT * FROM Kuupaevad")
print(c.fetchall())



conn.commit()
conn.close()

