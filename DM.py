"DefinitionManager"
import unittest
definitions = list()


def register(instance):
    "Will register a definition to to DM"
    global definitions
    definitions.append(instance)


def all():
    "Returns all definitions"
    global definitions
    return definitions


def filter(**args):
    "Will return all the definitions matching the arguments given"
    global definitions
    return_list = list()
    for definition in definitions:
        for key, value in args.items():
            if definition.get(key) != value:
                break
        else:
            return_list.append(definition)
    return return_list


def clear():
    "Used to clear the registered definitions"
    global definitions
    definitions = list()
