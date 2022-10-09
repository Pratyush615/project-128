from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)

soup = bs(page.text, 'html.parser')

star_table = soup.find_all('table')

table_rows = star_table[7].find_all('tr')

temp_list = []
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Name = []
Radius = []
Distance = []
Mass = []

for i in range(1,len(temp_list)):
    Name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][8])
    Radius.append(temp_list[i][9])
df = pd.DataFrame(list(zip(Name,Distance,Mass,Radius)),columns=["Star_name","Distance","Mass","Radius"])
df.to_csv("dwarf_stars.csv")