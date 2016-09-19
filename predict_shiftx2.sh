#!/usr/bin/env bash

if [[ -z $SHIFTX_BASE ]]; then
    echo "lal"
    SHIFTX_BASE= # <path>/camshift-1.35/
fi

if [ "$#" -eq 0 ]; then
    echo "Run as $0 <pdb-file1> (<pdb-file2) ...)"
    exit 1
fi

if [[ -z $SHIFTX_BASE ]]; then
    echo "set SHIFTX_BASE variable to e.g. <path>/shiftx2/"
    exit 1
fi

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

THISPWD=$(pwd)

cd $SHIFTX_BASE

for pdb in "$@";do
    PDBPATH=$THISPWD/$(dirname $pdb)
    PDBFILE=$THISPWD/$(dirname $pdb)/$(basename $pdb)
    TEMPDIR=$PDBPATH/${pdb%.*}_tmp_dir
    mkdir $TEMPDIR
    $SHIFTX_BASE/shiftx2.py -e -v -i $PDBFILE -o $PDBFILE\.shiftx2 -f BMRB -a ALL -z $TEMPDIR > /dev/null
    rm -r $TEMPDIR
    cd $THISPWD
    mv $pdb\.sxp ${pdb%.*}.shiftx
    mv $pdb\.shifty ${pdb%.*}.shifty
    mv $pdb\.shiftx2 ${pdb%.*}.shiftx2
done
