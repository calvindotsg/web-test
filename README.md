<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Automated web testing and web scraping for search metrics with configurable parameters</h1>
</p>
<!-- PROJECT LOGO -->

[![GitHub stars](https://img.shields.io/github/stars/calvindotsg/web-test)](./portfolio/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/calvindotsg/web-test)](./portfolio/network)
[![GitHub issues](https://img.shields.io/github/issues/calvindotsg/web-test)](./portfolio/issues)
[![GitHub license](https://img.shields.io/github/license/calvindotsg/web-test)](./portfolio/blob/master/LICENSE)

## Overview

For the purpose of automated web testing with Selenium, this Python project is a web scraping tool designed to extract specific elements from a website based on a list of keywords. It navigates to a specific search URL, takes a screenshot, and captures text elements. All configurations and parameters, such as the website URL and the text to find, are now loaded from a YAML configuration file. Metrics are stored in an output CSV file.

## Technologies Used

- Python
- Selenium WebDriver
- BeautifulSoup
- Pandas
- YAML

## Requirements

To run this project, you need to install the required Python packages:

```bash
pip install selenium pandas beautifulsoup4 pyyaml
```

Also, download the appropriate [WebDriver](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) for the browser you are using.

## Features

- Page load time capture.
- Screenshot taking.
- Text element extraction.
- Configuration from YAML file.
- Unit tests for code validation (`test_main.py`).

## How to Use

1. Clone this repository.
2. Modify `config.yaml` to set your configurations like `website`, `inputFile`, `outputFile`, and string match parameters.
3. Add a CSV file with keywords based on your `inputFile` configuration.
4. Run the main script:

```bash
python main.py
```

To run unit tests, execute:

```bash
python -m unittest test_main.py
```

## Code Structure

The code is divided into modular functions, each doing a specific task:

- `initialize_driver()`: Initializes WebDriver.
- `read_keywords_from_csv(file_path)`: Reads keywords from the input CSV.
- `capture_page_load_time(start_time)`: Captures page load time.
- `capture_http_status(driver)`: Captures HTTP status code.
- `take_screenshot(driver, keyword, file_name)`: Takes screenshots.
- `save_metrics(df, index, page_load_time, elements_retrieved)`: Saves metrics into a DataFrame.
- `find_elements_from_source(soup_string, str1, sub2)`: Extracts specific text elements.
- `retrieve_elements(driver)`: Extracts multiple text elements.
- `export_to_csv(df, output_file_path)`: Exports DataFrame to CSV.
- `main()`: Main function to control the flow.

## Testing

The project includes a `test_main.py` file that contains unit tests for the different functionalities.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome. For major changes, please open an issue first to discuss what you would like to add or modify.

## Author

- [Calvin](https://calvin.sg)