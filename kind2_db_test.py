# coding: utf-8

import sqlite3

db_path = "C:\ProgramData\ArcSoftDoorSingle\doorsingleKD.db"
conn = sqlite3.connect(db_path)

print("データベースに接続しました。")

# sql = "SELECT * FROM recognition_record WHERE STRFTIME('%Y-%m-%d', add_time) = STRFTIME('%Y-%m-%d', 'NOW')"
sql = "SELECT add_time, work_number, recognition_name,temperature_val FROM recognition_record_view WHERE STRFTIME('%Y-%m-%d', add_time) = '2021-07-14' and work_number = '0001'"
for row in conn.execute(sql):
	print(row)
	print(type(row))

conn.close()

