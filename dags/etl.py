import requests
import pandas as pd
import configparser

from bs4 import BeautifulSoup
from datetime import datetime 
from sqlalchemy import create_engine

# Reading configuration data from '.env'
config = configparser.ConfigParser()
config.read('.env')


from helper import extraction, transformation, loading


#======= Extract data
df = extraction()


#======= Function for data transformation
transformation()


# Load data into the database
loading()




