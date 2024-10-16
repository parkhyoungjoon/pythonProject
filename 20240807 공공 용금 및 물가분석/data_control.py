import pymysql
import pandas as pd
import csv
import numpy as np
conn = pymysql.connect(host='localhost', user='root', password='4665', db='product', charset='utf8')
cur = conn.cursor()

def isert_p_name(category_name, product_name):
    sql = 'select category_id from product_category_tb where category_name = %s'
    cur.execute(sql, category_name)
    cd = cur.fetchone()
    sql = 'insert into product_name_tb(category_id,product_name) values(%s, %s)'
    cur.execute(sql,(cd,product_name))
    conn.commit()
    print('입력완료')

def isert_p_category(type,d):
    sql = 'insert into product_category_tb(type_id,category_name) values(%s, %s)'
    cur.execute(sql,(type,d))

def isert_p_price(d,val,year):
    idx = 1
    for v in val:
        sql = 'insert into product_price_tb(product_id,city_id,product_price,year) values(%s, %s, %s, %s)'
        cur.execute(sql,(d,idx,v,year))
        idx +=1
    conn.commit()


def product_name_insert_list(data):
    for d in range(len(data[0])):
        sql = 'select product_id from product_name_tb where product_name = %s'
        cur.execute(sql, data[1][d])
        cd = cur.fetchone()
        if cd == None :
            isert_p_name(data[0][d],data[1][d])
    conn.commit()
    print('입력완료')

def category_name_insert_list(type, data):
    for d in data:
        sql = 'select category_id from product_category_tb where category_name = %s'
        cur.execute(sql, d)
        cd = cur.fetchone()
        if cd == None :
            isert_p_category(type,d)
    conn.commit()
    print('입력완료')

def data_isert(link,year,type):
    data = pd.read_excel(link)
    data = data.fillna(0)
    product_name_list = [data[data.columns[3]].to_list(),data[data.columns[4]].to_list()]
    product_price_city_dict = {}
    for idx, val in enumerate(product_name_list[1]):
        product_price_city_dict[val] = data.loc[idx][data.columns[9:16]].tolist()
    category_name_insert_list(type,product_name_list[0])
    product_name_insert_list(product_name_list)
    for idx,val in product_price_city_dict.items():
        sql = 'select product_id from product_name_tb where product_name = %s'
        cur.execute(sql,idx)
        d = cur.fetchone()
        if d == None :
            isert_p_name(type,idx)
            sql = 'select product_id from product_name_tb where product_name = %s'
            cur.execute(sql,idx)
            d = cur.fetchone()
        isert_p_price(d,val,year)

data_isert('생필품지역별_동향[전체2019년]87-5시40분.xls',2019,'A')
data_isert('생필품지역별_동향[전체2020년]87-5시35분.xls',2020,'A')
data_isert('생필품지역별_동향[전체2021년]87-5시1분.xls',2021,'A')
data_isert('생필품지역별_동향[전체2022년]87-4시59분.xls',2022,'A')
data_isert('생필품지역별_동향[전체2023년]87-2시35분.xls',2023,'A')


cur.close()
conn.close()
