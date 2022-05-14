# Выполнила Черданцева Анна. QAP-

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


while True:
    try:
        array = input('Введите, пожалуйста, через пробел некоторые целые числа от 0 до 100: ').split()
        l_array = list(map(int, array))
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
        b_array.append(guest_num)
        bb_array = babble_sort(b_array)
        if guest_num < 0 or guest_num > 100:
            raise Exception
        break
    except ValueError:
        print('Введите, пожалуйста, ЦЕЛОЕ ЧИСЛО.')  # Отслеживается ошибка значений - число с запятой..
        exit()
    except Exception:
        print('Введите число не меньше 0 и не больше 100.')
        exit()

print(f'Отсортированный числовой массив: {b_array}.')

guest_num_in = binary_search(b_array, guest_num, 0, len(b_array))
smoll_in = guest_num_in - 1
big_in = guest_num_in + 1

print(f'Индекс вашего числа в массиве: {guest_num_in}.')

if smoll_in in range(len(b_array)):
    print(f'Индекс предыдущего меньшего числа: {smoll_in}.')
else:
    print(f'Индекс предыдущего меньшего числа: {smoll_in}, вне (меньше) диапазона.')

if big_in in range(len(b_array)):
    print(f'Индекс следующего большего числа: {big_in}.')
else:
    print(f'Индекс предыдущего меньшего числа: {big_in}, вне (больше) диапазона.')

if b_array[guest_num_in] == b_array[big_in]:
    print('Ваше число равно следующему числу.')
else:
    ...
