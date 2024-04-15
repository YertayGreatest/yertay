import psycopg2, csv
conn = psycopg2.connect(dbname="postgres", host="localhost", user="postgres", password="linktai")
cur = conn.cursor()

#delete number by name

delete_number = """
    UPDATE phonebook SET phone_number = NULL WHERE first_name = %s
"""
name_delete = 'Ferguson'
cur.execute(delete_number, (name_delete,))

#Querying data from tables (filters)
querying_tables = """
    SELECT * FROM phonebook WHERE first_name ILIKE %s
"""
filterval = 'J%'
cur.execute(querying_tables, (filterval,))
rows = cur.fetchall()
for row in rows:
    print(row)
    
#insert from csv file
def read_csv(file_name):
    phonebook_data = []
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            first_name = row[0]
            last_name = row[1]
            phone_number = row[2]
            phonebook_data.append((first_name, last_name, phone_number))
    return phonebook_data

insert_from_csv = """
    INSERT INTO phonebook (first_name, last_name, phone_number) VALUES
    (%s, %s, %s)
"""

#for record in read_csv('lab10/testdata.csv'):
#    cur.execute(insert_from_csv, record)


   
insert_again = """
    INSERT INTO phonebook (first_name, last_name, phone_number) VALUES
    ('Alejandro', 'Orlando', '3489503'),
    ('Mehmet', 'Suvari', '4488493')
"""

def insert_console(conn):
    cur = conn.cursor()
 
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone number: ")
    
    insert_query = '''
        INSERT INTO phonebook (first_name, last_name, phone_number) 
        VALUES (%s, %s, %s)
    '''
    cur.execute(insert_query, (first_name, last_name, phone_number))
    
    
    
    
    conn.commit()
    cur.close()
    

create_tables_phonebook = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        phone_number VARCHAR(50)
        
    )
"""
insert_manually = """
    INSERT INTO phonebook (id, first_name, last_name, phone_number) VALUES
    (1, 'John', 'Doe', '1234567890'),
    (2, 'Michael', 'Smith', '4738392009'),
    (3, 'Alice', 'Johnson', '5556667778');
"""
update = """
    UPDATE phonebook
    SET phone_number = '0000000000'
    WHERE first_name = 'Alice' AND last_name = 'Johnson'
"""

#insert_csv(conn, 'lab10/testdata.csv')

#insert_console(conn) 

#cur.execute()

conn.commit()
cur.close()
conn.close()