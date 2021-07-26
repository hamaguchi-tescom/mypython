import sys
import pandas as pd
import sqlite3


time = sys.argv[1]
db_path = "./doorsingleKD.db"
sql = "SELECT add_time, equipment_name, work_number, recognition_name,temperature_val FROM recognition_record_view where add_time like '{}%' order by add_time".format(
    time)

with sqlite3.connect(db_path) as conn:
    df = pd.read_sql(sql, conn)
    df.index = df.index + 1
    df.to_excel(f'{time}.xlsx')
