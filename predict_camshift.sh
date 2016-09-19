#!/usr/bin/env bash

if [[ -z $CAMSHIFT_BASE ]]; then
    echo "lal"
    CAMSHIFT_BASE= # <path>/camshift-1.35/
fi

if [ "$#" -le 1 ]; then
    echo "Run as $0 <minimization> <pdb-file1> (<pdb-file2) ...)"
    echo "where <minimization> = {hatoms,all,none,off}"
    exit 1
fi

if [[ -z $CAMSHIFT_BASE ]]; then
    echo "set CAMSHIFT_BASE variable to e.g. <path>/camshift-1.35/"
    exit 1
fi

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
MINI=$1
shift

for pdb in "$@";do
   $CAMSHIFT_BASE/bin/camshift --data $CAMSHIFT_BASE/data/ --pdb $pdb --mini $MINI | python2 $SCRIPTPATH/camshift_to_star.py $pdb
done
