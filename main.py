from flask import Flask
from datetime import datetime


now2 = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    return f"The date for the home is: {now}, the date for global is {now2}"



if __name__ == '__main__':
    app.run(debug=True)