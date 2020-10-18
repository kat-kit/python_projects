#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup
import os
# get the .sh file command arguments ( region, annee de debut, annee de fin)
reg = None
print("region", reg)
debut = None
print("debut", str(debut))
fin = None
print("fin", str(fin))
keys = ["region=", "debut=", "fin="]
for i in range(1, len(sys.argv)):
    if sys.argv[i].find("region=") == 0:
        reg = sys.argv[i][len("region="):]
        print("region", reg)
    if sys.argv[i].find("debut=") == 0:
        debut = int(sys.argv[i][len("debut="):])
        print("debut", str(debut))
    if sys.argv[i].find("fin=") == 0:
        fin = int(sys.argv[i][len("fin="):])
        print("fin", str(fin))

# the url bellow is for json api it can be used later
url = "https://data.economie.gouv.fr/api/records/1.0/search"

# download url is for downloading csv regions files
download_url = "https://data.economie.gouv.fr/explore/dataset/comptes-individuels-des-regions-fichier-global/download"

# download_csv method downloads the csv file from the plateforme , it send request with params to the download API
# and store downloaded file in the appropriate path


def download_csv(annee, region):
    print("get data and return response")
    print("region demandée", region)
    request_params = {"format": "csv",
                      "timezone": "Europe/Berlin",
                      "lang": "fr",
                      "use_labels_for_header": True,
                      "csv_separator": ";"}
    if region is not None:
        request_params["refine.reg"] = str(region)
    if annee is not None:
        request_params["refine.exer"] = str(annee)
    r = requests.get(download_url, params=request_params)
    if annee is not None:
        if reg is None:
            path = str(annee) + \
                '/comptes_individuels_regions_fichiers_' + str(annee) + '.csv'
        else:
            path = str(annee) + '/' + str(region) + \
                '/comptes_individuels_regions_fichiers.csv'
    else:
        if region is None:
            path = 'comptes_individuels_regions_fichiers_global.csv'
        else:
            path = 'regions_data/comptes_individuels_regions_fichiers_region_' + \
                str(region) + '.csv'
    print("path to data", path)
    open(path, 'wb').write(r.content)


if debut is not None and fin is not None:
    for annee in range(debut, fin+1):
        download_csv(annee, reg)
else:
    download_csv(None, reg)
