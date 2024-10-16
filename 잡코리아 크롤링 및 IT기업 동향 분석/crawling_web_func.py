import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import os
import csv
# 채용 정보 크롤링
def check_and_create_csv(file_path,columns):
    # 파일이 존재하는지 확인
    if not os.path.exists(file_path):
        # 파일이 없으면 CSV 파일 생성
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)

def count_rows_in_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        # 행의 개수 세기
        row_count = sum(1 for row in csvreader)
    return row_count

def append_to_csv(file_path, data):
    # CSV 파일에 데이터를 이어 쓰기 위해 'a' 모드로 파일 열기
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # 2차원 리스트 데이터를 CSV 파일에 쓰기
        csvwriter.writerows(data)

def clean_string(s):
    # 줄바꿈(\n, \r) 제거
    s = s.replace('\n', ' ').replace('\r', ' ')
    # 두 칸 이상의 공백을 하나의 공백으로 변경
    s = re.sub(r'\s{2,}', ' ', s)
    # 문자열 양쪽의 공백 제거
    return s.strip()

def list_func_append(tbList,columns,data_list):
    dt_list = tbList.find_all('dt')
    dd_list = tbList.find_all('dd')
    for i in range(len(dd_list)):
        dt_str = dt_list[i].text.strip()
        if dt_str not in columns: break
        idx = columns.index(dt_str)
        data_list[idx] = clean_string(dd_list[i].text)
    return data_list

def crawl_list_in_info(data_list_p,links,columns):
    for link in links:
        url = f'https://www.jobkorea.co.kr/{link}'
        # URL에서 HTML 컨텐츠 가져오기
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            print(f"Failed to retrieve contents from {url}")
            return
        time.sleep(2)
        # BeautifulSoup를 사용하여 HTML 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        tbList = soup.find('div',{'class':'tbCol'}).find('dl',{'class':'tbList'})
        company_name = soup.find('div',{'class':'coInfo'}).find('h4').text
        print(company_name)
        data_list=['']*len(columns)
        data_list[columns.index('회사명')] = company_name
        data_list = list_func_append(tbList,columns,data_list)
        data_list_p.append(data_list)

def crawl_list_link(url, columns,csv_filename):
    key = int((count_rows_in_csv(csv_filename) / 20))+ 1
    data_list_p = []
    print(key)
    # URL에서 HTML 컨텐츠 가져오기
    response = requests.get(f'{url}{key}', headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        print(f"Failed to retrieve contents from {url}")
        
    
    # BeautifulSoup를 사용하여 HTML 파싱
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 필요한 데이터를 추출하여 리스트에 추가
    article = soup.find('article',{'class':'list'})
    if article:
        links = [header.attrs['href'] for header in article.find_all('a',{'class':'information-title-link'})]
        crawl_list_in_info(data_list_p, links, columns)
        append_to_csv(csv_filename,data_list_p)
        crawl_list_link(url, columns,csv_filename)
        
def main():
    csv_filename = 'company_scout_info.csv'
    # 데이터를 저장할 리스트 초기화
    url = 'https://www.jobkorea.co.kr/Search/?duty=1000235&tabType=recruit&Page_No='    # 크롤링할 리스트 주소
    columns=['회사명','경력','학력','스킬','핵심역량','기본우대','자격증','외국어']           # 크롤링해서 넣을 리스트
    check_and_create_csv(csv_filename,columns)
    crawl_list_link(url,columns,csv_filename)
main()