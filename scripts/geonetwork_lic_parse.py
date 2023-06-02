import json

def unpack_lic():
   f = open('../data/geonetwork_licenses.jsonl', 'r', encoding="utf8")
   fout = open('../data/geonetwork_licenses_unpacked.jsonl', 'w', encoding="utf8")
   n = 0
   for line in f:
      document = json.loads(line)   
      if not isinstance(document['record'], dict): continue
      if 'legalConstraints' not in document['record'].keys(): continue
      if isinstance(document['record']['legalConstraints'], str):
         arr = [document['record']['legalConstraints']]
      else:
         arr = document['record']['legalConstraints']
      if arr is None: continue
      for legal in arr:
         item = None
         if isinstance(legal, dict):
             item = {}
             if 'name' in legal.keys(): item['title'] = legal['name']
             if 'url' in legal.keys(): item['link'] = legal['url']
         elif isinstance(legal, str):
             if legal[0:5] == 'link|':
                parts = legal.split('|')
                item = {'title' : parts[2], 'link' : parts[1]}
             else:
                item = {'title' : legal}       
         if item is not None:
             fout.write(json.dumps(item) + '\n')
         else:
             print(legal)
      n += 1
      if n % 1000 == 0:
         print(n)

if __name__ == "__main__":
    unpack_lic()