from flask import Flask
from MLModularcodingProject.logger import logging

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
          logging.info("we are testing our logging file")

          return "Welcome to Data Science Learning - MLModularcodingProject"


if __name__ == "__main__":
        app.run(debug = True) #5000