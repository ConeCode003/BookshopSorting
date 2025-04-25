import random


def bubble_sort(arr, comparison_function):
    swaps = 0
    sortirana = False
    while not sortirana:
        sortirana = True
        for idx in range(len(arr) - 1):
            if comparison_function(arr[idx], arr[idx + 1]):
                sortirana = False
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1
    print("Bubble sort: There were {0} swaps".format(swaps))
    return arr


def quicksort(lista, start, end, comparison_function):
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = lista[pivot_idx]
    lista[end], lista[pivot_idx] = lista[pivot_idx], lista[end]
    less_than_pointer = start
    for i in range(start, end):
        if comparison_function(pivot_element, lista[i]):
            lista[i], lista[less_than_pointer] = lista[less_than_pointer], lista[i]
            less_than_pointer += 1
    lista[end], lista[less_than_pointer] = lista[less_than_pointer], lista[end]
    quicksort(lista, start, less_than_pointer - 1, comparison_function)
    quicksort(lista, less_than_pointer + 1, end, comparison_function)
