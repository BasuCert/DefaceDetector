import os
import yaml


def get_parent_path(file_path):
    curfilePath = os.path.abspath(file_path)
    curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))
    return os.path.abspath(os.path.join(curDir, os.pardir))


def get_config(term, section="general"):
    try:
        conf_file = get_parent_path(__file__) + '/config.yaml'
        with open(conf_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
    except FileNotFoundError:
        print("file not found")
        return {}
    try:
        return cfg.get(section, {}).get(term, {})
    except KeyError:
        print("key not found")
        return {}
