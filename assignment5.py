# program name: assignment5.py
# course: adv application development xls group 18 spring semester 2025 co
# student name: bayden blackwell
# assignment number: assignment 5
# due date: 04/18/2025
# purpose: save temps in a database and show sunday and thursday averages
# resources used: stack overflow, google, youtube, visual studio copilot

import sqlite3

# connect to database
conn = sqlite3.connect('temperature_readings.db')
cur = conn.cursor()

# make table
cur.execute("drop table if exists TemperatureData")
cur.execute("""
create table TemperatureData (
    ID integer primary key autoincrement,
    Day_Of_Week text,
    Temperature_Value real
)
""")

# read file and add to table
with open("Assignment5input.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            day = parts[0]
            try:
                temp = float(parts[1])
                cur.execute("insert into TemperatureData (Day_Of_Week, Temperature_Value) values (?, ?)", (day, temp))
            except:
                pass

conn.commit()

# get sunday avg
cur.execute("select avg(Temperature_Value) from TemperatureData where Day_Of_Week = 'Sunday'")
sunday = cur.fetchone()[0]

# get thursday avg
cur.execute("select avg(Temperature_Value) from TemperatureData where Day_Of_Week = 'Thursday'")
thursday = cur.fetchone()[0]

# print results
print(f"average temperature for sunday: {sunday:.2f}")
print(f"average temperature for thursday: {thursday:.2f}")

# close
conn.close()
