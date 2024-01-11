from flask import Flask
from MLModularcodingProject.logger import logging
from MLModularcodingProject.exception import CustomException
import os, sys
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

    try:
        raise Exception("We are testing our exception file") # Error
    
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)
    
        logging.info("we are testing our logging file")

        return "Welcome to Data Science Learning - MLModularcodingProject"


if __name__ == "__main__":
        app.run(debug = True) #5000