import psycopg2
conn = psycopg2.connect(dbname='postgres', host='localhost', user='postgres', password='linktai')
cur = conn.cursor()
#1
def search_pattern(pattern):
    query = """
        SELECT * FROM phonebook WHERE first_name ILIKE %s or last_name ILIKE %s or phone_number ILIKE %s;
    """
    cur.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
#search_pattern('Del')

#2
def procedure_insert(user, phone):
    cur.execute("SELECT COUNT(*) AS count FROM phonebook WHERE first_name = %s", (user,))
    result = cur.fetchone()
    count = result[0]
    if count >0:
        cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (phone, user))   
        print(f'user {user} updated with number {phone}')
    else:
        cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (user, phone) )
        print(f'user {user} was added with number {phone}')       
    conn.commit()
#procedure_insert("Ahmed", "12398932")

#3 
def insert_many(user_list):
    incorrect = []
    for user, surname, phone in user_list:
        if len(phone) == 10 and phone.isdigit():
            cur.execute("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s,%s)", (user, surname, phone))
            print(f'user {user}, {surname} was added with number {phone}')
        else:
            incorrect.append((user, surname, phone))
    conn.commit()
    return incorrect
#user_list = [('asohho', 'asdds', '23234'), ('asdasdq', 'asdqqqq', '1234567890')]
#print(insert_many(user_list))

#4
def pagination(table, limit, offset):
    query = "SELECT * FROM phonebook LIMIT %s OFFSET %s;"
    cur.execute(query, (limit, offset))
    results = cur.fetchall()
    for row in results:
        print(row)
pagination('phonebook', limit=5, offset=1)

#5
def delete_byname(value):
    if value.isdigit():
        query = "SELECT id FROM phonebook WHERE phone_number=%s"
    else:
        query = "SELECT id FROM phonebook WHERE first_name=%s OR last_name=%s"
    cur.execute(query, (value, value))
    result = cur.fetchone()
    if result:
        entry_id = result[0]
        delete_q = "DELETE FROM phonebook WHERE id = %s"
        cur.execute(delete_q, (entry_id,))
        conn.commit()
        print('Entry deleted successfully')
    else:
        print('Entry not found')
delete_byname("Pammy")
delete_byname('15')