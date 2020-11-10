# This is the test file

# Import all the relevant files and modules required for testing
from bread_factory import Naan_Factory
import unittest
import pytest # always pip install pytest

# Create class to write tests
class Factory_Test(unittest.TestCase):

    # Create an object of the class
    customer = Naan_Factory()

    # If the ingredients include both water and flour, then output should be fresh dough
    def test_make_dough(self):
        self.assertEqual(self.customer.make_dough('water', 'flour'), "Made Dough!")
        # baking powder and salt are not the ingredients so should not be equal
        self.assertNotEqual(self.customer.make_dough('baking powder', 'salt'), "Made Dough!")

    # If input is fresh dough, then it should return freshly baked naan
    def test_bake_naan(self):
        self.assertEqual(self.customer.bake_naan('dough'), 'Here is your freshly baked naan!')
        self.assertNotEqual(self.customer.bake_naan('water'), 'Here is your freshly baked naan!')

    # Factory will only product bread if water and flour are the ingredients
    def test_factory(self):
        self.assertEqual(self.customer.factory('water', 'flour'), 'Making Naan!')
        self.assertEqual(self.customer.factory('flower', 'sugar'), 'To make naan, water and flour is needed')


