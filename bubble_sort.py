import random
arr = random.sample(range(0, 20), 10)
print (arr)

def bubble_sort(a):
    N = len(a)
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print(a)

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