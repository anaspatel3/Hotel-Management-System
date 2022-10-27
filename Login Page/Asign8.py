import sqlite3
db=sqlite3.connect('Anas.db')
query = "insert into Anas_272(StudentID, StudentFirstName, StudentLastName, City) values(0828272,'Anas','Patel','Scarborough');"
try:
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    print("Record added successfully")
except:
    print("ERROR")
    db.rollback()

db.close()