import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('CyTOFArticles.csv')
df = df[['Year', 'Title', 'full_authors', 'full_citation', 'link']]
# for pub in df['full_citation']:
#     print(pub.split(".")[0])

df['journal'] = [pub.split(".")[0] for pub in df['full_citation']]

plt.figure(figsize=(16,8))
plt.bar(x=df['journal'].value_counts().index[0:50],height=df['journal'].value_counts()[0:50])
plt.xticks(rotation=90)
plt.ylabel('Number of Papers')
plt.title("Number of Mass Cytometry Papers Published by Journal: Top 50 Journals")
# plt.show()
plt.tight_layout()

plt.savefig('top_50_journals.')
# for index, row in df.iterrows():
#     print(row[4])
#
# with open('update.csv', "w") as up:
#     up.write(datetime.now().strftime("%B %d, %Y %H:%M:%S"))
# with open('update.csv', 'r') as up:
#     test = up.read()
# print(type(test))