# json_example.py
import json

data = {"title": "Учебная задача", "completed": False}
text = json.dumps(data, ensure_ascii=False, indent=2)
restored = json.loads(text)
assert restored == data
print(text)
