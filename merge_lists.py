a = [x for x in range(5, 15, 4)]
b = [x for x in range(0, 10, 2)]
print (a, b, sep='\n')

def merge_lists(a, b):
    i = 0
    j = 0
    res = []
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res += a[i:] + b[j:]  
    print(res)  
merge_lists(a, b)        