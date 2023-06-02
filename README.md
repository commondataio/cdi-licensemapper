# cdi-licensemapper
Data licenses mapping experiments, code and data


This repository includes data dumps from Common Data Index database with frequency lists of data licenses ids, urls and names.

Data dumped as tsv files with field names and count of occurences to 'data' directory.

Code as added to the 'scripts' directory. 


## Notes

* ArcGIS Hub, DKAN and Socrata data exported as DCAT 1.1 (dcatus11) with 'license' field
* uData provides 'license' field as abbreviation, more research needed, maybe it could be extracted from source
* from CKAN datasets data fields extracted, not from CKAN license API endpoint. 
* Geonetwork schema is unstable and 'legalContraint' field could be string, dict, or string with "|" delimiter. It's parsed, script added
* InvenioRDM include multiple rights records, all extracted


