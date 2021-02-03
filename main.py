from flask import Flask, render_template, url_for, request
from datetime import datetime
import pandas as pd
# from flask_bootstrap import Bootstrap
import requests
from bs4 import BeautifulSoup
import math

update_day = datetime.now().strftime("%B %d, %Y")

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def home():
    # form = Search()
    df = pd.read_csv('CyTOFArticles.csv')
    df = df[['Year','Title', 'full_authors','full_citation','link', 'PMID']]
    if request.method == 'POST':
        year = request.form['year']
        print(year)
        title = request.form['title']
        author = request.form['author']
        if year != "":
            df = df[df['Year'] == int(year)]
        if title != "":
            df = df[df['Title'].str.lower().str.contains(title.lower())]
        if author != "":
            df = df[df['full_authors'].str.title().str.contains(author.title())]
        return render_template('index.html', df=df.to_html(classes='table table-striped', index=False), art_num=len(df), update_day=update_day)

    return render_template('index.html', df=df.to_html(classes='table table-striped', index=False), art_num=len(df), update_day=update_day)

@app.route("/update")
def update():
    # df = papers()
    return '<h1>update is completed</h1>'


if __name__ == '__main__':
    app.run(debug=True)