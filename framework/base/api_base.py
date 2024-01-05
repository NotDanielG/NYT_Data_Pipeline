from abc import ABC, abstractmethod

class apiBase(ABC):
    def __init__(self, config, url, api_key, api_params):
        self.config = config
        self.url = url
        self.endpoint_args = api_params
        self.endpoint_args[self.config['api_key_name']] = api_key

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def before_execute(self):
        pass

    @abstractmethod
    def after_execute():
        pass