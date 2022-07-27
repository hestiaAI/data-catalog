#!/bin/bash

#File: tree-md

treep=$(tree -f -L 3 --noreport -I '*~|README.md|*emplate*|tree-md.sh' --charset ascii $1 | sed -e 's/| \+/  /g' -e 's/[|`]-\+/ */g' -e 's:\(* \)\(\(.*/\)\([^/]\+\)\):\1[\4](\2):g')

printf "${treep}\n"
