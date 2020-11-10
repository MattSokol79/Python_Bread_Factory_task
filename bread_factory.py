# This file contains the Naan Factory class

class Naan_Factory:

    def make_dough(self, *ingredients):
        # If the inputted ingredients are both only water and flour, then we can make dough
        if 'water' in ingredients and 'flour' in ingredients:
            return "Fresh dough"
        # If ingredients are not water or flour, ask for water and flour input
        else:
            return "Need water and flour in order to make dough"

    def bake_naan(self, ingredient):
        # In order to make naan, we need fresh dough, so it will only run if the previous
        # method resolves
        if 'Fresh dough' in ingredient:
            return "Freshly baked naan"
        # No fresh dough, no naan!
        else:
            return "Cannot make naan without dough!"

    def run_factory(self, *ingredients):
        # Essentially makes sure that the user inputs the correct ingredients and this
        # ensures that all the previous methods work
        if 'water' in ingredients and 'flour' in ingredients:
            baked_naan = self.bake_naan("Fresh dough")
            if baked_naan == "Freshly baked naan":
                return True
        # If we dont have water or flour we cannot produce bread!
        else:
            return "To make naan, water and flour is needed"



test = Naan_Factory()
print(test.bake_naan('Fresh dough'))
print(test.run_factory('water', 'flour'))