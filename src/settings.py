import os
import sys
import json


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)


settings_json = f'{SCRIPT_DIR}/settings.json'


try:
    with open(settings_json, 'r') as file:
        settings = json.load(file)
except FileNotFoundError as error:
    raise error