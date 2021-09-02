"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


def stopwatch(func):
    def start_stop(element):
        start = time.time()
        func(element)
        stop = time.time()
        print(f'Время выполнения: {stop - start}')
        return element

    return start_stop


@stopwatch
def dict_add(element):
    """
    Наполнение словаря.
    Сложность O(1)
    """
    for index in range(1000000):
        element[index] = str(index)
    return element


@stopwatch
def list_add(element):
    """
    Наполнения списка.
    Сложность O(1)
    """
    for index in range(1000000):
        element.append(str(index))
    return element


@stopwatch
def change_values(element):
    """
    замена 300ого элемента списка по индексу.
    Сложность O(1)
    """
    element[299] = 1
    return element


@stopwatch
def dict_getting_element(element):
    """
    Получение значение словаря с индексом 100
    Сложность функции: O(1)
    """
    return element[100]


@stopwatch
def list_getting_element(element):
    """
    Получение значение списка с индексом 100
    Сложность функции: O(1)
    """
    return element[100]


@stopwatch
def dict_del_element(element):
    """
    Удаление значение словаря с индексом 100
    Сложность функции: O(n)
    """
    return element.pop(100)


@stopwatch
def list_del_element(element):
    """
    Удаление значение словаря с индексом 100
    Сложность функции: O(1)
    """
    return element.pop(100)


new_dict = {}
new_list = []
print('Наполнения словаря.')
dict_add(new_dict)
print('Наполнения списка.')
list_add(new_list)
"""
Наполнение словаря происходит медленнее чем в список,хотя сложности операции одинаковы. я думаю это связано с тем,
что в словарь идет добавление по индексу и при каждом добавлении
необходимо пересчитывать индексы.
"""
print('замена 300ого элемента списка по индексу в словаре.')
change_values(new_dict)
print('замена 300ого элемента списка по индексу в списке.')
change_values(new_list)
"""
замена элемента словаря по индексу происходит значительно
медленнее, так как словарь неупорядоченный, а список упоряоченный.
"""
print('Получение значения словаря с индексом 100')
dict_getting_element(new_dict)
print('Получение значение списка с индексом 100')
list_getting_element(new_list)
print('Удаление значения словаря с индексом 100')
dict_del_element(new_dict)
print('Удаление значения списква с индексом 100')
list_del_element(new_list)

"""
Удаление необходимого элемента в списке происходит быстрее чем в словаре.
Словарь не упорядоченный, а список упорядоченный.
"""
