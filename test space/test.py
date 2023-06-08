for num in page_num:
    bottom_ten = f'https://api.builtin.com/services/job-retrieval/legacy-collapsed-jobs?categories=147&subcategories=&experiences=&industry=&company_sizes=&regions=&locations=&remote=&working_option=&per_page=10&page={num}&search=&sortStrategy=recency&job_locations=&company_locations=&jobs_board=true&hybridEnabled=false&national=true'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Vary': 'Accept-Encoding'
    }
    link_two = data_scraper(bottom_ten, head=headers)
    print ('On page:', num)
    for i in range(len(link_two['company_jobs'])):
        # Scraping company information
        alias = link_two['company_jobs'][i]['company']['alias']
        company_perks = link_two['company_jobs'][i]['company']['company_perks']
        elite = link_two['company_jobs'][i]['company']['elite']
        high_volume_poster = link_two['company_jobs'][i]['company']['high_volume_poster']
        company_id = link_two['company_jobs'][i]['company']['id']
        job_slots = link_two['company_jobs'][i]['company']['job_slots']
        limited_listing = link_two['company_jobs'][i]['company']['limited_listing'] if link_two['company_jobs'][i]['company']['limited_listing'] in [True, False] else None
        try:
            locations = [link_two['company_jobs'][i]['company']['locations'][indx]['seo_name'] for indx in range(len(link_two['company_jobs'][i]['company']['locations']))]
        except:
            locations = None
        premium = link_two['company_jobs'][i]['company']['premium']
        company_title = link_two['company_jobs'][i]['company']['title']
        total_employees = link_two['company_jobs'][i]['company']['total_employees']
        # Scraping Job data
        for job_num in range(len(link_two['company_jobs'][i]['jobs'])):
          job_alias = link_two['company_jobs'][i]['jobs'][job_num]['alias']
          job_description = link_two['company_jobs'][i]['jobs'][job_num]['body']
          category_ids = link_two['company_jobs'][i]['jobs'][job_num]['category_id']
          company_id = link_two['company_jobs'][i]['jobs'][job_num]['company_id']
          company_size = link_two['company_jobs'][i]['jobs'][job_num]['company_size']
          easy_apply = link_two['company_jobs'][i]['jobs'][job_num]['easy_apply']
          yrs_experience = link_two['company_jobs'][i]['jobs'][job_num]['experience_level']
          hot_job_score = link_two['company_jobs'][i]['jobs'][job_num]['hot_jobs_score']
          apply_link = link_two['company_jobs'][i]['jobs'][job_num]['how_to_apply']
          hybrid = link_two['company_jobs'][i]['jobs'][job_num]['hybrid']
          job_id = link_two['company_jobs'][i]['jobs'][job_num]['id']
          industry_id = link_two['company_jobs'][i]['jobs'][job_num]['industry_id']
          is_national = link_two['company_jobs'][i]['jobs'][job_num]['is_national']
          original_location = link_two['company_jobs'][i]['jobs'][job_num]['original_location']
          remote = link_two['company_jobs'][i]['jobs'][job_num]['remote']
          remote_status = link_two['company_jobs'][i]['jobs'][job_num]['remote_status']
          salary_max = link_two['company_jobs'][i]['jobs'][job_num]['salary_max']
          salary_min = link_two['company_jobs'][i]['jobs'][job_num]['salary_min']
          salary_single_value = link_two['company_jobs'][i]['jobs'][job_num]['salary_single_value']
          salary_type = link_two['company_jobs'][i]['jobs'][job_num]['salary_type']
          sort_date = link_two['company_jobs'][i]['jobs'][job_num]['sort_job']
        try:
            targeted_remote_locations = [link_two['company_jobs'][i]['jobs'][job_num]['targeted_remote_locations'][indx]['seo_name'] for indx in range(len(link_two['company_jobs'][i]['targeted_remote_locations']))]
        except:
            targeted_remote_locations = None
        job_title = link_two['company_jobs'][i]['jobs'][job_num]['title']
        working_options = link_two['company_jobs'][i]['jobs'][job_num]['working_option']
        job_info = {
            'alias': alias,
            'elite': elite,
            'high_volume_poster': high_volume_poster,
            'company_id': company_id,
            'job_slots': job_slots,
            'limited_listing': limited_listing,
            'locations': locations,
            'premium': premium,
            'company_title': company_title,
            'total_employees': total_employees,
            'job_alias': job_alias,
            'job_description': job_description,
            'category_id': category_ids,
            'company_id': company_id,
            'company_size': company_size,
            'easy_apply': easy_apply,
            'yrs_experience': yrs_experience,
            'hot_job_score': hot_job_score,
            'apply_link': apply_link,
            'hybrid': hybrid,
            'job_id': job_id,
            'industry_id': industry_id,
            'is_national': is_national,
            'original_location': original_location,
            'remote': remote,
            'remote_status': remote_status,
            'salary_max': salary_max,
            'salary_min': salary_min,
            'salary_single_value': salary_single_value,
            'salary_type': salary_type,
            'sort_date': sort_date,
            'targeted_remote_locations': targeted_remote_locations,
            'job_title': job_title,
            'working_options': working_options
        }
        job_list.append(job_info)

