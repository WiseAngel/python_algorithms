a = [1,6,7,8,3,4,5,6]
b = [x for x in a if x > 3]
print(b)

c = filter(lambda x: x < 4, a)
print(c)