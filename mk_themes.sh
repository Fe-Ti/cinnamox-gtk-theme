#!/bin/bash
ICON_THEME='ePapirus'
for i in `ls -x colors/Uti/`
do
    ./change_color.sh colors/Uti/${i} -n ${ICON_THEME} &
done
