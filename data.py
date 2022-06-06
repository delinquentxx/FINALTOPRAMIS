import sqlite3

db_path = 'flipp.db'

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


#create announcement
def insert_announcement(announcement_data):
    conn, cur = connect_db(db_path)
    query = 'INSERT INTO Announcement (date, committee, message) VALUES (?,?,?)'
    values = (announcement_data['date'],
              announcement_data['committee'],
              announcement_data['message'])
    cur.execute(query, values)
    conn.commit()
    conn.close()


#delete announcement through announcement id
def process_deleting_announcement(announcement_id):
    conn, cur = connect_db(db_path)
    query = 'DELETE FROM Announcement WHERE id=?'
    cur.execute(query, announcement_id)
    conn.commit()
    conn.close()