import sqlite3
# Import SQLite3 extension
try:
    conn = sqlite3.connect(database="people.db")
    print("it works")
# PEP249??? I guess, I'll look this up later (I thought it was supposed to be PEP8 lmfao)

except sqlite3.OperationalError as oe:
    print(f"connection could not be processed : { oe }")
except:
    print("this doesnt work for some reason lol")