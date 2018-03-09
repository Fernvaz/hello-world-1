def create_instance(compute, project, zone, name):
    startup_script = open('startup-script.sh', 'r').read()
#Opens the startup script to get subcommands for the install.
    image_response = compute.images().getFromFamily(
      project='centos-cloud', family='centos-7').execute()

    source_disk_image = image_response['selfLink']
    machine_type = "zones/%s/machineTypes/f1-micro" % zone
#Starts the machine with a micro CPU and Centos 7 OS.
    config = {
        'name': name,
        'machineType': machine_type,

        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],
#Configures network interfaces to be able to communicate with the outside world.

        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],
#Gives the instance the script is running on the ability to interact with other instances and create logs.
       # Enable https/http for select instances
       "labels": {
       "http-server": "",
      "https-server": ""
       },

       "tags": {
       "items": [
       "http-server",
       "https-server"
       ]
       },

        'metadata': {
            'items': [{
#Metadata may be passed to the new instance through these fields.
                'key': 'startup-script',
                'value': startup_script
#Enables the startup script we wrote upon the instance starting up.
            }]
        }
    }


    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()
