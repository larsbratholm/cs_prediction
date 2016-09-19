#!/usr/bin/env bash

if [[ -z $PHAISTOS_BUILD ]]; then
    PHAISTOS_BUILD= # <path>/phaistos/build/
fi

if [ "$#" -eq 0 ]; then
    echo "Run as $0 <ProCS datafolder> <pdb-file1> (<pdb-file2) ...)"
    exit 1
fi

if [[ -z $PHAISTOS_BUILD ]]; then
    echo "set PHAISTOS_BUILD variable to e.g. <path>/phaistos/build/"
    exit 1
fi


if [ ! -x $PHAISTOS_BUILD/test/procs15_predictor ];then
    echo "procs15_predictor not found. compile with 'make procs15_predictor' from $PHAISTOS_BUILD"
    exit 1
fi

PROCS_DATAFOLDER=$1
shift
FILES=$(for i in "$@";do echo ${i%.*}.pdb;done)

# set debug to 1 for detailed output
$PHAISTOS_BUILD/test/procs15_predictor --data-folder $PROCS_DATAFOLDER --pdb-files $FILES \
--debug 0

