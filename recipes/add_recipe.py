import sys
import os
import re
import json

# command prompt for ingredient on at a time
# enter done to move to instructions
# command prompt for instructions one at a time
# enter done to move to notes
# enter done to save the recipe to the json file

# JSON Schema

# 1. Recipe Name
#     A. 'ingredients'
#         a. %ingredient% : %measurement%
#     B. 'instructions'
#         a. %step% : %text%
#     C. 'notes'
#         a. text
#
# {recipeName : {
# 'ingredients' : {
# ingredientName1 : measurement,
# ingredientName2 : measurement,
# ingredientName3 : measurement,
# ingredientName4 : measurement
# },
# 'instructions' : {
# stepOne : text,
# stepTwo : text,
# stepThree : text,
# stepThree : text
# },
# 'notes' : text
# }}




class recipeBuilder():
    def __init__(self):
        self.ingredient_count = 0
        self.ingredients = {}
        self.instruction_count = 0
        self.instructions = {}
        self.note_count = 0
        self.notes = {}
        self.recipe_json = 'recipe_list.json'
        self.continue_keywords = ['Done', 'done', 'DONE', 'Next', 'next', 'NEXT', 'No', 'no', 'NO', '']

    def camel_case(self, string):
        split_string = list(map(lambda x: x.capitalize(), re.split(r', | |_|-', string)))
        camel_string = ''.join(split_string)
        return camel_string[0].lower() + camel_string[1:]

    def get_recipe_name(self):
        name_recieved = False
        while not name_recieved:
            name = input("What is the name of the recipe?\n")
            if name == '' or name == ' ':
                print('You need to enter a recipe name!')
                continue
            else:
                name_recieved = True
                name = self.camel_case(name)
        self.recipe_name = name
        return self.recipe_name

    def get_recipe_ingredients(self):
        print('Add in the ingredients and then their measurements: \n(ENTER to move on)')
        print('~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ')
        keep_adding = True
        while keep_adding:
            self.ingredient_count += 1
            ingredient_input = input(f"Ingredient {self.ingredient_count}:\n")
            if ingredient_input not in self.continue_keywords:
                measurement_input = input(f"Measurement for {ingredient_input}:\n").lower()
                self.ingredients[self.camel_case(ingredient_input)] = measurement_input
            else:
                if self.ingredient_count == 1:
                    print('You need to add at least one ingredient!')
                    self.ingredient_count -= 1
                    continue
                else:
                    keep_adding = False
                    break
        return self.ingredients

    def get_recipe_instructions(self):
        print('List the instructions one by one: \n(ENTER to move on):')
        print('~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ')
        keep_adding = True
        while keep_adding:
            self.instruction_count += 1
            instruction_input = input(f"Instruction {self.instruction_count}:\n")
            if instruction_input not in self.continue_keywords:
                self.instructions[self.instruction_count] = instruction_input
            else:
                if self.instruction_count == 1:
                    print('You need to add at least one instruction!')
                    self.instruction_count -= 1
                    continue
                else:
                    keep_adding = False
                    break
        return self.instructions

    def get_recipe_note(self):
        print('If you have a note to add, you can do so below: \n(ENTER to move on):')
        print('~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ')
        keep_adding = True
        while keep_adding:
            self.note_count += 1
            note_input = input(f"Note {self.note_count}:\n")
            if note_input not in self.continue_keywords:
                self.notes[self.note_count] = note_input
            else:
                keep_adding = False
                break
        return self.notes


    def create_recipe_json(self):
        output = {}
        output[self.recipe_name] = {
        'ingredients' : self.ingredients,
        'instructions' : self.instructions,
        'notes' : self.notes
        }
        self.json_output = output
        return self.json_output

    def write_to_json(self):
        with open(self.recipe_json, 'r+') as f:
            data = json.loads(f.read())
            print(data)
            assert hasattr(self, 'json_output'), "You need to create a recipe to export it!"
            data['recipes'][self.recipe_name] = self.json_output[self.recipe_name]
        with open(self.recipe_json, 'w') as j:
            print(data)
            j.write(json.dumps(data))
        return data

    def create_a_recipe(self):
        self.get_recipe_name()
        self.get_recipe_ingredients()
        self.get_recipe_instructions()
        self.get_recipe_note()
        self.create_recipe_json()
        self.write_to_json()

b = recipeBuilder()
b.create_a_recipe()
