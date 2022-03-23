import json
import os

from data import teachers

with open('teachers.json') as f:
    data = json.load(f)
    print(type(data[0]['free']))

