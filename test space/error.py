
# json.decoder.JSONDecodeError: Expecting value: line 7 column 1 (char 8)

from bs4 import BeautifulSoup
import requests
import json
import time
import pandas as pd
import datetime




print ('\nSCRAPER HAS STARTED')
print ('-----------------------------------------------------------------------------------------------------')
# Build the scraper
def data_scraper (url, headers):
    json_data = requests.get(url, headers=headers).json()
    time.sleep(1)
    return json_data

pages = ['']
for page_num in range(len(pages)):
    top_three = f'https://api.builtin.com/services/job-retrieval/legacy-jobs?categories=147&subcategories=&experiences=&industry=&company_sizes=&regions=&locations=&remote=&per_page=3&page={page_num}&search=&sortStrategy=recency&job_locations=&company_locations=&jobs_board=true&elite=true&national=true'
    bottom_ten = f'https://api.builtin.com/services/job-retrieval/legacy-collapsed-jobs?categories=147&subcategories=&experiences=&industry=&company_sizes=&regions=&locations=&remote=&working_option=&per_page=10&page={page_num}&search=&sortStrategy=recency&job_locations=&company_locations=&jobs_board=true&hybridEnabled=false&national=true'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Vary': 'Accept-Encoding'
    }
    print (data_scraper(top_three, headers))
    # print (data_scraper(bottom_ten))