import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import math

# df = pd.read_csv('CyTOFArticles.csv')
# df = df[['Year', 'Title', 'full_authors', 'full_citation', 'link']]
# # for pub in df['full_citation']:
# #     print(pub.split(".")[0])
#
# df['journal'] = [pub.split(".")[0] for pub in df['full_citation']]
#
# plt.figure(figsize=(16,8))
# plt.bar(x=df['journal'].value_counts().index[0:50],height=df['journal'].value_counts()[0:50])
# plt.xticks(rotation=90)
# plt.ylabel('Number of Papers')
# plt.title("Number of Mass Cytometry Papers Published by Journal: Top 50 Journals")
# # plt.show()
# plt.tight_layout()
#
# plt.savefig('top_50_journals.')
# # for index, row in df.iterrows():
# #     print(row[4])
# #
# # with open('update.csv', "w") as up:
# #     up.write(datetime.now().strftime("%B %d, %Y %H:%M:%S"))
# # with open('update.csv', 'r') as up:
# #     test = up.read()
# # print(type(test))

df = pd.read_csv('CyTOFArticles.csv')
num_articles = df.shape[0]
print(num_articles)
new_articles = 1198
if new_articles > num_articles:
    n_pages = math.ceil((new_articles-num_articles)/10)
    print(f'n_pages {n_pages}')
    diff = new_articles-num_articles
    print(f'diff {diff}')
    page = 1
    df2=pd.DataFrame()
    while page <= n_pages:
        print(page)
        df1 = pd.DataFrame([[1,2,3,4,5,6,7,8]]*10, columns=df.columns)
        df2 = pd.concat([df1, df2], axis=0)
        # print(df.head())
        # print(f'diff {diff} current page {page}')
        print(df2)
        page += 1
    df = pd.concat([df2[0:diff], df])
    print(df)
    print(df.reset_index())