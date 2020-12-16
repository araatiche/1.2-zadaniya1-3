score_sum = 0 # инициализируем переменные для суммы оценок и количества строк в файле
line_count = 0
print("Оценка меньше 3 у следующих учеников:")
# без явного указания кодировки файл из задания не открывается (UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined>)
f = open('result.txt',"r",encoding="utf-8")
for line in f:
    current_line = line.rstrip() # функция rstrip() удаляет символ перевода строки из строки
    score_sum += int(current_line[-1]) # чтобы можно было взять последний элемент строки (оценка) как -1й элемент
    if int(current_line[-1]) < 3: # в случае если оценка меньше 3 выводим данную строку на экран 
        print(current_line)
    line_count += 1   # счетчик строк для подсчета среднго балла
awg_score = score_sum / line_count # считаем средний балл, выводим на экран
print("Средний бал: ",str(awg_score))