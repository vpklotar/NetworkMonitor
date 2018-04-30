#!/usr/bin/python3
from config import read_config_files
from base.ServiceDefinition_class import ServiceDefinition
from base.HostDefinition_class import HostDefinition
from base.CommandDefinition_class import CommandDefinition
import SSE
import EM


class Main:

    def __init__(self):
        SSE.register_substitiution("USER1", "exec")
        self.parse_arguments()
        definitions = read_config_files('configs')
        self.definitions = self.init_definitions(definitions)
        EM.start()

    def parse_arguments(self):
        pass

    def init_definitions(self, definitions):
        re_defs = list()
        for definition in definitions:
            def_instance = self.init_definition(definition)
            if def_instance:
                re_defs.append(def_instance)
                def_instance.register()
        for definition in re_defs:
            definition.load_inheritance()
            result = definition.sanity_check()
            if len(result) > 0:
                print("Error(s) in definition:")
                for error in result:
                    print(error)
        return re_defs

    def init_definition(self, definition):
        def_type = definition["type"]
        if def_type == "host":
            return HostDefinition(definition)
        if def_type == "service":
            return ServiceDefinition(definition)
        if def_type == "command":
            return CommandDefinition(definition)
        else:
            print("Unsupported type '%s'" % def_type)


Main()
