# web-scraping-for-forex-site

# Financial Data Web Scraping and Database Loading

This repository contains a Python script that demonstrates web scraping financial data from a website and loading it into a PostgreSQL database. The script utilizes libraries such as Requests, BeautifulSoup, Pandas, and SQLAlchemy.

## Code Overview

- `main.py`: Python script that performs the web scraping, data transformation, database connection, and data loading tasks.
- `.env`: Configuration file storing database connection details.

## Getting Started

To run the script locally:

1. Clone this repository.
2. Ensure you have Python installed (preferably Python 3.x).
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Create a `.env` file with your database connection details in the format:
    ```
    [DB_CONN]
    user=your_db_user
    password=your_db_password
    host=your_db_host
    database=your_database_name
    ```
5. Run the `main.py` script.

## Usage

The `main.py` script consists of several functions:
- `extraction()`: Scrapes financial data from web pages.
- `transformation()`: Processes and transforms the collected data.
- `db_connection()`: Creates a PostgreSQL database connection URL.
- `loading()`: Loads the transformed data into the PostgreSQL database.

You can modify the code to suit your specific web scraping needs or adapt it to work with different databases.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests to propose improvements or additional functionalities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The script was developed as a demonstration and learning exercise.
- Special thanks to the contributors of the libraries used in this project.

---

_This README provides a brief overview of the project and its functionalities. For more detailed information, refer to the code and comments within `main.py`._
