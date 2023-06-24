import os
import json
import yaml


class ConfigConverter:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_dict = {}

    def read_config(self):
        _, ext = os.path.splitext(self.config_file)
        with open(self.config_file, "r") as f:
            if ext == ".yaml":
                self.config_dict = yaml.safe_load(f)
            elif ext in (".cfg", ".conf"):
                self.config_dict = dict(line.strip().split("=") for line in f if "=" in line)

    def to_flat_dict(self, config_dict=None, prefix=""):
        config_dict = config_dict or self.config_dict
        flat_dict = {}
        for key, value in config_dict.items():
            new_prefix = f"{prefix}_{key}" if prefix else key
            if isinstance(value, dict):
                flat_dict.update(self.to_flat_dict(value, new_prefix))
            else:
                flat_dict[new_prefix] = value
        return flat_dict

    def write_to_env(self, env_file):
        with open(env_file, "w") as f:
            for key, value in self.config_dict.items():
                f.write(f"{key}={value}\n")

    def write_to_json(self, json_file):
        with open(json_file, "w") as f:
            json.dump(self.config_dict, f, indent=4)
