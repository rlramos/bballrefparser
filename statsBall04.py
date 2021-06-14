#!/usr/bin/env python3

''' Scrape selected 2019-20 stats and export to a .csv file according to certain games (week, month, etc)'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

print("'True freedom is impossible without a mind made free by discipline.' - Mortimer J. Alders")

url = "https://www.basketball-reference.com/players/j/jamesle01/gamelog/2004/"
page = requests.get(url)
content = BeautifulSoup(page.text, 'html.parser') # lxml

header = content.find('div', attrs={"class":"table_wrapper"})
columns = [i.get_text() for i in header.find_all('th')]
columns = columns[1:30]

df = pd.DataFrame(columns=columns)
# print(df)

players = content.find_all('tr', attrs={'id':re.compile('pgl_basic.')})

stats = []
for i in players:
    stats = [stat.get_text() for stat in i.find_all('td')]

    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns

    df = pd.concat([df, temp_df], ignore_index=True)


df.to_csv(r"/Users/ralphramos/desktop/lebron04-05.csv", index = False, sep=',', encoding='utf-8')
print('Excel file exported.')
