from flask import Flask, render_template, url_for, request
from datetime import datetime
import pandas as pd
# from flask_bootstrap import Bootstrap
import requests
from bs4 import BeautifulSoup
import math

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
            df = df[df['full_citation'].str.title().str.contains(citation.title())]
        return render_template('index.html', df=df, art_num=len(df), update_day=update_day)
        # return render_template('indexV1.html', df=df.to_html(classes='table table-striped', index=False, render_links=True, escape=False), art_num=len(df), update_day=update_day)

    return render_template('index.html', df=df,art_num=len(df), update_day=update_day)
    # return render_template('indexV1.html', df=df.to_html(classes='table table-striped', index=False, render_links=True, escape=False), art_num=len(df), update_day=update_day)

@app.route("/test")
def test():
    return '<h1> Test Page </h1>'


if __name__ == '__main__':
    app.run(debug=True)