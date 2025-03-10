import sqlite3
from datetime import datetime
from random import randint
from time import sleep

def log_kitchen_dht11():
    while True:
        query = """INSERT INTO kitchen (datetime, temperature, humidity) VALUES(?, ?, ?)"""
        now = datetime.now()
        now = now.strftime("%d/%m/%y %H:%M:%S")
        data = (now, randint(0, 30), randint(0, 100))

        try:
            conn = sqlite3.connect("database/sensor_data.db")
            cur = conn.cursor()
            cur.execute(query, data)
            conn.commit()
        except sqlite3.Error as sql_e:
            print(f"sqlite error occured: {sql_e}")
            conn.rollback()
        except Exception as e:
            print(f"Error occured: {e}")
        finally:
            conn.close
        sleep(1)

log_kitchen_dht11()