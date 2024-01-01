import json
import csv
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


import typer


app = typer.Typer()

MAPPER_FILE = '../data/mapped_v1.tsv'
LIC_FILE = '../reference/commonlicenses.yaml'
RULES_FILE = '../reference/rules.yaml'


@app.command()
def add(text, license_id):
    licenses = {}
    f = open(LIC_FILE, 'r', encoding='utf8')
    licenses_data = yaml.load(f, Loader=Loader)
    f.close()
    for row in licenses_data:
        licenses[row['id']] = row
    
    rules  = {}
    f = open(RULES_FILE, 'r', encoding='utf8')
    rules_data = yaml.load(f, Loader=Loader)
    f.close()
    for row in rules_data:
        rules[row['text']] = row

    if license_id not in licenses.keys():
        print('Unknown license type %s. Please add it to common licenses file' % (license_id))
        return
    if text in rules.keys():
       license = licenses[rules[text]['id']]
       print('Already has license id: %s, name: %s for text - %s' % (license['id'], license['name'], text))
    else:
       rules_data.append({'id' : license_id, 'text' : text})
       f = open(RULES_FILE, 'w', encoding='utf8')
       f.write(yaml.dump(rules_data, Dumper=Dumper))
       f.close()
       print('Added %s with license id %s' % (text, license_id))
 

@app.command()
def find_missing():
    """Identifiers which licenses in mapped file missing in the reference registry"""
    lic_ids = []

    f = open(LIC_FILE, 'r', encoding='utf8')
    licenses = yaml.load(f, Loader=Loader)
    f.close()
    for lic in licenses:
        lic_ids.append(lic['id'])

    unmapped = []
    f = open(MAPPER_FILE, 'r', encoding='utf8')
    reader = csv.DictReader(f, delimiter='\t') 
    for row in reader:
        if row['id'] not in lic_ids:
            if row['id'] not in unmapped:
                unmapped.append(row['license_id'])
    f.close()

    print(unmapped)

@app.command()
def convert():
    """Convert mapped data to yaml rules"""
    data = []
    texts = []
    f = open(MAPPER_FILE, 'r', encoding='utf8')
    reader = csv.DictReader(f, delimiter='\t') 
    for row in reader:
        if row['text'] in texts: continue
        texts.append(row['text'])
        data.append({'text': row['text'], 'id' : row['id']})
    f.close()
    f = open(RULES_FILE, 'w', encoding='utf8')
    f.write(yaml.dump(data, Dumper=Dumper))
    f.close()

@app.command()
def identify(text):
    """Identifies license by text provided. Very slow and ineffective. Temporary solution test license mapping for Common Data Index"""
    licenses = {}
    f = open(LIC_FILE, 'r', encoding='utf8')
    licenses_data = yaml.load(f, Loader=Loader)
    f.close()
    for row in licenses_data:
        licenses[row['id']] = row
    
    rules  = {}
    f = open(RULES_FILE, 'r', encoding='utf8')
    rules_data = yaml.load(f, Loader=Loader)
    f.close()
    for row in rules_data:
        rules[row['text']] = row

    if text in rules.keys():
       license = licenses[rules[text]['id']]
       print('License id: %s, name: %s for text - %s' % (license['id'], license['name'], text))
    else:
       print('License not found')

if __name__ == "__main__":
    app()