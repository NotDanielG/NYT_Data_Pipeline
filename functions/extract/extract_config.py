import datetime 

def get_extract_config():
    return {
        's3_bucket': 'nyt-bestsellers-data',
        'file_folder:' 'raw/'
        'nyt_file_path': '{source}/{type}/{year}/{week}',
        'file_name': '/data.json',
        'api_key_name': '{key}',
        'google_params': 'isbn:{isbn}&key={api}',
        'google_file_path': '{source}/{type}/{year}/{week}'
    }

def get_urls():
    return {
        'nyt_list_specific': 'https://api.nytimes.com/svc/books/v3/lists.json?',
        'google_books': 'https://www.googleapis.com/books/v1/volumes?q='
    }

