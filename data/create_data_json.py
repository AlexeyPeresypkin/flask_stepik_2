import json

from data.data import teachers, goals

with open('teachers.json', 'w') as f:
    json.dump(teachers, f, ensure_ascii=False, indent=4)

with open('goals.json', 'w') as f:
    json.dump(goals, f, ensure_ascii=False, indent=4)
