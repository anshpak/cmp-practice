#  Напишите программу sorting.py, которая реализует несколько методов сортировки и сравнивает их по времени выполнения:
# def bubble_sort(lst) -- пузырьковая сортировка
# def insertion_sort(lst) -- сортировка вставками
# def selection_sort(lst) -- сортировка выбором
# def quick_sort(lst) -- быстрая сортировка
# def merge_sort(lst) -- сортировка слиянием
# def python_sort(lst) -- встроенная сортировка Python (timsort)
# Входные параметры каждой функции:
# n -- целое число, длина массива (по умолчанию 10)
# out -- выводить отсортированный массив после работы функции (True) или нет (False, по умолчанию)
# Программа должна сгенерировать массив целых случайных чисел в диапазоне (0,1000) и далее последовательно 
# сортировать его указанными выше методами. Если параметр out=True, то для каждого метода выводятся отсортированные массивы.

import sys, random, time, copy

def python_sort(lst, out = False):
    print('python sort')
    arr = copy.deepcopy(lst)
    t0 = time.time()
    arr.sort()
    print(time.time() - t0)
    if out:
        print(arr)

def bubble_sort(lst, out = False):
    print('bubble sort')
    arr = copy.deepcopy(lst)
    start = time.time()
    for j in range(len(arr) - 1):
    # потому что массив из одного элемента не сортирую
        # флаг для того, чтобы заранее выходить из цикла с частично отсортированным массивом
        flag = 0
        for i in range(len(arr) - 1 - j):
        # на каждой новой итерации элемент занимает свое место в конце
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = 1
        if flag == 0:
            break
    end = time.time()
    print(end - start)
    if out:
        print(arr)

# можно добавить просто обмен без arr[i + 1] = key в конце
def insertion_sort(lst, out = False):
    print('insertion sort')
    arr = copy.deepcopy(lst)
    start = time.time()
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while (i >= 0) and (arr[i] > key):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    end = time.time()
    print(end - start)
    if out:
        print(arr)

def selection_sort(lst, out):
    print('selection sort')
    arr = copy.deepcopy(lst)
    start = time.time()
    for i in range(len(arr) - 1):
        min_flag = i
        min = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_flag = j
        arr[i], arr[min_flag] = arr[min_flag], arr[i]
    end = time.time()
    print(end - start)
    if out:
        print(arr)

# вики
# как это работает правильно?
# def select_sort(A):
#     for i in range(len(A)-1):
#         for k in range(i+1, len(A)):
#             if A[k] < A[i]:
#                 A[k], A[i] = A[i], A[k]

def quick_sort_sort(arr, a, b):
    if a >= b:
        return None
    else:
        r_ind = random.randrange(a, b + 1)
        i = a
        while i <= b:
            if (arr[i] >= arr[r_ind]) and (i < r_ind):
                key = arr[i]
                j = i
                while j != r_ind:
                    arr[j] = arr[j + 1]
                    j += 1
                arr[r_ind] = key
                r_ind -= 1
            elif (arr[i] < arr[r_ind]) and (i > r_ind):
                key = arr[i]
                j = i
                while j != r_ind:
                    arr[j] = arr[j - 1]
                    j -= 1
                arr[r_ind] = key
                r_ind += 1
            else:
                i += 1
        quick_sort_sort(arr, a, r_ind) 
        quick_sort_sort(arr, r_ind + 1, b)

def quick_sort(lst, out):
    print('quick sort')
    arr = copy.deepcopy(lst)
    start = time.time()
    quick_sort_sort(arr, 0, len(arr) - 1)
    print(time.time() - start)
    if out:
        print(arr)

def merge(arr1, arr2):
    res = []
    l_min = len(arr1) if len(arr1) < len(arr2) else len(arr2)
    i = 0
    j = 0
    while (i < len(arr1)) and (j < len(arr2)):
        while (i < len(arr1)) and arr1[i] <= arr2[j]:
            res += [arr1[i]]
            i += 1
            # 
            # print(res)
            # 
        if i == len(arr1):
            break
        while (j < len(arr2)) and (arr2[j] < arr1[i]):
            res += [arr2[j]]
            j += 1
            # 
            # print(res)
            # 
    if j == len(arr2):
        res += arr1[i:]
    elif i == len(arr1):
        res += arr2[j:]
    return res

def merge_sort_sort(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    elif len(arr) == 1:
        return arr
    mid = len(arr) // 2
    # 
    # print(arr)
    #
    return merge(merge_sort_sort(arr[:mid]), merge_sort_sort(arr[mid:]))

def merge_sort(lst, out):
    print('merge sort')
    arr = copy.deepcopy(lst)
    start = time.time()
    arr = merge_sort_sort(arr)
    print(time.time() - start)
    if out:
        print(arr)

if len(sys.argv) == 1:
    n = 10
    out = False
elif len(sys.argv) == 2:
    out = False
else:
    n = int(sys.argv[1])
    out = sys.argv[2]

lst = [random.randrange(1000) for _ in range(n)]
bubble_sort(lst, out)
insertion_sort(lst, out)
selection_sort(lst, out)
quick_sort(lst, out)
merge_sort(lst, out)
python_sort(lst, out)