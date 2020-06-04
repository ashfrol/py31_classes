import os
from os.path import join

# def read_and_transform(filename):
#     cook_book = {}
#     recipe = []
#     with open(filename, 'r') as file:
#         for line in file:
#             line = line.strip()
#             if not line:
#                 cook_book[recipe[0]] = recipe[2:]
#                 # print(cook_book)
#                 list_of_ingredients = []
#                 for item in recipe[2:]:
#                     ingredient = {}
#                     item = item.split(' | ')
#                     # print(item)
#                     ingredient['ingredient_name'] = item[0]
#                     ingredient['quantity'] = item[1]
#                     ingredient['measure'] = item[2]
#                     list_of_ingredients.append(ingredient)
#                 cook_book[recipe[0]] = list_of_ingredients
#                 recipe.clear()
#             else:
#                 recipe.append(line)
#         # print(cook_book)
#         return cook_book

def create_dict_from_file(filename):
    cook_book = {}
    with open(filename, encoding='utf8') as file_work:
        for line in file_work:
            line = line.strip()
            dish_name = line
            counter = int(file_work.readline())
            list_of_ingredient = []
            for i in range(counter):
                temp_dict = {}
                ingredient = file_work.readline().lower().strip().split(' | ')
                temp_dict['ingredient_name'] = ingredient[0]
                temp_dict['quantity'] = ingredient[1]
                temp_dict['measure'] = ingredient[2]
                list_of_ingredient.append(temp_dict)
                cook_book[dish_name] = list_of_ingredient
            file_work.readline()
        # print(cook_book)
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_dict_from_file(join('input', 'recipes.txt'))
    print(cook_book)
    dict_of_ingredients = {}
    list_of_ingredients = []
    for dish in dishes:
        try:
            for ingredient in cook_book.get(dish):
                ingredient_name = ingredient.get('ingredient_name')
                measure = ingredient.get('measure')
                if ingredient['ingredient_name'] not in list_of_ingredients:
                    quantity = int(ingredient.get('quantity')) * person_count
                    dict_of_ingredients.update({ingredient_name:{'measure': measure, 'quantity': quantity}})
                    list_of_ingredients.append(ingredient['ingredient_name'])
                else:
                    quantity = int(ingredient.get('quantity')) * person_count + dict_of_ingredients[ingredient_name]['quantity']
                    dict_of_ingredients.update({ingredient_name:{'measure': measure, 'quantity': quantity}})
        except TypeError as e:
            print(f'В списке рецептов нет блюда {dish}')
    print(dict_of_ingredients)

# create_dict_from_file(join('input', 'recipes.txt'))

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }