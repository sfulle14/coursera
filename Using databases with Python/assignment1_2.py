import sqlite3

conn = sqlite3.connect('coursera_classes/Using databases with Python/assignment1_2.sqlite')
cur = conn.cursor()

# Drops table if it exists 
cur.execute('DROP TABLE IF EXISTS Counts')

# Creates table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'coursera_classes/Using databases with Python/mbox.txt'   # Grabs a file by default if none are given
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    email_pieces = email.split('@')
    org = email_pieces[1]
    # ? place holder to prevent sql injections to be replaced by (org,)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) 
    # Gets data and puts it in row
    row = cur.fetchone()
    if row is None:
        # Inserts org and sets count value to 1 if this is ther first time the org is seen
        cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?,1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE org = ?',
                    (org,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()