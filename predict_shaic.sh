#!/usr/bin/env bash

if [[ -z $SHAIC_BASE ]]; then
    SHAIC_BASE= # <path>/shAIC
fi

if [ ! -x dssp ];then
    DSSP=dssp
else
    if [ ! -x mkdssp ];then
        DSSP=mkdssp
    else
        echo "dssp/mkdssp command not found in path"
    fi
fi

if [ "$#" -eq 0 ]; then
    echo "Run as $0 <pdb-file1> (<pdb-file2) ...)"
    exit 1
fi

if [[ -z $SHAIC_BASE ]]; then
    echo "set SHAIC_BASE variable to e.g. <path>/shAIC/"
    exit 1
fi

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

for pdb in "$@";do
    cd $(dirname $pdb)
    # make changes to pdb files to match shaic format
    # and only take first model
    pdbtmp=${pdb%.*}.shaic_tmp
    dssptmp=${pdb%.*}.dssp
    sed -n -e '/ATOM /,$p' $pdb \
        | sed -e '/TER/,$d' \
        | sed -e '/END/,$d' \
        | sed "s@HN@H @" \
        | sed "s@ HT1@1H  @" \
        | sed "s@ HT2@2H  @" \
        | sed "s@ HT3@3H  @" \
        | sed "s@ OT1@ O  @" \
        | sed "s@ OT2@ OXT@" > $pdbtmp
    $DSSP -i $pdbtmp > $dssptmp
    # remove a blank line in dssp file
    sed -e '3d' $dssptmp > "$dssptmp"2 # depends on dssp version

    python2 $SHAIC_BASE/shAIC1_0_0.py $pdbtmp -dssp "$dssptmp"2 -dp $SHAIC_BASE/data/ &> /dev/null
    python2 $SCRIPTPATH/shaic_to_star.py $(ls shAICpredictions_$(basename $pdbtmp .shaic_tmp)?.out | head -n1) $pdbtmp
    rm $pdbtmp
    rm "$dssptmp"*
    rm shAICpredictions*
    cd - >/dev/null
done
