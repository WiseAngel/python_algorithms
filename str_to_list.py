a = [1, 6, 7, 8, 3, 4, 5, 6]
b = [x for x in a if x > 3]
print(b)

c = list(filter(lambda x: x < 4, a))
print(c)

s = "1 2 3 4 5 6"
str_to_list = list(map(int, s.split()))
print(str_to_list)
