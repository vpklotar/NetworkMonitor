hosts = list()
services = list()

def register(instance):
    global hosts
    global services
    if instance.get('type') == "host":
        hosts.append(instance)
    elif instance.get('type') == "service":
        services.append(instance)

def get_host(name):
    global hosts
    """Will return a host with the given name if it is registed"""
    for host in hosts:
        if host.get('host_name') == name:
            return host
    return None