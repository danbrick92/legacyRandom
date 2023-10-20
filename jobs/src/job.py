from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time

BASE_URL = "https://www.indeed.com/jobs"
JOBS_PER_PAGE = 15
WAIT_TIME = 3

def get_search_page(title, location):
    # Alter parameters to be browser supported
    title = title.replace(" ", "+")
    location = location.replace(" ", "+").replace(",", "%2C")

    url = f"{BASE_URL}?q={title}&l={location}"
    return url

def get_jobs(title, location, desired_jobs, sort_by_date=False):
    # Get the driver and setup wait times
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, WAIT_TIME) 

    # Prepare to start looking at jobs
    sort = "&sort=date" if sort_by_date else ""
    url_indeed = lambda x: f"{get_search_page(title, location)}&filter=0{sort}&start={x}"
    list_jobs = []

    # Check how many jobs there are
    driver.get(url_indeed(0))
    num_jobs = int(driver.find_element(By.CLASS_NAME, "jobsearch-JobCountAndSortPane-jobCount").find_element(By.TAG_NAME, 'span').text.split(' ')[0].replace(',', ''))
    if desired_jobs != -1:
        max_jobs = min(desired_jobs, num_jobs)
    else:
        max_jobs = num_jobs
    print(f"Searching for {max_jobs} jobs out of total {num_jobs} jobs found...")

    i = 0
    url = url_indeed(0)
    while True:
        # Get the page
        driver.get(url)
        jobs = driver.find_element(By.ID, "mosaic-provider-jobcards").find_element(By.TAG_NAME, 'ul').find_elements(By.CLASS_NAME, 'job_seen_beacon')

        for j in jobs:
            # Get standard info
            title = j.find_element(By.CLASS_NAME, "jobTitle").find_element(By.TAG_NAME, "span").text
            hyperlink = j.find_element(By.CLASS_NAME, "jobTitle").find_element(By.TAG_NAME, "a").get_attribute("href")
            company = j.find_element(By.CLASS_NAME, "companyName").text
            location = j.find_element(By.CLASS_NAME, "companyLocation").text
            date = j.find_element(By.CLASS_NAME, "date").text.split("\n")[1]

            # Check if there is a salary
            salarySnippet = ""
            salaryContainers = j.find_elements(By.CLASS_NAME, "salary-snippet-container")
            if len(salaryContainers) > 0:
                salarySnippet = salaryContainers[0].find_element(By.TAG_NAME, "div").text
            if salarySnippet == "":
                salaryContainers = j.find_elements(By.CLASS_NAME, "estimated-salary")
                if len(salaryContainers) > 0:
                    salarySnippet = salaryContainers[0].find_element(By.TAG_NAME, "span").text
            
            job = {
                "title": title, 
                "company": company,
                "location": location,
                "salary": salarySnippet,
                "date": date,
                "hyperlink": hyperlink
            }

            list_jobs.append(job)
            i += 1

        # Check exit conditions
        try:
            url = driver.find_element(By.CSS_SELECTOR, '[aria-label="Next Page"]').get_attribute("href")
        except:
            print("Ran out of jobs to find")
            break
        if i >= max_jobs:
            print("Hit jobs limit")
            break
        time.sleep(WAIT_TIME)

    print(f"Found {len(list_jobs)} jobs")
    return list_jobs
