# подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
# Преобразование введённой последовательности в список
# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.

# Выполнила Черданцева Анна. QAP-73.
def babble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


# def smoll_big_in(b_array, element):
#     if b_array.index(element) < guest_num:
#         return f'Индекс предыдущего меньшего числа {b_array.index(element)}.'
#     elif b_array.index(element) > guest_num:
#         return f'Индекс  следующего большего числа {b_array.index(element)}.'
#     else:
#         ...


while True: # Открыт цикл с отслеживанием ошибок
    try:
        array = input('Введите, пожалуйста, через пробел некоторые целые числа от 0 до 100: ').split()
        l_array = list(map(int, array))  # Преобразуем в список гостевой массив.
        b_array = babble_sort(l_array)
        for i in b_array:
            if i < 0 or i > 100:
                raise Exception
        break
    except ValueError:
        print('Введите целые числа, через пробел, от 0 да 100.')  # Отслеживается ошибка значений - буквенный ввод.
        exit()
    except Exception:
        print('Введите числа не меньше 0 и не больше 100.')
        exit()

while True:
    try:
        guest_num = int(input('Введите, пожалуйста, искомое число: '))
        if guest_num < 0 or guest_num > 100:
            raise Exception
        break
    except ValueError:
        print('Введите, пожалуйста, ЦЕЛОЕ ЧИСЛО.')  # Отслеживается ошибка значений - число с запятой..
        exit()
    except Exception:
        print('Введите число не меньше 0 и не больше 100.')
        exit()

print(b_array)

guest_num_in = binary_search(b_array, guest_num, 0, len(b_array))
print(guest_num_in.__index__())

for i in b_array:


# if guest_num == guest_num_in:
#     print(f'Ваше число {guest_num} совпадает со следующим числом.')
# elif smoll_in:
#     print(f'Индекс предыдущего меньшего числа {b_array.index(smoll_in)}.')
# elif big_in:
#     print(f'Индекс  следующего большего числа {b_array.index(big_in)} меньше.')
# else:
#     print(f'Ваше не понимаю что тут надо делать!')


