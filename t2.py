import json
import os
desktop_path=os.path.join(os.path.expanduser("~"), "Desktop", "j.txt")
with open(desktop_path, "r", encoding="utf-8") as file:
    data = json.load(file)
print(data)