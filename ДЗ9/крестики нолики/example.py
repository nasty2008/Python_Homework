import json

def get_data():
    with open ('file.json', 'r', encoding= 'utf-8') as f:
        elems = json.load(f)
        return elems