import sqlite3

# connect to the sqlite database
db = sqlite3.connect("data/student_db")
cursor = db.cursor()

# Create the pyton_programing table
#cursor.execute('''
      #CREATE TABLE python_programming (id INTEGER PRIMARY KEY, name TEXT,
              #grade INTEGER)

# Insert the following rows into the Python_Programming table 
rows_to_insert = [
      (55, 'Carl Davis', 61),
      (66, 'Dennis Fedrickson', 88),
      (77, 'Jane Richards', 78),
      (12, 'Peyton Sawyer', 45),
      (2, 'Lucas Brooke', 99)
]

cursor.executemany("INSERT INTO python_programming VALUES(?, ?, ?)", row_to_insert)

# Commit the inserted rows
db.commit()

# Select all records from 60 and 80
cursor.execute("SELECT *  FROM python_programming WHERE grade BETWEEN 60 AND 80")
print("Records with grade between 60 and 80")
print(cursor.fetchall())

# Change Carls grade to 65
cursor.execute("UPDATE Python_programming SET grade = 65 WHERE name = 'Carl Davis' ")

# Delete Dennis fedrickson row
cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Federickson' ")

# Change the grade of all student with an id greater than 55 to a grade of 80
cursor.execute("UPDATE python_programming SET grade = 80 WHERE id = 55")

# Commit change
db.commit()

# Close cursor
cursor.close()

# Close cursor
db.close()



