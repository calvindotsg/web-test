# Importing required libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import yaml
import sqlite3

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

inputFile = config["inputFile"]
outputFile = config["outputFile"]
website = config["website"]
average_page_load_time = config["average_page_load_time"]
outputImagesPath = config["outputImages"]

substring_to_find_elements = {
    "logo": {
        "str1": config["logo_str1"],
        "str2": config["logo_str2"],
        "str2_alt": config["logo_str2_alt"]
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


# Take screenshot
def take_screenshot(driver, keyword, file_name):
    driver.save_screenshot(outputImagesPath + file_name + '_' + keyword + '.png')


# Save metrics to DataFrame
def save_metrics(df, index, elements_retrieved):
    df.at[index, 'code MCC'] = elements_retrieved["mcc"]["code"]
    df.at[index, 'name MCC'] = elements_retrieved["mcc"]["name"]
    df.at[index, 'Merchant Name'] = elements_retrieved["merchant_name"]
    df.at[index, 'Logo'] = elements_retrieved["logo"]


def find_elements_from_source(soup_string, str1, sub2, element_name):
    # try block to handle exceptions when substring is not found in http source
    try:
        # getting index of substrings
        idx1 = soup_string.index(str1)
        idx2 = soup_string.index(sub2)

        res = ''
        # getting elements in between
        for idx in range(idx1 + len(str1), idx2):
            res = res + soup_string[idx]

        if "https://heymax.ai/default-merchant-logo.png" in res:
            res = "https://heymax.ai/default-merchant-logo.png"

        if element_name == 'mcc':
            mcc_code_res = res[:4]
            mcc_descr_res = res[7:]

            # creating a dictionary
            res = {"name": mcc_descr_res, "code": mcc_code_res}

    except ValueError as ve:
        # res = "Not found substring in source for " + element_name + " element"
        print("Print value error " + element_name + " element: ", ve)
    except Exception as e:
        # res = "Exception occurred while finding substring in source " + element_name + " element"
        print("Print error " + element_name + " element: ", e)

    # printing result
    print("The extracted " + element_name + " element string : " + str(res))
    # return as dictionary
    return res


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


# Database Connection
def connect_db():
    conn = sqlite3.connect("metrics.db")
    cursor = conn.cursor()
    return conn, cursor


# Create Table
def create_table(cursor):
    # cursor.execute("""
    #     DROP TABLE metrics
    #     """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS merchant_affiliation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id TEXT,
            merchant_name TEXT,
            merchant_description TEXT,
            merchant_icon TEXT,
            mcc_code TEXT,
            mcc_name TEXT,
            mcc_string TEXT
        );
        """)


# Insert Data
def insert_data(cursor, elements_retrieved):
    cursor.execute("INSERT INTO merchant_affiliation (document_id, merchant_name, merchant_description, merchant_icon, "
                   "mcc_code, mcc_name, mcc_string) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (None, elements_retrieved["merchant_name"], None, elements_retrieved["logo"],
                    elements_retrieved["mcc"]["code"], elements_retrieved["mcc"]["name"],
                    str(elements_retrieved["mcc"])))


# Main function to control the flow
def main():
    driver = initialize_driver()
    start_lapsed_time = time.time()
    keywords_df = read_keywords_from_csv(inputFile)
    conn, cursor = connect_db()
    create_table(cursor)

    for index, row in keywords_df.iterrows():
        print('Starting keyword: ' + row['keyword'])
        site = website + row['keyword']
        driver.get(site)
        # wait for page to load
        time.sleep(average_page_load_time)
        elements_retrieved = retrieve_elements(driver)
        take_screenshot(driver, row['keyword'], f"{index + 1}")
        # Copy text elements and other related metrics.
        save_metrics(keywords_df, index, elements_retrieved)
        insert_data(cursor, elements_retrieved)

    export_to_csv(keywords_df, outputFile)
    conn.commit()
    conn.close()
    print('Script lapsed time: ' + str(time.time() - start_lapsed_time) + ' seconds')
    driver.quit()


# Run the main function
main()
