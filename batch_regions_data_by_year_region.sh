#!/bin/bash
#declare periode from DEBUT to FIN
DEBUT=2008
FIN=2008

#get data by regions and year
echo "download xls files for different regions 1csv/year/region"

#declare regions array
declare -a regions=("011" "024" "052" "053" "093" "101" "104" "094" "021" "022" "023" "025" "026" "031" "041" "042" "043" "054" "072" "073" "074" "082" "083" "091" "102" "103" "027" "028" "032" "044" "075" "076" "084")
for REG in "${regions[@]}"
do
  # création des dossiers pour ranger les fichiers
  for ANNEE in `seq $DEBUT $FIN`; do mkdir -p $ANNEE/$REG; done
  ./download_region.py region=$REG debut=$DEBUT fin=$FIN

done

#get all data without any search cretaria
echo "download global 1csv"
./download_region.py

