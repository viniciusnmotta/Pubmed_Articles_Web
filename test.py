import pandas as pd
from pub_list import df
from datetime import datetime

df = pd.read_csv('CyTOFArticles.csv')
df = df[['Year', 'Title', 'full_authors', 'full_citation', 'link']]

for index, row in df.iterrows():
    print(row[4])

with open('update.csv', "w") as up:
    up.write(datetime.now().strftime("%B %d, %Y %H:%M:%S"))
with open('update.csv', 'r') as up:
    test = up.read()
print(type(test))