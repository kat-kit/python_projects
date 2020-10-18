#!/bin/bash
DEBUT=2008
FIN=2009

echo "download xls files for years 1csv/year"

  # création des dossiers pour ranger les fichiers
  for ANNEE in `seq $DEBUT $FIN`; do mkdir -p $ANNEE; done
  ./download_region.py  debut=$DEBUT fin=$FIN