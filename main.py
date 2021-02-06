from flask import Flask, render_template, url_for, request
from datetime import datetime, timedelta
import pandas as pd
# from flask_bootstrap import Bootstrap
import requests
from bs4 import BeautifulSoup
import math
from pub_list2 import CreateTable

# update_day = datetime.now().strftime("%B %d, %Y")
with open('update.csv', 'r') as up:
    update_day = up.read()

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    # form = Search()
    # global df
    df = pd.read_csv('CyTOFArticles.csv')
    df = df[['Year','Title', 'full_authors','full_citation','link']]#, 'PMID'
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
        return render_template('index.html', df=df, art_num=len(df), update_day=update_day)
        # return render_template('indexV1.html', df=df.to_html(classes='table table-striped', index=False, render_links=True, escape=False), art_num=len(df), update_day=update_day)

    return render_template('index.html', df=df,art_num=len(df), update_day=update_day)
    # return render_template('indexV1.html', df=df.to_html(classes='table table-striped', index=False, render_links=True, escape=False), art_num=len(df), update_day=update_day)

@app.route("/test")
def test():

    with open('update.csv') as up:
        last_update = up.read()
    last_update = datetime.strptime(last_update, "%B %d, %Y")
    if last_update.date() < datetime.today().date():
        create_table = CreateTable()
        df = create_table.papers()
        df = df[['Year', 'Title', 'full_authors', 'full_citation', 'link']]
        return render_template('index.html', df=df, art_num=len(df), update_day=update_day)
    return f'<h1> The page is updated</h1>'
    # df = pd.read_csv('CyTOFArticles2.csv')
    # num_articles = df.shape[0]
    # new_articles = 1198
    # if new_articles > num_articles:
    #     diff = math.ceil((new_articles-num_articles)/10)
    #     page = 1
    #     while page <= diff:
    #         df1 = pd.DataFrame([1,2,3,4,5,6,7,8])
    #         df = pd.concat(df1, df)
    #         print(df.head())
    #         print(f'diff {diff} current page {page}')
    #         page += 1
    #
    #
    # with open('update.csv') as up:
    #     last_update = up.read()
    #     last_update = datetime.strptime(last_update, "%B %d, %Y")
    # if last_update.date() + timedelta(days=-1) < datetime.today().date():
    #     return f'<h1> It needs update. Last update on {last_update}</h1>'
    # return f'<h1> The page is updated</h1>'


if __name__ == '__main__':
    app.run(debug=True)