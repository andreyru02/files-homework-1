from pprint import pprint


class Cookbook:
    def __init__(self):
        self.cook_book = {}
        self.list_dishes = {}

    def entry_dict(self):
        while_stop = True
        with open('recipes.txt') as f:
            while while_stop:
                ing_list = []
                ing_name = f.readline().strip()
                if not ing_name:
                    break
                self.cook_book[ing_name] = ing_name
                count = f.readline()

                for _ in range(int(count)):
                    ing_dick = {}
                    ingredient = f.readline().strip()
                    ing_dick['ingredient_name'] = ingredient.split(' | ')[0]
                    ing_dick['quantity'] = ingredient.split(' | ')[1]
                    ing_dick['measure'] = ingredient.split(' | ')[2]
                    ing_list.append(ing_dick)
                self.cook_book[ing_name] = ing_list

                f.readline()
        return self.cook_book

    def get_shop_list_by_dishes(self, dishes, person_count):
        self.entry_dict()
        for dish_get in dishes:
            for dish, ingredients in self.cook_book.items():
                if dish_get == dish:
                    for ing in ingredients:
                        self.list_dishes[ing['ingredient_name']] = {'measure': ing['measure'],
                                                                    'quantity': int(ing['quantity']) * person_count}

        return self.list_dishes


pprint(Cookbook().entry_dict())
pprint(Cookbook().get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
