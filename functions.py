import random # Подключение библиотеки random
user_defined_list = [] # инициализируем список
list_length = int(input("Введите длинну списка: "))
for i in range(0,list_length): 
    n = random.randint(1,50) 
    user_defined_list.append(n) # заполняем список случайными числами от 1 до 50 в цикле, количество итераций задано пользователем
print("Полученный список:")
print(user_defined_list)