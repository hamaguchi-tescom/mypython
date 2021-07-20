# coding: utf-8
# import csv
import sys
import sqlite3
from openpyxl import Workbook
from openpyxl.styles import numbers, PatternFill
from openpyxl.utils import get_column_letter


db_path = "./doorsingleKD.db"
time = sys.argv[1]

conn = sqlite3.connect(db_path)
# sql = "SELECT * FROM recognition_record WHERE STRFTIME('%Y-%m-%d', add_time) = STRFTIME('%Y-%m-%d', 'NOW')"
sql = "SELECT add_time, equipment_name, work_number, recognition_name,temperature_val FROM recognition_record_view where add_time like ? order by add_time"

# 書き込み用ファイルを作成
FILL_TITLE = PatternFill(patternType='solid', fgColor='B0E0E6')
wb = Workbook()
ws = wb.active
y = 1
ws.cell(row=y, column=1).value = "add_time"
ws.cell(row=y, column=2).value = "equipment_name"
ws.cell(row=y, column=3).value = "work_number"
ws.cell(row=y, column=4).value = "recognition_name"
ws.cell(row=y, column=5).value = "temperature_val"

for rows in ws['A1':'E1']:
    for cell in rows:
        cell.fill = FILL_TITLE
        value_len = len(str(cell.value)) * 2
        ws.column_dimensions[get_column_letter(cell.column)].width = value_len
        print(value_len)
# ws.column_dimensions['A'].width = 20
# ws.row_dimensions[1].height = 50
for row in conn.execute(sql, (time+'%',)):
    y += 1
    ws.cell(row=y, column=1).value = row[0]
    ws.cell(row=y, column=2).value = row[1]
    ws.cell(row=y, column=3).value = row[2]
    ws.cell(row=y, column=4).value = row[3]
    ws.cell(row=y, column=5).value = row[4]

    wb.save(f'{time}.xlsx')

    # with open(f'{time}.csv', 'a', newline='', encoding='utf_8_sig') as csvfile:
    # c = csv.writer(csvfile, delimiter=',')
    # c.writerow(['add_time', 'equipment_name', 'work_number',
    #             'recognition_name', 'temperature_val'])
    # for row in conn.execute(sql, (time+'%',)):
    #     print(row)
    #     c.writerow(row)
