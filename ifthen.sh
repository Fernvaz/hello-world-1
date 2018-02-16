#!/bin/bash
if [ -e /var/www/html/index.html ]; then                      #Checks for the existence of index.html. 
  exit 0;                                                     #Exits the program "successfully".
fi
