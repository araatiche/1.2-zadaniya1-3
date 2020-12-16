import random # Подключение библиотеки random
user_defined_list = [] # инициализируем список
list_length = int(input("Введите длинну списка: "))
for i in range(0,list_length): 
    n = random.randint(1,50) 
    user_defined_list.append(n) # заполняем список случайными числами от 1 до 50 в цикле, количество итераций задано пользователем
print("Полученный список:")
print(user_defined_list)
# функция вычисляющая среднее значение чисел в списке
def avg_value(input_list):
    list_elements_sum = sum(input_list) # встроенная функция sum вычисляет сумму элементов списка
    average = list_elements_sum / len(input_list) 
    return average 
# функция вычисляющая cумму с помощью цикла for
def for_summ(input_list):
    summ_f = 0
    for sf in input_list: # sf каждый цикл принимает текущее значение элемента input_list от первого до последнего 
        summ_f += sf # суммируем их в summ_f
    return summ_f
# функция вычисляющая cумму с помощью цикла while
def while_summ(input_list):
    summ_w = 0 
    sw = 0
    while (sw < len(input_list)): # пока sw меньше длинны входного списка
        summ_w += input_list[sw] # суммируем в summ_w значение элемента списка с индексом, равным текущему значению sw
        sw += 1 # инкримируем sw
    return summ_w
# выводим результаты всех функций
print("Среднее значение: ", avg_value(user_defined_list))
print("Сумма с помощью цикла for: ", for_summ(user_defined_list))
print("Сумма с помощью цикла while: ", while_summ(user_defined_list))