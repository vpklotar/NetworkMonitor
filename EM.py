"Execution Manager"

import DM

service_connections = {}  # service_def -> [host, host, host]


def start():
    "Start the monitoring"
    init()
    global service_connections
    print(service_connections)


def register(service, host):
    "Register a host to a service"
    global service_connections
    if service not in service_connections.keys():
        service_connections[service] = []
    service_connections[service].append(host)


def init():
    "Grab all the service-definitions and correlate them with hosts"
    for service in DM.filter(type='service', sanity_check_ok=True):
        register(service, service.get('host_name'))
