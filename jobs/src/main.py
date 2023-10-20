from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time

import company
import job
import filter as filt

POSITIONS = ["Machine Learning Engineer", "Software Engineer"]
LOCATIONS = ["Reading, PA", "Remote"]
DESIRED_NUM_JOBS = 10
SAVE_DIR = "../jobs/"


def save_df(df, position, location, version):
    filename = f"{SAVE_DIR}/jobs-checkpoint-{version}-{position}-{location}.csv"
    print(f"Saving {version} df to {filename}")
    df.to_csv(filename, index=False)


def get_jobs_as_df(list_jobs):
    # Save jobs to df
    df = pd.DataFrame(list_jobs)
    df = df.drop_duplicates()
    print(f"Found {df.shape[0]} unique jobs. Found {len(list_jobs)} total good jobs.")
    return df


def main():
    # Set position and location
    position = POSITIONS[0]
    location = LOCATIONS[1]

    # Get jobs
    jobs = job.get_jobs(position, location, DESIRED_NUM_JOBS, sort_by_date=False)
    jobs = filt.filter_out_titles(jobs)

    # Save jobs to df
    df = get_jobs_as_df(jobs)
    save_df(df, position, location, "indeed")

    # Add in company information
    df = company.add_company_info(df)
    save_df(df, position, location, "glassdoor")

    print("Completed Job Search...")

if __name__ == "__main__":
    main()
