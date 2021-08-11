#Сортировка вставками
import random
arr = random.sample(range(0, 20), 10)
print (arr)

def insertion_sort(a):
    N = len(a)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a
res = insertion_sort(arr)
print (res)
















# def insertion_sort(arr):
#     for i in range(len(arr)):
#         cursor = arr[i]
#         pos = i
#         while pos > 0 and arr[pos - 1] > cursor:
#             # Меняем местами число, продвигая по списку
#             arr[pos] = arr[pos - 1]
#             pos = pos - 1
#         # Остановимся и сделаем последний обмен
#         arr[pos] = cursor
#     print (arr)
