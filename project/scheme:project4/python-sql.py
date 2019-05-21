import sqlite3
db = sqlite3.Connection("n.db")  # connect  create a file in the current path
db.execute("CREATE TABLE nums AS SELECT 2 UNION SELECT 3;")
# the second argument fill the "?"
db.execute("INSERT INTO nums VALUES (?),(?),(?);", range(4, 7))
# fetchall select all rows as a list
print(db.execute("SELECT * FROM nums;").fetchall())
db.commit()  # save change to the file
# 也可以用for row in a.execute(select * from xxxxx) 来iterate
