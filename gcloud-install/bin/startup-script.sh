#!/bin/bash
echo "This thing happened."

yum -y install httpd
systemctl enable httpd
systemctl start httpd
#Gets HTTPd started and installed.
