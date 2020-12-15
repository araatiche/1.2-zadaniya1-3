import random # Подключение библиотеки random
# инициализируем списки
first_list = []
second_list = []
for i in range(0,20): # заполняем списки в цикле
    n = random.randint(1,15) 
    first_list.append(n) # первый случайными значениями от 1 до 15
    m = random.randint(1,10)
    second_list.append(m) # второй случайными значениями от 1 до 10
print("Исходные списки:")
print(first_list)
print(second_list)
for i in range(0,len(second_list)): # внешним циклом перебераем значения второго списка
    current_value = second_list[i] 
    for j in range(first_list.count(current_value)):  # вложенным циклом находим количество вхождений текущего элемента второго списка в первый
        first_list.remove(current_value) # и удаляем его это количество раз
print("Первый список с удаленными значениями:")
print(first_list)