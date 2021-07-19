# coding: utf-8
import csv
import sys
import sqlite3

db_path = "C:\ProgramData\ArcSoftDoorSingle\doorsingleKD.db"
time = sys.argv[1]

conn = sqlite3.connect(db_path)
# print("データベースに接続しました。")
# sql = "SELECT * FROM recognition_record WHERE STRFTIME('%Y-%m-%d', add_time) = STRFTIME('%Y-%m-%d', 'NOW')"
sql = "SELECT add_time, work_number, recognition_name,temperature_val FROM recognition_record_view where add_time like ?"
for row in conn.execute(sql,(time+'%',)):
		print(row)
		
	
conn.close()