import json
import os
from calculation_utils import get_datetime_from_weeknum
from framework import apiBase
import extract_config

def index(event, context):
    year = event['year']
    week = event['week']
    
    query_params = event['nyt_params'] # listname, bestsellers-date, api-key
    date = get_datetime_from_weeknum(year=year, week=week)
    query_params['bestsellers-date'] = date

    nyt_api_key = os.environ.get('NYT_API_KEY')
    google_api_key = os.environ.get('GOOGLE_API_KEY')

    config = extract_config.get_extract_config()
    nyt_url = extract_config.get_urls()['nyt_list_specific']
    google_books_url = extract_config.get_urls()['google_books']

    config['nyt_file_path'] = config['file_path'].format(source='new-york-times', type='list', year=year, week=week)
    config['google_file_path'] = config['google_file_path'].format(source='google-books', type='list', year=year, week=week)
    config['results_key'] = config['results_key_name'].format(key='results')
    
    extractApi = apiBase(config = config, url=nyt_url, api_key=nyt_api_key, api_params=query_params)
    extractApi.set_google_variables(google_books_url, google_api_key)

    response = {
        "statusCode": extractApi.response_code
    }

    return response
