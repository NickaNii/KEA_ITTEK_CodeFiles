import sqlite3
from datetime import datetime
from random import randint
from time import sleep


def get_kitchen_data(number_of_rows):
        query = """SELECT * FROM kitchen ORDER BY datetime;"""
        datetime = []
        temperature = []
        humidity = []

        try:
            conn = sqlite3.connect("database/sensor_data.db")
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchmany(number_of_rows)
            for row in rows:
                 datetime.append(row[0])
                 temperature.append(row[1])
                 humidity.append(row[2])
            return datetime, temperature, humidity
        
        except sqlite3.Error as sql_e:
            print(f"sqlite error occured: {sql_e}")
            conn.rollback()
        except Exception as e:
            print(f"Error occured: {e}")
        finally:
            conn.close

get_kitchen_data(10)