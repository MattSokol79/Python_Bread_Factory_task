# Task - TDD Bread Factory! bread

**Timings**
- 60-90 Minutes

**Summary**
- TDD bread factory is the latest bread brand in Py Land. It always produces the best bread because it has the best testing strategy!

- What they do is before they make any new bread, they make a test to make sure the end output is correct. Then they adjust the recipe until it's just right!

- You are going to do the same with bread! This is called Test Driven Development.

**Tasks**
- This exercise is going to bring together lots of concepts.

**Learning Outcomes**
- Learning outcomes include:
    - git
    - github
    - functions
    - TDD
    - Separation of concerns - this is important do not ignore!
    - DRY code
    - DOD

**Installing and running**
-To run the naan factory do the following:

`import naan factory
run factory()`

**TDD - test driven development**
1. write the test
2. run it, and read the error
3. code and make it pass the test
this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

**Unit Tests**
Test single pieces of code. Like a function.

**base of a test**
Usually has 3 phases.
- setup phase (know variables)
- calling of the function / piece of code with know variables
- asserting for expect output

**User stories for Naan Factory**
1. As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

2. As a user, I can use the bake dough with dough to get naan.

3. As a user, I can user the run factory with water and flour and get naan.

**Acceptance Criteria**
- you have written tests
- test pass
- you have written more test to make sure everything works as indented
- all user stories are satisfied
- code does not break
- code has exit condition
- DOD is followed

## Answer
- Wrote 2 files, the test file which tests
the code, and the code file

**Test file**
- First import all necessary modules for testing
```python
# This is the test file

# Import all the relevant files and modules required for testing
from bread_factory import Naan_Factory
import unittest
import pytest # always pip install pytest
```
- Then create the test class which ensures
the code passes all the tests
```python
# Create class to write tests
class Factory_Test(unittest.TestCase):

    # Create an object of the class
    customer = Naan_Factory()

    # If the ingredients include both water and flour, then output should be fresh dough
    def test_make_dough(self):
        self.assertEqual(self.customer.make_dough('water', 'flour'), "Fresh dough")
        # baking powder and salt are not the ingredients so should not be equal
        self.assertNotEqual(self.customer.make_dough(['baking powder', 'salt']), "Fresh dough")

    # If input is fresh dough, then it should return freshly baked naan
    def test_bake_naan(self):
        self.assertEqual(self.customer.bake_naan('Fresh dough'), 'Freshly baked naan')

    # Factory will only product bread if water and flour are the ingredients
    def test_run_factory(self):
```

**Code File**
- The task asked for 3 functions, one to make
dough, one to make naan and one to run the factory.
- If the user inputs anything other than flour 
and water as ingredients, the factory will not
run
```python
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
```
- In order to run the factory, we need a nice user interface
which provides the user with options of what they can do:
```python
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
```

- To test if the program has worked, called
an object of the class and ran the program
```python
def main():

    # Created an object of the class to test functionality
    factory_test = Naan_Factory()
    factory_test.run_factory()


if __name__ == '__main__':
    main()
```