a = [1,6,7,8,3,4,5,6]
b = [x for x in a if x > 3]
print(b)

c = list(filter(lambda x: x < 4, a))
print(c)

def fac(x):
  return 1 if x==1 else fac(x-1)*x
print(fac(4))

def fib(n):
  return 1 if n<=2 else fib(n-1)+fib(n-2)
print(fib(5))

def palindrome(s):
  if len(s)<=1:
    return True
  elif s[0] != s[-1]:
    return False
  else: 
    return palindrome(s[1:-1])
print(palindrome('asdsa1'))

s = "1 2 3 4 5 6"
str_to_list = list(map(int, s.split()))
print(str_to_list)