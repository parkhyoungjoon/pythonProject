import pymysql
import pandas as pd
conn = pymysql.connect(host='localhost', user='root', password='4665', db='product', charset='utf8')
cur = conn.cursor()

csv_data = pd.read_csv('Korean_CPI_by_City_2019-2023.csv')

cpi_year = list(csv_data[csv_data.columns[0]])
cpi_city = list(csv_data[csv_data.columns[1]])
cpi_city_r = []
cpi_data = list(csv_data[csv_data.columns[2]])
grdp_data = list(csv_data[csv_data.columns[3]])
city_list = ['Seoul','Busan','Daegu','Incheon','Gwangju','Daejeon','Ulsan','Sejong']
for ci in cpi_city:
    cpi_city_r.append((city_list.index(ci)+1))
for i in range(len(cpi_city_r)):
    sql = 'insert into cpi_tb(city_id,data,GRDP,year) values(%s,%s,%s,%s)'
    cur.execute(sql,(cpi_city_r[i],cpi_data[i],grdp_data[i],cpi_year[i]))
conn.commit()
cur.close()
conn.close()