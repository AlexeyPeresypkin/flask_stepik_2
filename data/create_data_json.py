import json

from data import teachers, goals

with open('data/teachers.json', 'w') as f:
    json.dump(teachers, f, ensure_ascii=False, indent=4)

with open('data/goals.json', 'w') as f:
    json.dump(goals, f, ensure_ascii=False, indent=4)
