from abc import ABC, abstractmethod

class apiBase(ABC):
    def __init__(self, config, url, api_key, api_params, google_api_key):
        self.config = config
        self.url = url
        self.save_path = self.get_save_path(config)
        self.endpoint_args = api_params
        self.endpoint_args[self.config['api_key_name']] = api_key

    @abstractmethod
    def run(self):
        self.before_execute()
        self.execute()
        self.after_execute()

    @abstractmethod
    def execute_api(self):
        pass

    @abstractmethod
    def before_execute(self):
        pass

    @abstractmethod
    def after_execute():
        pass