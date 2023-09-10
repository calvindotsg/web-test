<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Automated web testing and web scraping Metrics Collector with SQLite Database and configurable parameters</h1>
</p>
<!-- PROJECT LOGO -->

[![GitHub stars](https://img.shields.io/github/stars/calvindotsg/web-test)](./web-test/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/calvindotsg/web-test)](./web-test/network)
[![GitHub issues](https://img.shields.io/github/issues/calvindotsg/web-test)](./web-test/issues)
[![GitHub license](https://img.shields.io/github/license/calvindotsg/web-test)](./web-test/blob/master/LICENSE)

## Overview

As part of automated web testing, this Python project automates web scraping specific elements from a search page. It captures screenshots, extracts text elements such as logos, MCC, and merchant names, and stores them in both a CSV and an SQLite database. The project now supports more robust error handling and logging, and all configurations are read from a YAML file for flexibility.

## Technologies Used

- Python
- Selenium WebDriver
- BeautifulSoup
- Pandas
- SQLite
- YAML

## Requirements

Install the required Python packages:

```bash
pip install selenium pandas beautifulsoup4 pyyaml sqlite3
```

Also, ensure to download the appropriate [WebDriver](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) for your browser.

## Features

- Captures screenshots for search results.
- Extracts specific text elements.
- Configuration from a YAML file.
- Storing metrics in an SQLite database and CSV file as required.
- Unit tests for code validation (`test_main.py`).
- Detailed logging and error handling.

## How to Use

1. Clone the repository.
2. Modify the `config.yaml` file to set your configurations.
3. Add a CSV file with keywords based on the `inputFile` configuration in `config.yaml`.
4. Run the main script:

```bash
python main.py
```

To run unit tests:

```bash
python -m unittest test_main.py
```

### YAML structure

```yaml
inputFile : string
outputFile : string
outputImages : string
website : string
average_page_load_time : integer

logo_str1 : string
logo_str2 : string
logo_str2_alt : string
mcc_str1 : string
mcc_str2 : string
merchant_name_str1: string
merchant_name_str2: string
```

## Code Structure

The code is modular, with each function performing specific tasks:

- `initialize_driver()`: Initializes WebDriver.
- `read_keywords_from_csv()`: Reads keywords from a CSV file.
- `take_screenshot()`: Captures screenshots.
- `save_metrics()`: Saves metrics to a DataFrame.
- `find_elements_from_source()`: Extracts text elements.
- `retrieve_elements()`: Retrieves multiple text elements.
- `export_to_csv()`: Exports data to CSV.
- `connect_db()`: Establishes a database connection.
- `create_table()`: Creates a table in the SQLite database.
- `insert_data()`: Inserts data into the database.
- `main()`: Main function that orchestrates the workflow.

## Database Integration

The project utilizes SQLite to store metrics. The SQLite database is created and managed through the Python `sqlite3` library. Each keyword's scraped data is stored in a new row in the `metrics` table.

## Testing

Unit tests (`test_main.py`) are included to ensure the code's functionality.

## License

This project is open-source and under the MIT License.

## Contributing

Contributions are welcome. For major changes, please open an issue first.

## Author

- [Calvin](https://calvin.sg)

Feel free to customize this README.md to suit your project's specific requirements.
