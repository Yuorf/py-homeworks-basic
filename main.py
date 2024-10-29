# Задача 1
def read_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book

# Задача 2
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ing_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ing_name in shopping_list:
                    shopping_list[ing_name]['quantity'] += quantity
                else:
                    shopping_list[ing_name] = {'measure': measure, 'quantity': quantity}
    return shopping_list

# Задача 3
def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)

def merge_files(file_names, output_file):
    files_info = [(file_name, count_lines(file_name)) for file_name in file_names]
    files_info.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, line_count in files_info:
            out_file.write(f"{file_name}\n{line_count}\n")
            with open(file_name, 'r', encoding='utf-8') as in_file:
                out_file.writelines(in_file.readlines())
            out_file.write('\n')

cook_book = read_cook_book('recipes.txt')
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(shop_list)
merge_files(['1.txt', '2.txt'], 'result.txt')