#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def get_page(url):
    try:
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            print("Error " + str(response.status_code))
            return False
    except requests.exceptions.ConnectTimeout:
        print('Connection timeout occured!')
    except requests.exceptions.ReadTimeout:
        print('Read timeout occured')
    except requests.exceptions.ConnectionError:
        print('... dns lookup failed..')


def extract_news(url):
    """ Extract news from a given web page """
    news_list = []
    response = get_page(url)
    page = BeautifulSoup(response, 'html5lib')
    tables = page.table.findAll('table')[1].findAll('tr', {'class': 'athing'})
    for i in range(len(tables)):
        id = 'item?id=' + tables[i]['id']
        new = {'title': page.findAll('a', {'class': 'storylink'})[i].text,
               'url': page.findAll('a', {'class': 'storylink'})[i]['href'],
               'author': page.findAll('a', {'class': 'hnuser'})[i].text,
               'points': page.findAll('span', {'class': 'score'})[i].text,
               'comments': page.findAll('a', {'href': id})[-1].text}
        news_list.append(new)
    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    return parser.table.findAll('table')[1].findAll('a')[-1]['href']


def get_news(url, pages=1):
    """ Collect news from a given web page """
    news = []
    while pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        parser = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(url)
        next_page = extract_next_page(parser)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        pages -= 1
    return news


def split(string): # функция, которая будет разбивать заголовки на отдельные слова
    return [letter for letter in string.split() if letter != ' ']
