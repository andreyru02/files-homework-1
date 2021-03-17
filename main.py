from pprint import pprint


class Cookbook:
    def entry_dict(self):
        cook_book = {}
        while_stop = True
        with open('recipes.txt') as f:
            try:
                while while_stop:
                    ing_list = []
                    for ing_name in f.readline().splitlines():
                        cook_book[ing_name] = ing_name
                    count = f.readline()

                    for _ in range(int(count)):
                        ing_dick = {}
                        ingredient = f.readline().strip()
                        ing_dick['ingredient_name'] = ingredient.split(' | ')[0]
                        ing_dick['quantity'] = ingredient.split(' | ')[1]
                        ing_dick['measure'] = ingredient.split(' | ')[2]
                        ing_list.append(ing_dick)
                    cook_book[ing_name] = ing_list

                    f.readline()
            except ValueError:
                while_stop == False
        print(cook_book)


Cookbook().entry_dict()
