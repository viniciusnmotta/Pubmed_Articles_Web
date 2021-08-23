import requests
from bs4 import BeautifulSoup
import pandas as pd
import math
from datetime import datetime


class CreateTable:

    def update_pub(self):
        df = pd.read_csv('CyTOFArticles.csv')
        URL = "https://pubmed.ncbi.nlm.nih.gov/?term=%22Mass+Cytometry%22+or+%22cytof%22&sort=date"
        page = 1
        n_pages = 3
        df2 = pd.DataFrame()

        while page <= n_pages:
            print(page)
            response = requests.get(url=f"{URL}&page={page}")
            soup = BeautifulSoup(response.text, "html.parser")
            num_articles = int(soup.find('span', class_="value").text.replace(",", ""))
            # n_pages = math.ceil((num_articles - df.shape[0]) / 10)
            # print(n_pages)

            titles = [" ".join(item.text.split()) for item in soup.find_all(class_='docsum-title')]
            short_authors = [item.text for item in soup.find_all(class_='docsum-authors short-authors')]
            short_citations = [item.text for item in soup.find_all(class_='docsum-journal-citation short-journal-citation')]
            PMIDs = [item.text for item in soup.find_all(class_='docsum-pmid')]
            links = ["https://pubmed.ncbi.nlm.nih.gov"+item['href'] for item in soup.find_all("a", class_="docsum-title", href=True)]
            full_authors = [item.text for item in soup.find_all(class_='docsum-authors full-authors')]
            full_citations = [item.text for item in soup.find_all(class_='docsum-journal-citation full-journal-citation')]
            year = [item.split(". ")[1].replace(".","") for item in short_citations]
            my_dict = {'PMID': PMIDs,
                       'Year': year,
                      'Title': titles,
                       'short_author': short_authors,
                       'short_citation': short_citations,
                       'link': links,
                       'full_authors': full_authors,
                       'full_citation': full_citations,
                       }
            df1 = pd.DataFrame(my_dict)
            df2 = pd.concat([df2, df1], axis=0)
            page += 1
        self.date = datetime.now().strftime('%B %d, %Y')
        today = datetime.now().strftime("%Y%m%d")
        with open('update.csv', "w") as up:
            up.write(datetime.now().strftime("%B %d, %Y"))
        # diff = num_articles - df.shape[0]
        # print(diff)
        # df = pd.concat([df2[0:diff], df], axis=0)
        df = pd.concat([df2, df], axis=0)
        df.reset_index(drop=True, inplace=True)
        # df.drop_duplicates(inplace=True)
        df.to_csv('CyTOFArticles.csv', index=False)
        return df

    def create_pub(self):
        URL = "https://pubmed.ncbi.nlm.nih.gov/?term=%22Mass+Cytometry%22+or+%22cytof%22&sort=date"
        # URL = 'https://pubmed.ncbi.nlm.nih.gov/?term=%22Mass+Cytometry%22&sort=date'
        num_articles = requests.get(url=URL)
        num_articles = BeautifulSoup(num_articles.text, "html.parser")
        num_articles = int(num_articles.find('span', class_="value").text.replace(",",""))
        n_pages = math.ceil(num_articles/10)
        print(num_articles)
        page = 1
        df = pd.DataFrame()
        while page <= n_pages:
            print(page)
            response = requests.get(url=f"{URL}&page={page}")
            print(response.status_code)

            soup = BeautifulSoup(response.text, "html.parser")

            titles = [" ".join(item.text.split()) for item in soup.find_all(class_='docsum-title')]
            short_authors = [item.text for item in soup.find_all(class_='docsum-authors short-authors')]
            short_citations = [item.text for item in soup.find_all(class_='docsum-journal-citation short-journal-citation')]
            PMIDs = [item.text for item in soup.find_all(class_='docsum-pmid')]
            links = ["https://pubmed.ncbi.nlm.nih.gov"+item['href'] for item in soup.find_all("a", class_="docsum-title", href=True)]
            full_authors = [item.text for item in soup.find_all(class_='docsum-authors full-authors')]
            full_citations = [item.text for item in soup.find_all(class_='docsum-journal-citation full-journal-citation')]
            year = [item.split(". ")[1].replace(".","") for item in short_citations]
            print(year)
            my_dict = {'PMID': PMIDs,
                       'Year': year,
                      'Title': titles,
                       'short_author': short_authors,
                       'short_citation': short_citations,
                       'link': links,
                       'full_authors': full_authors,
                       'full_citation': full_citations,
                       }
            df1 = pd.DataFrame(my_dict)
            df = pd.concat([df, df1], axis=0)
            page += 1
        with open('update.csv', "w") as up:
            up.write(datetime.now().strftime("%B %d, %Y"))
        df.to_csv('CyTOFArticles.csv', index=False)
        return df
#
# df = CreateTable()
# df_final = df.create_pub()

