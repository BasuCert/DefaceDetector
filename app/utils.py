import os
import yaml

curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))


def get_config(term, section="general"):
    try:
        conf_file = os.path.abspath(os.path.join(curDir, os.pardir)) + '/config.yaml'
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
