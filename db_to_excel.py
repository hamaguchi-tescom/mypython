import sys
import pandas as pd
import sqlite3
from styleframe.style_frame import StyleFrame, Styler


time = sys.argv[1]
db_path = "./doorsingleKD.db"
sql = "SELECT add_time, equipment_name, work_number, recognition_name,temperature_val FROM recognition_record_view order by add_time"

with sqlite3.connect(db_path) as conn:
    df = pd.read_sql(sql, conn)

    # 時間で条件指定
    df = df[df['add_time'].str.contains(time)]
    df.to_excel(f'{time}.xlsx', index=False)

with StyleFrame.ExcelWriter(f'{time}.xlsx') as writer:
    sf = StyleFrame(df)

    # Excelに適用する書式を設定
    style = Styler(bg_color="yellow")

    # ヘッダーの色を設定
    sf.apply_headers_style(style)

    # 列の幅を設定
    sf.set_column_width(['add_time', 'equipment_name', 'work_number',
                         'temperature_val'
                         ], 20)
    sf.set_column_width('recognition_name', 30)

    # Excelファイルを名前を付けて保存
    sf.to_excel(writer, sheet_name=f'{time}.xlsx', index=False)
