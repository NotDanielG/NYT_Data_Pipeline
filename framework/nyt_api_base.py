import requests 
import os
import boto3
import json
import pandas as pd

class nytApiBase:
    def __init__(self, config, url, api_key, api_params):
        super.__init__(config, url, api_key, api_params)
        self.response_code = 0
        self.isbn_list = []
        self.google_result = []
        self.google_params = self.config['google_params']

    def run(self):
        self.before_execute()
        self.execute()
        self.after_execute()

    def execute(self):
        params = '&'.join('='.join((key, value)) for (key, value) in self.endpoint_args.items()) 
        request_url = self.url + params
        response = requests.get(request_url)

        self.response_code = response.status_code
        if self.response_code == 200:
            results = json.loads(response.text)['results']
            self.save_to_s3(save_content=results, bucket_name=self.config['bucket_name'], save_path=self.get_save_path(self.config['nyt_file_path']))
            self.execute_google_books(results)

    def insert_isbn_list(self, results):
        for book in results:
            if len(book['isbns']) > 0:
                self.isbn_list.insert(book['isbns'][0])

    def execute_google_books(self, results):
        self.insert_isbn_list(results)
        for isbn in self.isbn_list:
            param_string = self.config['google_params'].copy().format(isbn=isbn, api=self.google_key)
            request_url = self.google_url + param_string
            response = requests.get(request_url)

            self.response_code = response.status_code
            if self.response_code == 200:
                results = json.loads(response.text)
                if results['totalItems'] > 0:
                    self.google_result.insert(results['items'][0])
        
        self.save_to_s3(save_content=self.google_result, bucket_name=self.config['bucket_name'], save_path=self.get_save_path(self.config['google_file_path']))
            
    def get_save_path(self, file_path):
        return self.config['file_folder'] + file_path + self.config['file_name']
    
    def save_to_s3(self, save_content, bucket_name, save_path):
        s3 = boto3.resource('s3')
        s3obj = s3.Object(bucket_name, save_path)
        s3obj.put(Body=(bytes(json.dumps(save_content).encode('UTF-8')))) # Saves to S3

    def set_google_variables(self, google_url, google_key):
        self.google_url = google_url
        self.google_key = google_key

    