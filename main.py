# Importing required libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import yaml

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

inputFile = config["inputFile"]
outputFile = config["outputFile"]
website = config["website"]
average_page_load_time = config["average_page_load_time"]

substring_to_find_elements = {
    "logo": {
        "str1": config["logo_str1"],
        "str2": config["logo_str2"]
    },
    "mcc": {
        "str1": config["mcc_str1"],
        "str2": config["mcc_str2"]
    },
    "merchant_name": {
        "str1": config["merchant_name_str1"],
        "str2": config["merchant_name_str2"]
    }
}


# Initialize WebDriver
def initialize_driver():
    driver = webdriver.Chrome()
    return driver


# Read keywords from CSV
def read_keywords_from_csv(file_path):
    return pd.read_csv(file_path)


# Capture page load time
def capture_page_load_time(start_time):
    return time.time() - start_time


# Take screenshot
def take_screenshot(driver, keyword, file_name):
    driver.save_screenshot('output/' + keyword + '_' + file_name)


# Save metrics to DataFrame
def save_metrics(df, index, page_load_time, elements_retrieved):
    df.at[index, 'Page Load Time'] = page_load_time
    df.at[index, 'MCC'] = elements_retrieved["mcc"]
    df.at[index, 'Merchant Name'] = elements_retrieved["merchant_name"]
    df.at[index, 'Logo'] = elements_retrieved["logo"]
    # df.at[index, 'HTTP Status Code'] = http_status_code


def find_elements_from_source(soup_string, str1, sub2, elementName):

    # try block to handle exceptions when substring is not found in http source
    try:
        # getting index of substrings
        idx1 = soup_string.index(str1)
        idx2 = soup_string.index(sub2)

        res = ''
        # getting elements in between
        for idx in range(idx1 + len(str1), idx2):
            res = res + soup_string[idx]

    except ValueError as ve:
        res = "Not found substring in source for " + elementName + " element"
        print("Print value error " + elementName + " element: ", ve)
    except Exception as e:
        res = "Exception occurred while finding substring in source " + elementName + " element"
        print("Print error " + elementName + " element: ", e)

    # printing result
    print("The extracted " + elementName + " element string : " + res)
    return str(res)


# Capture Number of Results and other text elements
def retrieve_elements(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    soup_string = str(soup)
    # print(soup_string)

    logo = find_elements_from_source(soup_string,
                                     substring_to_find_elements["logo"]["str1"],
                                     substring_to_find_elements["logo"]["str2"],
                                     "logo"
                                     )
    mcc = find_elements_from_source(soup_string,
                                    substring_to_find_elements["mcc"]["str1"],
                                    substring_to_find_elements["mcc"]["str2"],
                                    "mcc"
                                    )
    merchant_name = find_elements_from_source(soup_string,
                                              substring_to_find_elements["merchant_name"]["str1"],
                                              substring_to_find_elements["merchant_name"]["str2"],
                                              "merchant_name"
                                              )

    # creating a dictionary
    retrieved_element_names = {"logo": logo, "mcc": mcc, "merchant_name": merchant_name}

    return retrieved_element_names


# Export DataFrame to CSV
def export_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)


# Main function to control the flow
def main():
    driver = initialize_driver()
    keywords_df = read_keywords_from_csv(inputFile)

    for index, row in keywords_df.iterrows():
        site = website + row['keyword']
        driver.get(site)
        start_time = time.time()
        page_load_time = capture_page_load_time(start_time)
        # wait for page to load
        time.sleep(average_page_load_time)
        elements_retrieved = retrieve_elements(driver)
        take_screenshot(driver, row['keyword'], f"{index}.png")
        # Copy text elements and other related metrics.
        save_metrics(keywords_df, index, page_load_time, elements_retrieved)

    export_to_csv(keywords_df, outputFile)
    driver.quit()


# Run the main function
main()
