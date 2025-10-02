import psycopg2
import datetime
now = datetime.datetime.now()

def create_table():
    conn = psycopg2.connect (dbname="postgres", user="postgres", password="admin123", host="localhost", port="5433")
    cursor=conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print("Table Created Successfully")

    conn.commit()
    conn.close()

def add_data():
    conn = psycopg2.connect (dbname="postgres", user="postgres", password="admin123", host="localhost", port="5433")
    cursor=conn.cursor()

    name = input ("Enter Name: ")
    id = input ("Enter Id: ")
    age= input ("Enter Age: ")

    query = '''insert into employees(Name,ID,Age) values(%s,%s,%s);'''
    cursor.execute(query,(name, id, age))
    print("Data Added Successfully")

    conn.commit()
    conn.close()

def extract_data():
    conn = psycopg2.connect (dbname="postgres", user="postgres", password="admin123", host="localhost", port="5433")
    cursor=conn.cursor()
    cursor.execute('''select * from employees;''')
    print(cursor.fetchall())

    conn.commit()
    conn.close()

def delete_table():
    conn = psycopg2.connect (dbname="postgres", user="postgres", password="admin123", host="localhost", port="5433")

    cursor=conn.cursor()
    cursor.execute('''DROP TABLE employees;''')
    print("Table deleted successfully")

    conn.commit()
    conn.close()

while 1:
    print(now.strftime("\nCurrent Date and Time: %Y-%m-%d %H:%M:%S"))
    choice = input("Select Choice:\n(1) To create employee table\n(2) To add data into table\n(3) To extract data\n(4) To delete employee table\n(5) To Exit\n")
    if choice == "1":
        try:
            create_table()
        except:
            print("Table already present")
    elif choice == "2":
        add_data()
    
    elif choice == "3":
        extract_data()
    
    elif choice == "4":
        delete_table()

    elif choice == "5":
        break

    else:
        print("Enter valid choice")
    
    