import random
arr = random.sample(range(0, 20), 10)
print (arr)

def selection_sort(arr):        
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
                print (arr)
        arr[min], arr[i] = arr[i], arr[min]
    print (arr)

selection_sort(arr)