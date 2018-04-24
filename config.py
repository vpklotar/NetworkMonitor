import os

def read_config_files(path):
    """
    Will return a list of sections with key-value paris within them from all .conf and
    .cfg files within the given path and its subdirectories.
    """
    config_files = get_all_config_files(path)
    config_data = list()
    for config_file in config_files:
        config_data.extend(read_config(config_file))
    return config_data

def get_all_config_files(path):
    """
    Will return a list of all .conf and .cfg files in the path and its subdirectories
    """
    return_list = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        for file in filenames:
            if file.endswith(".conf") or file.endswith(".cfg"):
                return_list.append("%s/%s" % (dirpath, file))
    return return_list

def read_config(path):
    """
    Read a file from top to botton and read sections.
    Read key-value pairs within each section and append each section to a list that is later returned.
    """
    return_list = list()
    current_configs_dict = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            line = line.replace('\t', ' ', 1)
            if line.endswith('{'):
                if line.startswith('define'):
                    # This is the beginning of a definition
                    current_configs_dict['type'] = line[7:-2]
                else:
                    print("Invalid format of line '%s' in file %s" % (line, path))
            elif line.endswith('}'):
                # End of a definition
                return_list.append(current_configs_dict)
                current_configs_dict = {}
            elif len(current_configs_dict) > 0:
                # We are currently in a definition.
                if not (line.startswith(";") or line.startswith("#")):
                    try:
                        key, value = line.split(' ', 1)
                        current_configs_dict[key] = value.strip()
                    except ValueError:
                        print("Improperly configured line '%s' in file '%s'" % (line, path))
            elif line:
                # Not in a efinition and the line is not empty
                print("Invalid line '%s' in file %s" % (line, path))

    if len(current_configs_dict) > 0:
        print("Invalid format in file %s. A section was not closed off." % path)
    return return_list