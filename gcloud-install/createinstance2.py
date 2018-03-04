#!/usr/bin/python

from oauth2client.client import GoogleCredentials
#Brings in authentication methods to connect to Google properly.
from googleapiclient import discovery
#Allows for VM instances to be catalogued and labeled for this machine.
import pprint
import json
import create_ldap 
from create_ldap import create_instance

credentials = GoogleCredentials.get_application_default()
compute = discovery.build('compute', 'v1', credentials=credentials)

project = 'genuine-ether-191902'
zone = 'us-east1-b'

#Changed the name to reflect my own project ID.

name = 'something-profound'
#Template name is template name.

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']

newinstance = create_instance(compute, project, zone, name)
instances = list_instances(compute, project, zone)
#Functions defined by the discovery section of the googleapiclient, most likely.

pprint.pprint(newinstance)
pprint.pprint(instances)
