import random
arr = random.sample(range(0, 20), 10)
print (arr)

def quick_sort(arr):

    if len(arr) <= 1:
        return (arr)

    sep = arr[0]
    # sep = arr[random.randint(0, len(arr)-1)] 
    left = [x for x in arr if x < sep]
    right = [x for x in arr if x > sep]
    mid = [x for x in arr if x == sep]
    return quick_sort(left) + quick_sort(mid) + quick_sort(right)

print(quick_sort(arr))
























# def partition(nums, low, high):  
#     # Выбираем средний элемент в качестве опорного
#     # Также возможен выбор первого, последнего
#     # или произвольного элементов в качестве опорного
#     pivot = nums[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1

#         j -= 1
#         while nums[j] > pivot:
#             j -= 1

#         if i >= j:
#             return j

#         # Если элемент с индексом i (слева от опорного) больше, чем
#         # элемент с индексом j (справа от опорного), меняем их местами
#         nums[i], nums[j] = nums[j], nums[i]

# def quick_sort(nums):  
#     # Создадим вспомогательную функцию, которая вызывается рекурсивно
#     def _quick_sort(items, low, high):
#         if low < high:
#             # This is the index after the pivot, where our lists are split
#             split_index = partition(items, low, high)
#             _quick_sort(items, low, split_index)
#             _quick_sort(items, split_index + 1, high)

#     _quick_sort(nums, 0, len(nums) - 1)
#     return (nums)