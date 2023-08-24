import csv

import requests
from bs4 import BeautifulSoup
import time
import os


def liutao():
    url = 'https://movie.douban.com/celebrity/1011562/photos/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}
    res = requests.get(url, headers=headers).text
    content = BeautifulSoup(res, "html.parser")
    data = content.find_all('div', attrs={'class': 'cover'})
    picture_list = []
    for d in data:
        plist = d.find('img')['src']
        picture_list.append(plist)
    print(picture_list)


def fire():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}

    page = 0
    data_list = []
    for i in range(0, 450, 30):
        print("开始爬取第 %s 页" % page)
        url = 'https://movie.douban.com/celebrity/1011562/photos/?type=C&start={}&sortby=like&size=a&subtype=a'.format(i)
        res = requests.get(url, headers=headers).text
        data = get_poster_url(res)
        # download_picture(data)
        data_list.extend(data)
        page += 1
        time.sleep(1)

    save_csv(data_list)


def get_poster_url(res):
    content = BeautifulSoup(res, "html.parser")
    data = content.find_all('div', attrs={'class': 'cover'})
    picture_list = []
    for d in data:
        plist = d.find('img')['src']
        picture_list.append(plist)
    return picture_list


def download_picture(pic_l):
    if not os.path.exists(r'picture'):
        os.mkdir(r'picture')
    for i in pic_l:
        pic = requests.get(i)
        p_name = i.split('/')[7]
        with open('picture\\' + p_name, 'wb') as f:
            f.write(pic.content)


def save_csv(pic_l):
    if not os.path.exists(r'picture'):
        os.mkdir(r'picture')
    with open('./picture/liutao.csv', 'w', newline='', encoding='utf-8') as flow:
        csv_writer = csv.writer(flow, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for res in pic_l:
            # print(res)
            csv_writer.writerow([res])


if __name__ == '__main__':
    # liutao()
    fire()
