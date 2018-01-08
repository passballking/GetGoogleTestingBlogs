#!/usr/bin/env python
# encoding=utf-8

import requests, re

DOWNLOAD_URL = 'https://testing.googleblog.com/?action=getTitles&widgetId=BlogArchive1&widgetType=BlogArchive&responseType=js&path=https%3A%2F%2Ftesting.googleblog.com%2F2017%2F06%2F&xssi_token=AOuZoY5a5JMoa9_-gJgPH-aAn3XJfE6O1g%3A1515193577646'


def download_page(url):
    data = requests.get(url)
    return (data.text)

def retrive(plainRes):
	m = re.search('\[\{.+\]', plainRes)
	result = m.group(0)
	print(result)

def main():
    page = download_page(DOWNLOAD_URL)
    retrive(page)

if __name__ == '__main__':
    main()

