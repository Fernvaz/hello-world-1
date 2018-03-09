#!/bin/bash
echo "This is different I promise."

yum -y install httpd
systemctl enable httpd
systemctl start httpd
#Gets HTTPd installed and started.
