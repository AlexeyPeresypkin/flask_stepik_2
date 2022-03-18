import json
from pprint import pprint

from data.data import teachers, goals

# with open('data/teachers.json', 'w') as f:
#     json.dump(teachers, f, ensure_ascii=False)
#
#
# with open('data/goals.json', 'w') as f:
#     json.dump(goals, f, ensure_ascii=False)


with open('data/teachers.json') as f:
    file = json.load(f)
    pprint(file[1])
