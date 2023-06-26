# Config Converter

`config_converter` is a Python package for converting configuration files to different formats. It can read `.yaml`, `.cfg`, and `.conf` configuration files, generate a flat dictionary from the configurations, and write the configurations to `.env` and JSON files, or set the configurations as environment variables.

## Installation

To install `config_converter`, run:

pip install config_converter

## Usage

To use `config_converter`, run the `config_converter` command with the following arguments:

config_converter [CONFIGFILE] [--env-file ENVFILE] [--json-file JSONFILE] [--set-env]

- `CONFIG_FILE`: Path to the configuration file.
- `--env-file ENV_FILE`: Path to the `.env` file to write to.
- `--json-file JSON_FILE`: Path to the JSON file to write to.
- `--set-env`: Set environment variables based on the configuration.

## Example

Suppose you have a configuration file called `config.yaml` with the following contents:

database: host: localhost port: 5432 username: admin password: secret

To generate a flat dictionary from this configuration and write it to an `.env` file, run:

config_converter config.yaml --env-file .env

This will create a `.env` file with the following contents:

DATABASEHOST=localhost  
DATABASEPORT=5432   
DATABASEUSERNAME=admin  
DATABASEPASSWORD=secret

Note: You can customize the README file content as per your requirements.
