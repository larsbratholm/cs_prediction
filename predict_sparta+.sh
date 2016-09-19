#!/usr/bin/env bash

if [[ -z $SPARTAPLUS_BASE ]]; then
    echo "lal"
    SPARTAPLUS_BASE= # <path>/SPARTA+/
fi

if [ "$#" -eq 0 ]; then
    echo "Run as $0 <pdb-file1> (<pdb-file2) ...)"
    exit 1
fi

if [[ -z $SPARTAPLUS_BASE ]]; then
    echo "set SPARTAPLUS_BASE variable to e.g. <path>/SPARTA+/"
    exit 1
fi

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

for pdb in "$@";do
    $SPARTAPLUS_BASE/sparta+ -in $1 -out ${1%.*}\.sparta_tmp &> /dev/null
    python2 $SCRIPTPATH/sparta+_to_star.py ${1%.*}\.sparta_tmp
    rm ${1%.*}\.sparta_tmp
    rm struct.tab
done

