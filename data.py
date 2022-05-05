import sqlite3

db_path = 'data.db'

# Connect to DB and return Conn and Cur objects
def connect_db(db_path):
    conn = sqlite3.connect(db_path)
    #convert tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

#register new account to DB
def insert_account(account_data):
    conn, cur = connect_db(db_path)
    query = 'INSERT INTO Accounts (SID, email, password) VALUES (?,?,?)'
    values = (account_data['SID'],
              account_data['email'],
              account_data['password'])
    cur.execute(query, values)
    conn.commit()
    conn.close()