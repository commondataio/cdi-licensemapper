# cdi-licensemapper
Data licenses mapping experiments, code and data

This repositry is the part of the Common Data Index project (https://github.com/commondataio)

This repository includes data dumps from Common Data Index database with frequency lists of data licenses ids, urls and names.

Data dumped as tsv files with field names and count of occurences to 'data' directory.

Code as added to the 'scripts' directory. 

## Notes

* ArcGIS Hub, DKAN and Socrata data exported as DCAT 1.1 (dcatus11) with 'license' field
* uData provides 'license' field as abbreviation, more research needed, maybe it could be extracted from source
* from CKAN datasets data fields extracted, not from CKAN license API endpoint. 
* Geonetwork schema is unstable and 'legalContraint' field could be string, dict, or string with "|" delimiter. It's parsed, script added
* InvenioRDM includes multiple rights records, all extracted


## General approach

1. Select most common licenses and create list of licenses with id, name and url for each license
2. Add mapper from license names, urls and id's to most common licenses
3. Create simple Python function to identify license from text provided. Use simple exact text matching rules


## Possible future development

1. Create registry of common licenses in the wild and add idenitifiers linked to OpenDefinition, SPDX, DCAT-AP.de, INSPIRE registry and e.t.c, description, important features
2. Create Python library to identify licenses types using preset of rules
3. Link datasets and data catalogs to certain licenses and usage terms

