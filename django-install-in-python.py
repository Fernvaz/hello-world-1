#!/usr/bin/python
import os

def django_setup():
  os.system('sudo yum install python-pip -y')
  os.system('sudo pip install virtualenv')
  os.system('sudo pip install --upgrade pip')
  os.system('sudo mkdir /opt/django')
  os.chdir('/opt/django')

  os.system('sudo yum install epel-release -y')
  os.system('sudo yum install python34 python-pip -y')

def django_install():
  os.system('sudo virtualenv -p python3 django')
  os.chdir('/opt/django/django')
  os.system('source /opt/django/django/bin/activate && pip install django')

  os.system('django-admin startproject project1')

  os.chdir('..')
  os.system('sudo chown -R tjense04 /opt/django')
  os.system('yum install git -y')



  os.system('myip=$( curl ifconfig.co ) && sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS =  \[\'"$myip"\'\]/g" /opt/django/django/project1/project1/settings.py ')
  #Gets global IP address and stores it.
  #First, we define myip as the curled result of an external IP grabber.
  #Stream editor (sed) statement: -i is insert. Use of "\" slashes is called escaping.
  # s/ tells sed to search for the given term.

def django_start():
#  os.system('sudo -u tjense04 virtualenv -p python3 django')
  os.chdir('/opt/django/django')
  os.system('sudo -u tjense04 -E sh -c "source /opt/django/django/bin/activate && /opt/django/django/project1/manage.py runserver 0.0.0.0:8000&"')

django_setup()
django_install()
django_setup()
django_install()
django_start()
