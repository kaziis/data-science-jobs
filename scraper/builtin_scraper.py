# Build a scraper that collects data on Data Science related jobs

from bs4 import BeautifulSoup
import requests
import json
import time
import pandas as pd
import datetime

print ('\nPROGRAM IS RUNNING')
print ('-----------------------------------------------------------------------------------------------------')

def log_file():
    f = open(r'C:\Users\kazir\OneDrive\Desktop\Github\Data_Science\DS_JOBS\Logs\log.txt', 'a')
    f.write(f"\nThe scraper ran on {datetime.datetime.now().strftime('%B %d, %Y at %I:%M:%S %p')}")
    print('The scraper finished running and added a new record onto the log file.\n')
    f.close()

# Build the scraper
def data_scraper (company_section, head):
    while True:
        response = requests.get(company_section, headers=head)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            json_data = json.loads(soup.text)
            break
    time.sleep(.5)
    return json_data

# Gathering the number of pages
def number_of_pages():
    dict_value = {
        'top_three': [''],
        'bottom_ten': ['']
        }
    print ('GATHERING PAGE NUMBERS')
    page_num = 0 # Set this to zero to start from page 0
    while True:
        top_three = f'https://api.builtin.com/services/job-retrieval/legacy-jobs?categories=147&subcategories=&experiences=&industry=&company_sizes=&regions=&locations=&remote=&per_page=3&page={page_num}&search=&sortStrategy=recency&job_locations=&company_locations=&jobs_board=true&elite=true&national=true'
        bottom_ten = f'https://api.builtin.com/services/job-retrieval/legacy-collapsed-jobs?categories=147&subcategories=&experiences=&industry=&company_sizes=&regions=&locations=&remote=&working_option=&per_page=10&page={page_num}&search=&sortStrategy=recency&job_locations=&company_locations=&jobs_board=true&hybridEnabled=false&national=true'
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
        if len(data_scraper(top_three, head=headers)['companies']) != 0:
            dict_value['top_three'].append(page_num)
        if len(data_scraper(bottom_ten, head=headers)['company_jobs']) != 0:
            dict_value['bottom_ten'].append(page_num)
        if len(data_scraper(top_three, head=headers)['companies']) == len(data_scraper(bottom_ten, head=headers)['company_jobs']):
            break
        print ('PAGE:', page_num)
        print (f"LINK 1 -> {len(data_scraper(top_three, head=headers)['companies'])} JOBS FOUND")
        print (f"LINK 2 -> {len(data_scraper(bottom_ten, head=headers)['company_jobs'])} JOBS FOUND")
        print ('-----------------------------------------------------------------------------------------------------')
        page_num += 1
    print ('All pages found!\n')
    return dict_value

def try_except_block (company_fields, job_fields, company_section, job_section):
    data_builder = {}
    for field in company_fields:
        if field == 'locations':
            try:
                data_builder[field] = [company_section[field][L]['seo_name'] for L in range(len(company_section[field]))]
            except:
                data_builder[field] = None
        else:
            try:
                data_builder[field] = company_section[field]
            except:
                data_builder[field] = None
    for job_field in job_fields:
        if job_field == 'targeted_remote_locations':
            try:
                data_builder[job_field] = [job_section[job_field][L]['seo_name'] for L in range(len(job_section[job_field]))]
            except:
                data_builder[job_field] = None
        elif job_field == 'sort_job':
            try:
                data_builder[job_field] = datetime.datetime.strptime(job_section[job_field], '%Y-%m-%dT%H:%M:%S')
            except:
                data_builder[job_field] = datetime.datetime.strptime(job_section[job_field], '%a, %d %b %Y %H:%M:%S %Z')
        else:
            if job_field == 'alias':
                try:
                    data_builder['job_alias'] = job_section[job_field]
                except:
                    data_builder[job_field] = None
            elif job_field == 'id':
                try:
                    data_builder['job_id'] = job_section[job_field]
                except:
                    data_builder[job_field] = None
            elif job_field == 'title':
                try:
                    data_builder['job_title'] = job_section[job_field]
                except:
                    data_builder[job_field] = None
            else:
                try:
                    data_builder[job_field] = job_section[job_field]
                except:
                    data_builder[job_field] = None
    return data_builder

def main ():
    job_list = []
    num_pages = number_of_pages()
    print ('PROCESSING LINK 1')
    for num in num_pages['top_three']:
        top_three = f'https://api.builtin.com/services/job-retrieval/legacy-jobs?categories=147&subcategories=&experiences=&industry=&company_sizes=&regions=&locations=&remote=&per_page=3&page={num}&search=&sortStrategy=recency&job_locations=&company_locations=&jobs_board=true&elite=true&national=true'
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
        link_one = data_scraper(top_three, head=headers)
        for i in range(len(link_one['companies'])):
            companies_fields = ['alias', 'company_perks', 'elite', 'high_volume_poster', 'id', 'job_slots', 'limited_listing', 'locations',
                                'premium', 'title', 'total_employees']
            job_fields = ['alias', 'body', 'category_id', 'company_id', 'company_size', 'easy_apply', 'experience_level', 'hot_jobs_score',
                            'how_to_apply', 'hybrid', 'id', 'industry_id', 'is_national', 'location', 'original_location', 'remote',
                            'remote_status', 'salary_max', 'salary_min', 'salary_single_value', 'salary_type', 'sort_job', 'targeted_remote_locations',
                            'title', 'working_option']
            jobs = try_except_block(companies_fields, job_fields, link_one['companies'][i], link_one['jobs'][i])
            job_list.append(jobs)
            print (f"Last Company Appended: {jobs['title']}")
            print ('-----------------------------------------------------------------------------------------------------')

    print ('PROCESSING LINK 2')
    for num in num_pages['bottom_ten']:
        bottom_ten = f'https://api.builtin.com/services/job-retrieval/legacy-collapsed-jobs?categories=147&subcategories=&experiences=&industry=&company_sizes=&regions=&locations=&remote=&working_option=&per_page=10&page={num}&search=&sortStrategy=recency&job_locations=&company_locations=&jobs_board=true&hybridEnabled=false&national=true'
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
        link_two = data_scraper(bottom_ten, head=headers)
        for i in range(len(link_two['company_jobs'])):
            companies_fields = ['alias', 'company_perks', 'elite', 'high_volume_poster', 'id', 'job_slots', 'limited_listing', 'locations',
                                'premium', 'title', 'total_employees']
            job_fields = ['alias', 'body', 'category_id', 'company_id', 'company_size', 'easy_apply', 'experience_level', 'hot_jobs_score',
                            'how_to_apply', 'hybrid', 'id', 'industry_id', 'is_national', 'location', 'original_location', 'remote',
                            'remote_status', 'salary_max', 'salary_min', 'salary_single_value', 'salary_type', 'sort_job', 'targeted_remote_locations',
                            'title', 'working_option']
            for n_job in range(len(link_two['company_jobs'][i]['jobs'])):
                jobs = try_except_block(companies_fields, job_fields, link_two['company_jobs'][i]['company'], link_two['company_jobs'][i]['jobs'][n_job])
                job_list.append(jobs)
                print (f"Last Company Appended: {jobs['title']}")
                print ('-----------------------------------------------------------------------------------------------------')
    path = f'C:\\Users\\kazir\\OneDrive\\Desktop\\Github\\Data_Science\\DS_JOBS\\CSVs\\DS_jobs_{datetime.datetime.now().strftime("%m%d%Y")}.csv'
    df = pd.DataFrame(job_list)
    df.to_csv(path, index=False)
    print ('All DS Jobs have been scraped.\n')
    log_file()

main()