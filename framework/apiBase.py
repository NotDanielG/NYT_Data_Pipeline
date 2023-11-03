import requests 
import os
import boto3
import json

class apiBase:
    def __init__(self, config, url, api_key, api_params):
        self.config = config
        self.url = url
        self.save_path = self.get_save_path(config)
        self.endpoint_args = api_params
        self.endpoint_args[self.config['api_key_name']] = api_key

    def execute(self):
        params = '&'.join('='.join((key, value)) for (key, value) in self.endpoint_args.items()) 
        request_url = self.url + params
        response = requests.get(request_url)

        if response.status_code == 200:
            results = json.loads(response.text)['results']
            s3 = boto3.resource('s3')
            s3obj = s3.Object(self.config['bucket_name'], self.config['file_name'])
            s3obj.put(Body=(bytes(json.dumps(results).encode('UTF-8'))))
        
            


    def get_save_path(self):
        return self.config['file_folder'] + self.config['file_path'] + self.config['file_name']
    
    def set_google_variables(self, google_url, google_key):
        self.google_url = google_url
        self.google_key = google_key






        
