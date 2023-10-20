import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def add_company_info(df):
    # Add new columns
    df['stars'] = -1.0
    df['sector'] = ""
    df['num_employees'] = ""
    df['glassdoor_link'] = ""

    for c in df['company'].unique():
        # Get search page
        url = f"https://www.glassdoor.com/Search/results.htm?keyword={c.replace(' ', '%20')}"
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10) 
        driver.get(url)

        # Check the first tile (current limitation)
        company_tiles = driver.find_elements(By.CLASS_NAME, "company-tile")
        if len(company_tiles) < 1:
            print(f"Could not find reviews for company {c}")
            continue

        # Save to df
        tile = company_tiles[0]
        hyperlink = tile.get_attribute("href")
        df.loc[df['company'] == c, 'glassdoor_link'] = hyperlink

        stars, sector, num_employees = "", "", ""

        try:
            stars = tile.find_element(By.XPATH, "div[1]/div/div/strong").text.split(' ')[0]
            df.loc[df['company'] == c, 'stars'] = stars
        except:
            print(f"Unable to find stars for {c}")

        try:
            sector = tile.find_element(By.XPATH, "div[2]/div[1]/span[1]").text
            df.loc[df['company'] == c, 'sector'] = sector
        except:
            print(f"Unable to find sector for {c}")
        
        try:
            num_employees = tile.find_element(By.XPATH, "div[2]/div[1]/span[2]").text
            df.loc[df['company'] == c, 'num_employees'] = num_employees
        except:
            print(f"Unable to find number of employees for {c}")

        print(c, stars, sector, num_employees, hyperlink)
    
    return df
