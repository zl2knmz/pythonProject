import csv

import requests
from bs4 import BeautifulSoup
import os


# 百格首页活动
def bai_ge():
    url = 'https://www.bagevent.com/index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}
    res = requests.get(url, headers=headers).text
    content = BeautifulSoup(res, "html.parser")

    logos = []
    logo_list = content.find_all('div', attrs={'class': 'event_cover'})
    for var in logo_list:
        logo = var.find('img', attrs={'class': 'img_lazy'})['data-original']
        logos.append(logo)
    # print(logos)
    # print(len(logos))

    data = content.find_all('div', attrs={'class': 'info'})
    info_list = []
    row_title = ['活动标题', '活动地址', '活动时间', '海报地址']
    info_list.append(row_title)
    i = 0
    for d in data:
        row = []
        name = d.find('div', attrs={'class': 'name'}).contents[0]
        addr_temp = d.find('span', attrs={'class': 'location ellipsis'}).contents
        if len(addr_temp) > 2:
            addr = addr_temp[2]
        else:
            addr = addr_temp[1]

        date_temp = d.find('span', attrs={'class': 'time'}).contents
        if len(date_temp) > 2:
            date = date_temp[2]
        else:
            date = date_temp[1]
        # print(date)
        row.append(name)
        row.append(addr)
        row.append(date)
        row.append(logos[i])
        info_list.append(row)
        i = i + 1
    # print(info_list)
    # print(len(info_list))
    if not os.path.exists(r'picture'):
        os.mkdir(r'picture')
    with open('./picture/bai_ge_event.csv', 'w', newline='', encoding='utf-8') as flow:
        csv_writer = csv.writer(flow, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for res in info_list:
            csv_writer.writerow([res[0], res[1], res[2], res[3]])


if __name__ == '__main__':
    bai_ge()
