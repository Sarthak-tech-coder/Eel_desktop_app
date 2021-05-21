from bottle import FapwsServer
import eel
import sqlite3
con = sqlite3.connect('databse.db')
cur = con.cursor() 
table = """
CREATE TABLE IF NOT EXISTS Entries (
id integer PRIMARY KEY autoincrement,
Title text NOT NULL,
Content text NOT NULL,
Price integer NOT NULL)"""
cur.execute(table)       
@eel.expose
def delete(num):
     sql = 'DELETE FROM Entries WHERE id=?'
     cur.execute(sql, (num))
     con.commit()
def init():
        cur.execute(table)
        print('connected')
@eel.expose
def input1(Title, Content, Price):
        query= '''
        INSERT INTO Entries (Title, Content,Price)
        VALUES (?, ?, ?);
        '''
        print('Input query')
        print(str(Title),str( Content), str(Price))
        cur.execute(query, (str(Title), str(Content), str(Price)))
        con.commit()
@eel.expose
def returnall():
    query = []
    for row in cur.execute('SELECT * FROM Entries'):
        print(row)
        query.append(row)
    eel.takeall(query)
eel.init('web')
eel.start('main.html', block=False)
@eel.expose
def quitprogram():
    quit()
    con.close()   
while True:
    eel.sleep(5.0)
