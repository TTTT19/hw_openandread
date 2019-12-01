print('Задача №1')
# открываем файл
# Читаем строчки по следующей логике:
# - первая строчка название блюда
# - вторая - количество строчек
# - дальше количество прочитанных строчек с ингридиентами зависит от предыдущего числа
# - последняя пустая строчка
# Читаем строчки до момента, пока в первой строчке что нибудь есть
# Разделяем строчки через символ " | " - получаем 3 поля: ингридиент, меру и количество
# Получаем новый словарь Ключ - блюдо, значение - список из 3х полей (ингридиент, мера и количество)
cook_book = {}
with open('recipes.txt', encoding='utf8') as f:
    while True:
        dish = f.readline().strip()
        if not dish:
            break
        ingridient_number = int(f.readline().strip())
        ingridient_already_read = 0
        cook_book_dish_all = []
        while True:
            a = f.readline().strip().split(" | ")
            cook_book_dish = {}
            cook_book_dish["ingridient_name"]= a[0]
            cook_book_dish["quantity"] = a[1]
            cook_book_dish["measure"] = a[2]
            cook_book_dish_all.append(cook_book_dish)
            ingridient_already_read += 1
            if ingridient_number == ingridient_already_read:
                cook_book[dish] = cook_book_dish_all
                break
        f.readline().strip()
print(cook_book)



print('Задача №2')
# Создаем функцию с параметрами - список блюд, количество гостей
# Проходимся по каждому из блюд в списке
# # Находим это блюдо в кулинарной книге и проходимся по ингридиентам из книги
# # # создаем словарь "shoplist", в который поочередно заносим записи. Ключ - ингридиент, элементы - количество и мера.
# # # если ключ уже есть в словаре "shoplist" - меняем только элемент количество - добавляем к текущему значению старое.
# # # в каждой прогоне - умножаем количество ингридиента из прочитанной строки на количество гостей (второй параметр функции)
shoplist = {}
def get_shop_list_by_dishes(dishes, person_count=1):
    for dish_for_list in dishes:
        for ingridient_name_list in cook_book[dish_for_list]:
            if ingridient_name_list['ingridient_name'] in shoplist.keys():
                old_quantity = int(shoplist.get(ingridient_name_list['ingridient_name']).get('quantity'))
                shoplist[ingridient_name_list['ingridient_name']]= {'measure': ingridient_name_list['measure'], 'quantity': int(ingridient_name_list['quantity'])*person_count+old_quantity}
            else:
                shoplist[ingridient_name_list['ingridient_name']]= {'measure': ingridient_name_list['measure'], 'quantity': int(ingridient_name_list['quantity'])*person_count}

    return (shoplist)
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5))