import sys
import csv
import os
from pymongo import MongoClient
import typer

app = typer.Typer()

def dict2csv(data, headers, filename, limit=None):
  f = open(filename, 'w', encoding='utf8')
  writer = csv.writer(f, delimiter='\t')
  writer.writerow(headers)
  output = sorted(data.items(), key=lambda x: x[1], reverse=True)  
  writer.writerows(output)
  f.close()


RIGHTS_KEYS = ['dc.rights.uri', 'dc.rights', 'dc.rights.license', 'dcterms.rights', 'gro.rights.copyright', 'dcterms.license', 'dc.rights.copyright', 'dc.rights.accessRights', 'dc.rights.label', 'dc.rights.accessrights', 'europeana.rights', 'dc.rights.url']


@app.command()
def run():
  data_keys = {} 
  for key in RIGHTS_KEYS:
      data_keys[key] = {}
  client = MongoClient()
  db = client['cdidatacommon']
  coll = db['dspace']
  n = 0
  total = coll.count_documents({})
  for record in coll.find():
    record = record['record']    
    n += 1
    if n % 10000 == 0:
      print('Processed %d of %d (%0.2f%%)' % (n, total, n * 100.0/total))
    if not isinstance(record, dict): continue
    if 'metadata' in record.keys():
      for metarec in record['metadata']:
          if metarec['key'] in RIGHTS_KEYS:
              k = metarec['key']
              v = metarec['value']
              d = data_keys[k].get(v, 0)      
              data_keys[k][v] = d + 1
  for key in data_keys.keys():      
      dict2csv(data_keys[key], ['name', 'value'], '../data/dspace_%s.csv' % (key.replace('.', '_')))

if __name__ == "__main__":
  app()