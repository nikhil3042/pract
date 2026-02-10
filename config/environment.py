import yaml
import os

class Environment:
    def __init__(self, env_name):
        self.env = env_name
        self._config = self._load_config()
        self._validate_env() # im calling that method in init so itll check first and then later methods are run

    def _load_config(self):
        config_path = os.path.join(os.getcwd(), "config", "config.yaml")
        with open(config_path, "r") as file:
            return yaml.safe_load(file)

    def get_base_url(self):
        return self._config["environments"][self.env]["base_url"]

    def get_username(self):
        return self._config["environments"][self.env]["username"]

    def get_password(self):
        return self._config["environments"][self.env]["password"]

    def _validate_env(self): #this will check if env is there in yaml or not
        if self.env not in self._config["environments"]:
            raise ValueError(f"Environment '{self.env}' not found in config.yaml")
