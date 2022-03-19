import json
from pprint import pprint

from data.data import teachers, goals

with open('teachers.json', 'w') as f:
    json.dump(teachers, f, ensure_ascii=False)


with open('goals.json', 'w') as f:
    json.dump(goals, f, ensure_ascii=False)
