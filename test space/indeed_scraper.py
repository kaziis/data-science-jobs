# Build a indeed scraper searching for all data scientist jobs in the United States

from bs4 import BeautifulSoup
import requests as r
import time
from selenium import webdriver

# Initialize the link for indeed and understand how pages are changed as you scroll down
page_number = 1
url = f'https://www.ziprecruiter.com/jobs-search?search=Data+Science&location=United+States&page={page_number}&impression_superset_id=CFRAY%3A7a1b8c9a7020efe9-IAD'

agent = {'user_agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

# Create scraper
def web_scraper (url):
    driver = webdriver.Chrome(r"...\OneDrive\Documents\Chrome Driver\chromedriver.exe")
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    time.sleep(5)
    return soup

links = [url]
while web_scraper(url).find_all('link', rel="next"):
    for link in web_scraper(url).find_all('link', rel="next"):
        links.append(link['href'])
        url = link['href']
    print (f"Link has been appended. Total Links: {len(links)}")
print (links)