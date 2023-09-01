<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Automated web testing and scraper for search result metrics</h1>
</p>
<!-- PROJECT LOGO -->

[![GitHub stars](https://img.shields.io/github/stars/calvindotsg/auto-web-test)](./portfolio/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/calvindotsg/auto-web-test)](./portfolio/network)
[![GitHub issues](https://img.shields.io/github/issues/calvindotsg/auto-web-test)](./portfolio/issues)
[![GitHub license](https://img.shields.io/github/license/calvindotsg/auto-web-test)](./portfolio/blob/master/LICENSE)

## Overview

For the purpose of automated web testing with Selenium, this Python project automates the process of web scraping specific elements from a website based on a list of keywords. The program navigates to a specified search URL for each keyword, captures a screenshot, and extracts specific text elements using BeautifulSoup. The captured metrics are stored in an output CSV file for further analysis.

## Technologies Used

- Python
- Selenium WebDriver
- BeautifulSoup
- Pandas

## Requirements

To run this project, you need to install the following Python packages:

```bash
pip install selenium pandas beautifulsoup4
```

Also, make sure to download the appropriate [WebDriver](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) for the browser you are using.

## Features

- Captures page load time for each keyword search.
- Takes a screenshot for each keyword's search result.
- Extracts and stores specific text elements like logo, MCC, and Merchant Name.
- Logs all the metrics into an output CSV file.

## How to Use

1. Clone this repository.
2. Add a CSV file named `top5.csv` in the `assets` directory, with a column named `keyword` listing the keywords you want to test.
3. Update the `website` variable to point to your target search URL.
4. Run the script:

```bash
python main.py
```

## Code Structure

The code is organized into modular functions, each responsible for a specific task:

- `initialize_driver()`: Initializes WebDriver.
- `read_keywords_from_csv(file_path)`: Reads keywords from the input CSV file.
- `capture_page_load_time(start_time)`: Captures page load time.
- `capture_http_status(driver)`: Captures HTTP status code.
- `take_screenshot(driver, keyword, file_name)`: Takes screenshots.
- `save_metrics(df, index, page_load_time, elements_retrieved)`: Saves metrics into a DataFrame.
- `find_elements_from_source(soup_string, str1, sub2)`: Extracts specific text elements.
- `retrieve_elements(driver)`: Captures number of results and other text elements.
- `export_to_csv(df, output_file_path)`: Exports the DataFrame to an output CSV file.
- `main()`: Main function to control the flow.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author

- [Calvin](https://calvin.sg)