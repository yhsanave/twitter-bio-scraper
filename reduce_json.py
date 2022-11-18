import json
import glob

d = {'data': []}

for fp in glob.glob('./raw/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        try:
            d['data'].extend(json.load(f)['data'])
        except:
            print(f'Error parsing {fp}! Make sure the json is formatted correctly (see readme)')

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False)