import json
import pytest
from config_converter.converter import ConfigConverter


@pytest.fixture
def cfg_file(tmpdir):
    cfg = tmpdir.join("config.cfg")
    cfg.write("host=localhost\nport=5432\nusername=admin\npassword=secret")
    return str(cfg)


@pytest.fixture
def yaml_file(tmpdir):
    yaml = tmpdir.join("config.yaml")
    yaml.write("database:\n  host: localhost\n  port: 5432\n  username: admin\n  password: secret")
    return str(yaml)


class TestConfigConverter:
    def test_read_config_from_cfg_file(self, cfg_file):
        converter = ConfigConverter(cfg_file)
        converter.read_config()
        assert converter.config_dict == {
            "host": "localhost",
            "port": "5432",
            "username": "admin",
            "password": "secret"
        }

    def test_read_config_from_yaml_file(self, yaml_file):
        converter = ConfigConverter(yaml_file)
        converter.read_config()
        assert converter.config_dict == {
            "database": {
                "host": "localhost",
                "port": 5432,
                "username": "admin",
                "password": "secret"
            }
        }

    def test_to_flat_dict(self):
        converter = ConfigConverter("")
        converter.config_dict = {
            "DATABASE": {
                "HOST": "localhost",
                "PORT": 5432,
                "USERNAME": "admin",
                "PASSWORD": "secret"
            },
            "SERVER": {
                "HOST": "localhost",
                "PORT": 8080
            }
        }
        flat_dict = converter.to_flat_dict()
        assert flat_dict == {
            "DATABASE_HOST": "localhost",
            "DATABASE_PORT": 5432,
            "DATABASE_USERNAME": "admin",
            "DATABASE_PASSWORD": "secret",
            "SERVER_HOST": "localhost",
            "SERVER_PORT": 8080
        }

    def test_write_to_env(self, tmpdir):
        env_file = str(tmpdir.join(".env"))
        converter = ConfigConverter("")
        converter.config_dict = {
            "DATABASE_HOST": "localhost",
            "DATABASE_PORT": 5432,
            "DATABASE_USERNAME": "admin",
            "DATABASE_PASSWORD": "secret"
        }
        converter.write_to_env(env_file)
        with open(env_file, "r") as f:
            contents = f.read()
        assert contents == "DATABASE_HOST=localhost\nDATABASE_PORT=5432\nDATABASE_USERNAME=admin\nDATABASE_PASSWORD=secret\n"

    def test_write_to_json(self, tmpdir):
        json_file = str(tmpdir.join("config.json"))
        converter = ConfigConverter("")
        converter.config_dict = {
            "DATABASE_HOST": "localhost",
            "DATABASE_PORT": 5432,
            "DATABASE_USERNAME": "admin",
            "DATABASE_PASSWORD": "secret"
        }
        converter.write_to_json(json_file)
        with open(json_file, "r") as f:
            contents = json.load(f)
        assert contents == {
            "DATABASE_HOST": "localhost",
            "DATABASE_PORT": 5432,
            "DATABASE_USERNAME": "admin",
            "DATABASE_PASSWORD": "secret"
        }
