"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
companies = {'ARS': 526879.45, 'SECT': 895674.32, 'FOX': 789456213.78, 'ZZZ': 478956213.56, 'XXX': 4789555555.55}

# 1 способ
list_values = sorted(list(companies.values()), reverse=True)[:3]                     # O(n)
for el in list_values:                                                               # O(1)
    for k, v in companies.items():                                                   # O(n)
        if v == el:
            print(k, ':', v)                                                         # O(1)

# Сложность: Линейная O(n)  + O(1) + O(n)  + O(1) = O(n)

# 2 способ
sorted_companies = sorted(companies, key=companies.get, reverse=True)[:3]    # O(n log n)
for i in sorted_companies:                                                   # O(1)
    print(i, ':', companies.get(i))                                          # O(1)

# Линейно-логарифмическая O(n log n) + O(1) + O(1) = O (n log n)

# Эффективнее 1 способ, т.к. итоговая сложность O(n) меньше, чем O(n log n)