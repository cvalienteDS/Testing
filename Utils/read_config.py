import logging
import sys
import yaml
import os

logger = logging.getLogger(__name__)

def read_yaml_config(config_name):
    path = config_name
    try:
        with open(path, 'r') as stream:
            try:
                return yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)
    except FileNotFoundError as ex:
        logger.error("Config not found [{}] on path [{}]".format(config_name, os.path.abspath(path)))
        sys.exit(1)