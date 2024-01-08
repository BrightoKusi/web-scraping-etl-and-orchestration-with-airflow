# web-scraping-etl-and-orchestration-with-airflow

## Project: Financial Data Extraction, Transformation, and Loading
This project involves two components: a Python script for web scraping financial data and an Airflow DAG (stock_data) to orchestrate an ETL (Extract, Transform, Load) process.

## Python Script
Description
The Python script performs the following tasks:

# Imported Libraries

requests
pandas
configparser
BeautifulSoup
datetime
sqlalchemy

# Web Scraping

Defines a function extraction() to scrape financial data from multiple pages of a website (afx.kwayisi.org) using BeautifulSoup.
Gathers data from HTML tables and stores it in a list of Pandas DataFrames.

# Data Transformation

Defines a function transformation() for data manipulation.
Adds a 'Scraped Date' column with the current date.
Handles null values in the 'Volume' column by filling them with the mean value.
Saves the modified DataFrame as stock_data.csv.

# Database Loading

Defines a function loading() to load the transformed data into a PostgreSQL database using SQLAlchemy.
Creates a connection to the database and writes the DataFrame to a table named stock_data.


## Airflow DAG (stock_data)

Description
The Airflow DAG (stock_data) orchestrates the ETL process using the following structure:

DAG Configuration

DAG Name: stock_data
Description: A stock data web-scraping DAG
Schedule: Runs daily (@daily)
Start Date: January 7, 2024

Tasks

begin_execution: DummyOperator to signify the start of execution.
extraction: PythonOperator task that triggers the extraction() function from the etl module.
transformation: PythonOperator task that triggers the transformation() function from the etl module.
loading: PythonOperator task that triggers the loading() function from the etl module.
end_execution: DummyOperator to signify the completion of execution.

Dependencies

The tasks are set up with dependencies in the following sequence:
begin_execution starts the workflow.
extraction follows begin_execution.
transformation follows extraction.
loading follows transformation.
end_execution marks the end of the workflow.

Default Arguments

depends_on_past: False
email: "brightokusi@gmail.com"
email_on_failure: True
email_on_retry: True
retries: 1
retry_delay: timedelta(minutes=5)

# Usage
The Python script should be run within a Python environment with the required dependencies installed.
Ensure that the .env file containing the database connection details is present and correctly formatted for the Python script.
Airflow should be correctly configured and running to execute the stock_data DAG.
The Python functions imported into the stock_data DAG from the etl module should handle the respective steps of the ETL process.
The DAG will execute daily, following the defined schedule.

# Important Notes
Verify the HTML structure of the target website remains consistent for proper scraping in the Python script.
Adjust database connection details, table names, and any specific requirements in the Python script and Airflow DAG according to your setup.
Check the implementation of extraction, transformation, and loading functions in the Python script for any specific dependencies or configurations.
