from flask import Flask, render_template, url_for, request
from datetime import datetime, timedelta
import pandas as pd
import requests
from bs4 import BeautifulSoup
import math
from pub_list import CreateTable


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():

    today = datetime.today().date()

    with open('update.csv', 'r') as up:
        update_day = up.read()
        last_update = datetime.strptime(update_day, "%B %d, %Y")

    if last_update.date() < today:
        create_table = CreateTable()
        create_table.update_pub()
        df = pd.read_csv('CyTOFArticles.csv')
        print(f"Number of duplicates after update function: {df.duplicated().sum()}")
        df.drop_duplicates(subset=['PMID'], inplace=True)
        df.to_csv('CyTOFArticles.csv', index=False)
        update_day = today.strftime("%B %d, %Y")

    df = pd.read_csv('CyTOFArticles.csv')
    print(f"number of duplicates in the csv file: {df.duplicated().sum()}")

    df = df[['Year', 'Title', 'full_authors', 'full_citation', 'link']]#, 'PMID'
    # df["col"] = df["link"].apply(lambda x: "<a href='{}'>{}</a>".format(x,x))
    if request.method == 'POST':
        year = request.form['year']
        title = request.form['title']
        author = request.form['author']
        citation = request.form['citation']
        if year != "":
            df = df[df['Year'] == int(year)]
        if title != "":
            df = df[df['Title'].str.lower().str.contains(title.lower())]
        if author != "":
            df = df[df['full_authors'].str.title().str.contains(author.title())]
        if citation != "":
            df = df[df['full_citation'].str.title().str.match(citation.title())]
            df = df.sort_values(['Year','full_citation'], ascending=False)
        return render_template('index.html', df=df, art_num=df.shape[0], update_day=update_day)

    return render_template('index.html', df=df, art_num=df.shape[0], update_day=update_day)


@app.route("/test")
def test():
    with open('update.csv') as up:
        last_update = up.read()
    last_update = datetime.strptime(last_update, "%B %d, %Y")
    if last_update.date() < datetime.today().date():
        return f'<h1>this page needs update</h1>'
    return f'<h1> The page is updated</h1>'



if __name__ == '__main__':
    app.run(debug=True)