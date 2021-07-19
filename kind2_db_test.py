# coding: utf-8
import csv
import sys
import sqlite3

db_path = "./doorsingleKD.db"
time = sys.argv[1]

conn = sqlite3.connect(db_path)
# print("データベースに接続しました。")
# sql = "SELECT * FROM recognition_record WHERE STRFTIME('%Y-%m-%d', add_time) = STRFTIME('%Y-%m-%d', 'NOW')"
sql = "SELECT add_time, equipment_name, work_number, recognition_name,temperature_val FROM recognition_record_view where add_time like ?"
with open(f'{time}.csv', 'a', newline='', encoding='utf_8_sig') as csvfile:
    c = csv.writer(csvfile, delimiter=',')
    c.writerow(['add_time', 'equipment_name', 'work_number',
                'recognition_name', 'temperature_val'])
    for row in conn.execute(sql, (time+'%',)):
        print(row)
        c.writerow(row)

conn.close()
