sorted_list = [x for x in range(10, 30)]
print (sorted_list)

def binary_search(arr, key):
    left = 0
    right = len(arr)-1

    while left <= right:
        middle = (left + right)//2
        
        if arr[middle] == key:
            print (f'Индекс элемента {key} равен {middle}')
            return middle
        
        elif arr[middle] < key:
            left = middle+1

        elif arr[middle] > key:
            right = middle-1
        
    print ('Элемент не найден')
    return False

binary_search(sorted_list, 29)


















# def binary_search(arr, key):
#     left = 0
#     right = len(arr)-1

#     while left <= right:
#         middle = (left + right)//2
        
#         if arr[middle] == key:
#             print (f'Индекс элемента {key} равен {middle}')
#             return middle
        
#         elif arr[middle] < key:
#             left = middle+1
#             print ('Cut left half')

#         elif arr[middle] > key:
#             right = middle-1
#             print ('Cut right half')
        
#     print ('Элемент не найден')
#     return False

# binary_search(sorted_list, 29)