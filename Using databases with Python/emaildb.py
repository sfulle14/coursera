import sqlite3

conn = sqlite3.connect('coursera_classes/Using databases with Python/emaildb.sqlite')
cur = conn.cursor()

# Drops table if it exists 
cur.execute('DROP TABLE IF EXISTS Counts')

# Creates table
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'coursera_classes/Using databases with Python/mbox-short.txt'   # Grabs a file by default if none are given
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split('@')
    email = pieces[1]
    # ? place holder to prevent sql injections to be replaced by (email,)
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) 
    # Gets data and puts it in row
    row = cur.fetchone()
    if row is None:
        # Inserts email and sets count value to 1 if this is ther first time the email is seen
        cur.execute('''INSERT INTO Counts (email, count)
                    VALUES (?,1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE email = ?',
                    (email,))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()