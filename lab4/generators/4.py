#Implement a generator quares to yield the square of all numbers from (a) to (b)

def squares(a, b):
    for i in range(a, b + 1):
        yield i**2

a = int(input("a: "))
b = int(input("b: "))
for i in squares(a, b):
    print(i)