#!/bin/bash
#create regions_data folder to store all downloaded xls files for regions
REGIONS_FOLDER="regions_data";
mkdir -p $REGIONS_FOLDER;

#declare regions array
declare -a regions=("011" "024" "052" "053" "093" "101" "104" "094" "021" "022" "023" "025" "026" "031" "041" "042" "043" "054" "072" "073" "074" "082" "083" "091" "102" "103" "027" "028" "032" "044" "075" "076" "084")
for REG in "${regions[@]}"
do
echo "download xls files for regions 1csv/region"
  # création des dossiers pour ranger les fichiers
 ./download_region.py  region=$REG
done