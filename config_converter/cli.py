import argparse
import os
import json
from .converter import ConfigConverter


def parse_args():
    """
    Parse command line arguments for converting configuration files to different formats.
    """
    parser = argparse.ArgumentParser(description="Convert configuration files to different formats")
    parser.add_argument("config_file", help="Path to the configuration file")
    parser.add_argument("--env-file", help="Path to the .env file to write to")
    parser.add_argument("--json-file", help="Path to the JSON file to write to")
    parser.add_argument("--set-env", action="store_true", help="Set environment variables based on the configuration")
    return parser.parse_args()


def write_to_file(file_path, data):
    try:
        with open(file_path, "w") as f:
            f.write(data)
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")


def convert_config(args):
    converter = ConfigConverter(args.config_file)
    converter.read_config()
    flat_dict = converter.to_flat_dict()

    if args.env_file:
        env_data = "\n".join([f"{k}={v}" for k, v in flat_dict.items()])
        write_to_file(args.env_file, env_data)

    if args.json_file:
        json_data = json.dumps(flat_dict, indent=4)
        write_to_file(args.json_file, json_data)

    os.environ.update(flat_dict) if args.set_env else None


def main():
    """
    Runs the program by parsing the arguments and converting the configuration.
    """
    parsed_args = parse_args()
    convert_config(parsed_args)
