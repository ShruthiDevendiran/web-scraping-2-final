from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)
        
soup = BeautifulSoup(page.text,'html.parser')

tables = soup.find_all('table',{"class":"wikitable sortable"})

temp_list = []

total_table = len(tables)
table_rows = tables[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
        Star_names.append(temp_list[i][0])
        Distance.append(temp_list[i][5])
        Mass.append(temp_list[i][7])
        Radius.append(temp_list[i][8])

headers = ['Star_name','Radius','Mass','Distance']

brown_star_df_1 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
brown_star_df_1.to_csv("brown_stars.csv",index = True, index_label="id")



    