# Was going to use but changed how we moved forward with the project
# Page converting to the numbers from the number of pages
def page_converter (dictionary_values):
    new_pages = []
    for page_num in dictionary_values['top_three']:
        top_three_url = f'https://api.builtin.com/services/job-retrieval/legacy-jobs?categories=147&subcategories=&experiences=&industry=&company_sizes=&regions=&locations=&remote=&per_page=3&page={page_num}&search=&sortStrategy=recency&job_locations=&company_locations=&jobs_board=true&elite=true&national=true'
        new_pages.append(top_three_url)
    for page_num in dictionary_values ['bottom_ten']:
        bottom_ten_url = f'https://api.builtin.com/services/job-retrieval/legacy-collapsed-jobs?categories=147&subcategories=&experiences=&industry=&company_sizes=&regions=&locations=&remote=&working_option=&per_page=10&page={page_num}&search=&sortStrategy=recency&job_locations=&company_locations=&jobs_board=true&hybridEnabled=false&national=true'
        new_pages.append(bottom_ten_url)
    return new_pages

# Running the links through a for loop to gather job data
def extracting_data (new_url):
    print ('\nEXTRACTING DATA...')
    bool_value = 'per_page=10'
    for url in new_url:
        if bool_value in url:
            print (url, '\n')






            # Scraping company information
            try:
                alias = link_two['company_jobs'][i]['company']['alias']
            except:
                alias = None
            try:
                company_perks = link_two['company_jobs'][i]['company']['company_perks']
            except:
                company_perks = None
            try:
                elite = link_two['company_jobs'][i]['company']['elite']
            except:
                elite = None
            try:
                high_volume_poster = link_two['company_jobs'][i]['company']['high_volume_poster']
            except:
                high_volume_poster = None
            try:
                company_id = link_two['company_jobs'][i]['company']['id']
            except:
                company_id = None
            try:
                job_slots = link_two['company_jobs'][i]['company']['job_slots']
            except:
                job_slots = None
            try:
                limited_listing = link_two['company_jobs'][i]['company']['limited_listing']
            except:
                limited_listing = None
            try:
                locations = [link_two['company_jobs'][i]['company']['locations'][indx]['seo_name'] for indx in range(len(link_two['company_jobs'][i]['company']['locations']))]
            except:
                locations = None
            try:
                premium = link_two['company_jobs'][i]['company']['premium']
            except:
                premium = None
            try:
                company_title = link_two['company_jobs'][i]['company']['title']
            except:
                company_title = None
            try:
                total_employees = link_two['company_jobs'][i]['company']['total_employees']
            except:
                total_employees = None
        for job_num in range(len(link_two['company_jobs'][i]['jobs'])):
            # Scraping Job data
            try:
                job_alias = link_two['company_jobs'][i]['jobs'][job_num]['alias']
            except:
                job_alias = None
            try:
                job_description = link_two['company_jobs'][i]['jobs'][job_num]['body']
            except:
                job_description = None
            try:
                category_ids = link_two['company_jobs'][i]['jobs'][job_num]['category_id']
            except:
                category_ids = None
            try:
                company_id = link_two['company_jobs'][i]['jobs'][job_num]['company_id']
            except:
                company_id = None
            try:
                company_size = link_two['company_jobs'][i]['jobs'][job_num]['company_size']
            except:
                company_size = None
            try:
                easy_apply = link_two['company_jobs'][i]['jobs'][job_num]['easy_apply']
            except:
                easy_apply = None
            try:
                yrs_experience = link_two['company_jobs'][i]['jobs'][job_num]['experience_level']
            except:
                yrs_experience = None
            try:
                hot_job_score = link_two['company_jobs'][i]['jobs'][job_num]['hot_jobs_score']
            except:
                hot_job_score = None
            try:
                apply_link = link_two['company_jobs'][i]['jobs'][job_num]['how_to_apply']
            except:
                apply_link = None
            try:
                hybrid = link_two['company_jobs'][i]['jobs'][job_num]['hybrid']
            except:
                hybrid = None
            try:
                job_id = link_two['company_jobs'][i]['jobs'][job_num]['id']
            except:
                job_id = None
            try:
                industry_id = link_two['company_jobs'][i]['jobs'][job_num]['industry_id']
            except:
                industry_id = None
            try:
                is_national = link_two['company_jobs'][i]['jobs'][job_num]['is_national']
            except:
                is_national = None
            try:
                location = link_two['company_jobs'][i]['jobs'][job_num]['location']
            except:
                location = None
            try:
                original_location = link_two['company_jobs'][i]['jobs'][job_num]['original_location']
            except:
                original_location = None
            try:
                remote = link_two['company_jobs'][i]['jobs'][job_num]['remote']
            except:
                remote = None
            try:
                remote_status = link_two['company_jobs'][i]['jobs'][job_num]['remote_status']
            except:
                remote_status = None
            try:
                salary_max = link_two['company_jobs'][i]['jobs'][job_num]['salary_max']
            except:
                salary_max = 0
            try:
                salary_min = link_two['company_jobs'][i]['jobs'][job_num]['salary_min']
            except:
                salary_min = 0
            try:
                salary_single_value = link_two['company_jobs'][i]['jobs'][job_num]['salary_single_value']
            except:
                salary_single_value = 0
            try:
                salary_type = link_two['company_jobs'][i]['jobs'][job_num]['salary_type']
            except:
                salary_type = None
            sort_date = link_two['company_jobs'][i]['jobs'][job_num]['sort_job']
            try:
                targeted_remote_locations = [link_two['jobs'][i]['targeted_remote_locations'][indx]['seo_name'] for indx in range(len(link_two['jobs'][i]['targeted_remote_locations']))]
            except:
                targeted_remote_locations = None
            try:
                job_title = link_two['company_jobs'][i]['jobs'][job_num]['title']
            except:
                job_title = None
            try:
                working_options = link_two['company_jobs'][i]['jobs'][job_num]['working_options']
            except:
                working_options = None