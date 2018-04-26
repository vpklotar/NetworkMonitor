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


class DM_test(unittest.TestCase):

    def test_register(self):
        self.addCleanup(clear)
        global definitions
        register({'name': 'test'})
        self.assertEqual(definitions, [{'name': 'test'}])

    def test_clear(self):
        self.addCleanup(clear)
        global definitions
        register({'name': 'test'})
        self.assertEqual(definitions, [{'name': 'test'}])
        clear()
        self.assertEqual(definitions, [])
    
    def test_clear_2(self):
        self.addCleanup(clear)
        global definitions
        register({'name': 'test'})
        clear()
        self.assertEqual(definitions, [])

    def test_all(self):
        self.addCleanup(clear)
        register({'name': 'test'})
        self.assertEqual(all(), [{'name': 'test'}])

    def test_filter(self):
        self.addCleanup(clear)
        register({'name': 'test'})
        self.assertEqual(filter(name='test'), [{'name': 'test'}])
    
    def test_filter_2(self):
        self.addCleanup(clear)
        register({'name': 'test'})
        self.assertEqual(filter(name='testar'), [])
    
    def test_filter_3(self):
        self.addCleanup(clear)
        register({'name': 'test'})
        self.assertEqual(filter(), [{'name': 'test'}])
    
    def test_filter_4(self):
        self.addCleanup(clear)
        register({'name': 'test'})
        self.assertEqual(filter(type='host'), [])


if __name__ == '__main__':
    unittest.main()
