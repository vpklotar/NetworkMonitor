#!/usr/bin/python3
import DM
from base.Definition_class import Definition
import unittest


class DM_test(unittest.TestCase):

    def test_register(self):
        self.addCleanup(DM.clear)
        DM.register({'name': 'test'})
        self.assertEqual(DM.definitions, [{'name': 'test'}])

    def test_clear(self):
        self.addCleanup(DM.clear)
        DM.register({'name': 'test'})
        self.assertEqual(DM.definitions, [{'name': 'test'}])
        DM.clear()
        self.assertEqual(DM.definitions, [])

    def test_clear_2(self):
        self.addCleanup(DM.clear)
        DM.register({'name': 'test'})
        DM.clear()
        self.assertEqual(DM.definitions, [])

    def test_all(self):
        self.addCleanup(DM.clear)
        DM.register({'name': 'test'})
        self.assertEqual(DM.all(), [{'name': 'test'}])

    def test_filter(self):
        self.addCleanup(DM.clear)
        DM.register({'name': 'test'})
        self.assertEqual(DM.filter(name='test'), [{'name': 'test'}])

    def test_filter_2(self):
        self.addCleanup(DM.clear)
        DM.register({'name': 'test'})
        self.assertEqual(DM.filter(name='testar'), [])

    def test_filter_3(self):
        self.addCleanup(DM.clear)
        DM.register({'name': 'test'})
        self.assertEqual(DM.filter(), [{'name': 'test'}])

    def test_filter_4(self):
        self.addCleanup(DM.clear)
        DM.register({'name': 'test'})
        self.assertEqual(DM.filter(type='host'), [])


class Definition_test(unittest.TestCase):

    def test_init_1(self):
        d = Definition({})
        self.assertEqual(d.settings, {})

    def test_init_2(self):
        d = Definition({'name': 'test'})
        self.assertEqual(d.settings, {'name': 'test'})

    def test_get(self):
        d = Definition({'name': 'test'})
        self.assertEqual(d.get('name'), 'test')

    def test_get_default_1(self):
        d = Definition({})
        self.assertEqual(d.get('name'), None)

    def test_get_default_2(self):
        d = Definition({})
        d.set_default('name', 'test')
        self.assertEqual(d.get('name'), 'test')

    def test_set_default_3(self):
        d = Definition({})
        d.set_default('name', 'test')
        self.assertEqual(d.get('name'), 'test')

    def test_set(self):
        d = Definition({'name': 'This is a test name'})
        d.set('name', 'test')
        self.assertEqual(d.get('name'), 'test')

    def test_set_override_false(self):
        d = Definition({'name': 'test'})
        d.set('name', 'This is a test name', override=False)
        self.assertEqual(d.get('name'), 'test')

    def test_load_settings_1(self):
        d = Definition({})
        d.load_settings({'name': 'test'})
        self.assertEqual(d.settings, {'name': 'test'})
    
    def test_load_settings_2(self):
        d = Definition({'name': 'test'})
        d.load_settings({'name': 'This is a test name'})
        self.assertEqual(d.settings, {'name': 'test'})
    
    def test_load_settings_3(self):
        d = Definition({'name': 'test'})
        d.load_settings({'name': 'This is a test name'}, override=True)
        self.assertEqual(d.settings, {'name': 'This is a test name'})
    
    def test_has_1(self):
        d = Definition({'name': 'test'})
        self.assertEqual(d.has('name'), True)
    
    def test_has_2(self):
        d = Definition({})
        self.assertEqual(d.has('name'), False)
    
    def test_register(self):
        d = Definition({'name': 'test'})
        d.register()
        self.assertEqual(DM.filter(name='test').pop(), d)
    
    def test_set_requiered_field(self):
        d = Definition()
        d.set_requiered_field('name')
        self.assertEqual(d.requiered_fields, ['name'])
    
    def test_sanity_check_1(self):
        d = Definition({'name': 'test'})
        d.set_requiered_field('name')
        self.assertEqual(d.sanity_check(), [])
    
    def test_sanity_check_2(self):
        d = Definition()
        d.set_requiered_field('name')
        self.assertEqual(len(d.sanity_check()), 0)
    
    def test_sanity_check_3(self):
        d = Definition({'register': 1})
        d.set_requiered_field('name')
        self.assertEqual(len(d.sanity_check()), 1)
    
    def test_sanity_check_ok_1(self):
        d = Definition({'register': 1})
        d.set_requiered_field('name')
        d.sanity_check()
        self.assertEqual(d.sanity_check_ok(), False)

    def test_sanity_check_ok_2(self):
        d = Definition({'register': 1, 'name': 'test'})
        d.set_requiered_field('name')
        d.sanity_check()
        self.assertEqual(d.sanity_check_ok(), True)
    
    def test_sanity_check_ok_3(self):
        d = Definition({'register': 1, 'name': 'test'})
        d.set_requiered_field('name')
        self.assertEqual(d.sanity_check_ok(), True)
    
    def test_sanity_check_ok_4(self):
        d = Definition({'register': 1})
        d.set_requiered_field('name')
        self.assertEqual(d.sanity_check_ok(), False)

    def test_load_defaults_1(self):
        d = Definition()
        d.set_default('name', 'test')
        d.load_defaults()
        self.assertEqual(d.settings, {'name': 'test'})
    
    def test_load_defaults_2(self):
        d = Definition({'name': 'test'})
        d.set_default('name', 'This is a test')
        d.load_defaults()
        self.assertEqual(d.settings, {'name': 'test'})
    
    def test_inheritance(self):
        d = Definition()
        self.assertEqual(d.load_inheritance(), None)


if __name__ == '__main__':
    unittest.main()
