import random
arr = random.sample(range(0, 10), 10)
print (arr)

def search_max_in_list(arr):
    max = arr[0]
    index = 0
    for i, v in enumerate(arr):
        if v > max:
            max = v
            index = i
    print (f'Максимальный элемент в списке равен {max} с ключом {index}')
search_max_in_list(arr)








# def search_max_in_list(arr):
#     max = arr[0]
#     index = 0
#     comparisons = 0
#     replacements = 0

#     for i, v in enumerate(arr):
#         if v > max:
#             max = v
#             index = i
#             replacements += 1
#         comparisons += 1

#     print(f'Замен {replacements}. Проверок {comparisons}')
#     print (f'Максимальный элемент в списке равен {max} с ключом {index}')


# search_max_in_list(arr)