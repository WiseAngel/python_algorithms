import random
arr = random.sample(range(0, 20), 10)
print (arr)

def bubble_sort(arr):
    len_list = len(arr)
    for i in range(len_list):
        for j in range(len_list - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

bubble_sort(arr)



# def bubble_sort(arr):
#     comparisons = 0
#     replacements = 0
#     len_list = len(arr)
#     for i in range(len_list):
#         print (f'****************{arr}')
#         for j in range(len_list - i -1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 replacements += 1
#                 print (arr)
#             else:
#                 print ('Замена не нужна')
#     comparisons += 1
        

# bubble_sort(arr)