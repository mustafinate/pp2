#Implement a generator that returns all numbers from (n) down to 0.
 
def nums(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("n: "))
for i in nums(n):
    print(i, end = " ")