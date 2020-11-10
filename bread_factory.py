# This file contains the Naan Factory class

class Naan_Factory:

    def make_dough(self, ingredient_1, ingredient_2):
        # If the inputted ingredients are both only water and flour, then we can make dough
        if (ingredient_1 == "water" and ingredient_2 == "flour") or (ingredient_1 == "flour" and ingredient_2 == "water"):
            return "Made Dough!"
        # If ingredients are not water or flour, ask for water and flour input
        else:
            return "Need water and flour in order to make dough"

    def bake_naan(self, ingredient):
        # In order to make naan, we need dough
        if 'dough' in ingredient:
            return "Here is your freshly baked naan!"
        # No dough, no naan!
        else:
            return "Cannot make naan without dough!"

    def factory(self, *ingredients):
        # Factory will run if we have water and flour available
        if 'water' in ingredients and 'flour' in ingredients:
            return "Making Naan!"
        # If we dont have water or flour we cannot produce bread!
        else:
            return "To make naan, water and flour is needed"

    def run_factory(self):
        while True:
            selection = input("""
            What would you like to do?
            1. Make dough
            2. Bake naan
            3. Run Factory
            (exit to stop)
            \n --> """).lower()

            if '1' in selection:
                print("What are your ingredients? ")
                ingredient_1 = input('1. -> ').lower()
                ingredient_2 = input('2. -> ').lower()
                print(self.make_dough(ingredient_1, ingredient_2))

            elif '2' in selection:
                have_dough = input("Do you have dough to bake? (Y/N)\n -> ").lower()
                if have_dough == 'y':
                    print(self.bake_naan('dough'))
                elif have_dough == 'n':
                    print("You need dough to bake naan bread")

            elif '3' in selection:
                have_ingredients = input("Have water and flour?? (Y/N)\n --> ").lower()
                if have_ingredients == 'y':
                    print(self.factory('water', 'flour'))
                elif have_ingredients == 'n':
                    print("We need water and flour to make naan!")

            elif 'exit' in selection:
                print("Thank you for using this factory menu")
                break


def main():

    # Created an object of the class to test functionality
    factory_test = Naan_Factory()
    factory_test.run_factory()


if __name__ == '__main__':
    main()