#!/bin/bash
what=lepMVAFriend
if [[ "$1" != "" ]]; then what=$1; fi
for F in $(ls ${what}*chunk* | sed 's/\.chunk[0-9]\+//' | sort | uniq); do
    if test -f $F; then echo "Merged file $F already exists. skipping."; continue; fi
    FILES=$(ls ${F/.root/.root.chunk*} | \
            perl -npe 's/\.chunk(\d+)\./sprintf(".%06d.",$1)/e' | \
            sort -n | \
            perl -npe 's/\.(\d+)\.root$/sprintf(".chunk%d.root",$1)/e' );
    echo -e "\nWill merge into $F:\n$FILES"; 
    hadd -f $F $FILES
done

