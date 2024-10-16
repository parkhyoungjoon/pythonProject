import pymysql
import pandas as pd
conn = pymysql.connect(host='localhost', user='root', password='4665', db='product', charset='utf8')
cur = conn.cursor()

sql = '''select * from product_price_tb
'''
cur.execute(sql)
cur.fetchall()
print(cur)
for c in cur:
    print(c)