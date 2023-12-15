import requests
import pandas as pd
import configparser

from bs4 import BeautifulSoup
from datetime import datetime 
from sqlalchemy import create_engine

# Reading configuration data from '.env'
config = configparser.ConfigParser()
config.read('.env')

# Retrieving database connection details
['DB_CONN']
db_user = config['DB_CONN']['user']
db_password = config['DB_CONN']['password']
db_host = config['DB_CONN']['host']
db_database = config['DB_CONN']['database']

# List of page numbers to scrape
page_numbers = [1, 2]
data_frames = []  # List to store DataFrames

# Base URL for web scraping
base_url = 'https://afx.kwayisi.org/ngx/?page={}'

# Function to extract data from web pages
def extraction():
    for page_num in page_numbers:
        url = base_url.format(page_num)
        scrapped_data = requests.get(url)
        scrapped_data = scrapped_data.content
        soup = BeautifulSoup(scrapped_data, 'lxml')
        
        # Find all tables on the page
        tables = soup.find_all('table')
        
        # Check if there are at least four tables
        if len(tables) >= 4:
            html_data = str(tables[3])  # Assuming the fourth table is what you need
            df_list = pd.read_html(html_data)
            
            # Assuming there's only one DataFrame in the list
            if df_list:
                data_frames.append(df_list[0])

    # Concatenate all DataFrames obtained from different pages into a single DataFrame
    if data_frames:
        combined_df = pd.concat(data_frames, ignore_index=True)
        return combined_df
    else:
        print("No data found or tables don't match the expected structure.")

# Extract data
df = extraction()

# Function for data transformation
def transformation():
    current_date = datetime.now().strftime('%y-%m-%d')
    df['Scraped Date'] = current_date
    
    # Check for null values in 'Volume'
    if df['Volume'].isnull().any():  # Check if any null values exist
        mean_volume = df['Volume'].mean()
        df['Volume'].fillna(mean_volume, inplace=True)  # Replace null values with the mean
    
    return df

# Perform data transformation
df = transformation()
print(df)  # Display transformed DataFrame

# Database connection
def db_connection(db_user, db_password, db_host, db_database):
    try:
        db_url = f'postgresql://{db_user}:{db_password}@{db_host}/{db_database}'
        return db_url
    except Exception as e:
        print('There was an error:', e)

# Create database connection URL
db_url = db_connection(db_user, db_password, db_host, db_database)
engine = create_engine(db_url)  # Create SQLAlchemy engine for the database

# Function to load data into the database
def loading():
    df.to_sql(name='html_data', con=engine, if_exists='replace', index=False)

# Load data into the database
loading()
