import random
arr = random.sample(range(0, 20), 10)
print (arr)

def merge(a,b):
    i = 0 
    j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res += a[i:] + b[j:]
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return (arr)
    else:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])    
        right = merge_sort(arr[mid:])
    return merge(left, right)

print(merge_sort(arr))






# def merge_sort(arr):
#     # Последнее разделение массива
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     # Выполняем merge_sort рекурсивно с двух сторон
#     left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

#     # Объединяем стороны вместе
#     return merge(left, right, arr.copy())


# def merge(left, right, merged):

#     left_cursor, right_cursor = 0, 0
#     while left_cursor < len(left) and right_cursor < len(right):
      
#         # Сортируем каждый и помещаем в результат
#         if left[left_cursor] <= right[right_cursor]:
#             merged[left_cursor+right_cursor]=left[left_cursor]
#             left_cursor += 1
#         else:
#             merged[left_cursor + right_cursor] = right[right_cursor]
#             right_cursor += 1
            
#     for left_cursor in range(left_cursor, len(left)):
#         merged[left_cursor + right_cursor] = left[left_cursor]
        
#     for right_cursor in range(right_cursor, len(right)):
#         merged[left_cursor + right_cursor] = right[right_cursor]

#     return merged
