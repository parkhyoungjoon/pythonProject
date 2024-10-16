import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import os
import csv
# 자소서 정보 크롤링
def check_and_create_csv(file_path,columns):
    # 파일이 존재하는지 확인
    if not os.path.exists(file_path):
        # 파일이 없으면 CSV 파일 생성
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
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

def list_func_append(tbList,data_list_p,company_name):
    dt_list = tbList.find_all('dt')
    dd_list = tbList.find_all('dd')
    for i in range(len(dd_list)):
        dt_str = dt_list[i].text[6:].strip()
        dd_str = clean_string(dd_list[i].text)[3:]
        data_list_p.append([company_name,dt_str,dd_str])

def crawl_list_in_info(data_list_p,links):
    for link in links:
        url = f'https://www.jobkorea.co.kr/{link}'
        # URL에서 HTML 컨텐츠 가져오기
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            print(f"Failed to retrieve contents from {url}")
            return
        # BeautifulSoup를 사용하여 HTML 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        selfQna = soup.find('div',{'class':'selfQnaWrap'})
        if selfQna:
            tbList = selfQna.find('dl',{'class':'qnaLists'})
            company_name = soup.find('div',{'class':'viewTitWrap'}).find('a').text
            print(company_name)
            list_func_append(tbList,data_list_p,company_name)

def crawl_list_link(url,csv_filename, key = 1):

    data_list_p = []
    print(key)
    # URL에서 HTML 컨텐츠 가져오기
    response = requests.get(f'{url}{key}', headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        print(f"Failed to retrieve contents from {url}")
    
    # BeautifulSoup를 사용하여 HTML 파싱
    soup = BeautifulSoup(response.content, 'html.parser')
    # 필요한 데이터를 추출하여 리스트에 추가
    article = soup.find('ul',{'class':'selfLists'})
    if article:
        links = [header.attrs['href'] for header in article.select('div.answer > a')]
        crawl_list_in_info(data_list_p, links)
        append_to_csv(csv_filename,data_list_p)
        if links:
            crawl_list_link(url,csv_filename, key+1)

def main():
    csv_filename = 'company_corear.csv'
    # 데이터를 저장할 리스트 초기화
    url = 'https://www.jobkorea.co.kr/starter/PassAssay?FavorCo_Stat=0&Pass_An_Stat=0&OrderBy=0&EduType=0&WorkType=0&schPart=10031&isSaved=1&Page='    # 크롤링할 리스트 주소
    columns=['회사명','질문','답']           # 크롤링해서 넣을 리스트
    check_and_create_csv(csv_filename,columns)
    crawl_list_link(url,csv_filename)
main()