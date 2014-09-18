#!/usr/bin/env python

__author__ = "Timothy McFadden"
__copyright__ = "Copyright 2014"
__credits__ = ["Timothy McFadden", "Jason Unrein"]
__license__ = "GPL"
__version__ = "0.0.0.1"  # file version
__maintainer__ = "Jason Unrein"
__email__ = "JasonAUnrein@gmail.com"
__status__ = "Development"

# Imports #####################################################################
from os import path, remove
import unittest
from persistent_pineapple import PersistentPineapple as PP


###############################################################################
class SanityTest(unittest.TestCase):
    test_path = path.dirname(path.realpath(__file__))
    test_file = "test1.json"
    save_file = "save1.json"
    fqtest = path.join(test_path, test_file)
    fqsave = path.join(test_path, save_file)

    def test_init(self):
        '''Verify object creation works/fails correctly'''

        # verify error is raised when no file is specified
        with self.assertRaises(TypeError):
            PP()
            PP(woc=True)
            PP(woc=False)

        # verify error is raised if file can't be found
        with self.assertRaises(IOError):
            PP(self.test_file)
            PP(self.test_file, woc=True)
            PP(self.test_file, woc=False)

        # verify valid file creates object
        
        self.assertIsInstance(PP(self.fqtest), PP)
        self.assertIsInstance(PP(self.fqtest, woc=True), PP)
        self.assertIsInstance(PP(self.fqtest, woc=False), PP)

    def test_get(self):
        '''Verify get method functionality'''
        pp = PP(self.fqtest)
        self.assertEqual(pp.get("setting1"), "value1")
        self.assertEqual(pp.get("setting 2"), 2)
        self.assertEqual(pp.get("section1"), {'subsetting1': 'subvalue2'})
    
    def test_borg(self):
        '''Verify borg functionality works (simple singleton)'''
        pp1 = PP(self.fqtest, woc=False)
        pp2 = PP(self.fqtest, woc=False)
        pp1.set("unsaved_value", 42)
        self.assertEqual(pp1.get("unsaved_value"), pp2.get("unsaved_value"))

    def test_reload(self):
        '''Verify reload functionality works'''
        pp = PP(self.fqtest, woc=False)
        pp.set("unsaved_value", 42)
        pp.reload()
        with self.assertRaises(KeyError):
            pp.get("unsaved_value")

    def test_save(self):
        '''Verify save functionality works'''
        pp1 = PP(self.fqtest, woc=False)
        pp1.set("unsaved_value", 42)
        pp1.save(path=self.fqsave)
        pp2 = PP(self.fqsave)
        self.assertEqual(pp1.settings, pp2.settings)
        remove(self.fqsave)
        
###############################################################################
if __name__ == "__main__":
    unittest.main()
