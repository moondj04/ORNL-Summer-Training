#!/bin/bash

read -p "Enter am acronym: " acronym

if [ "$acronym" = "ASAP" ]; then
    echo "As Soon As Possible";
elif [ "$acronym" = "LCD" ]; then
    echo "Liquid-Crystal Display";
elif [ "$acronym" = "TGIF" ]; then
    echo "Thank George It's Friday";
else
    echo "Sorry, we don't have this acronym..."
fi