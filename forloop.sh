#!/bin/bash
for x in $(ls *.conf); do                  #Looks for config files at current location.
cp $x $x.$(date +%F_+%R);                  #Appends date.
done
