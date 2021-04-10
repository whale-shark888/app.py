# -*- coding: utf-8 -*-
import pymysql
# 鏈接database  執行sql語句 關閉數據庫鏈接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',
                       charset='utf8', database='app')
print(conn.get_server_info())

# 1 實例化一個游標對象 2 定義sql語句 3 通過游標執行 4 處理執行結果
cursor = conn.cursor()
sql = 'select * from info'
cursor.execute(sql)
result = cursor.fetchall()
print(result)

# cursor.execute(sql) 執行
# conn.commit() submit
cursor.close()