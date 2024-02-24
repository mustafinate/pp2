#Define a function with a generator iterate the numbers, which are divisible by 3 and 4,range 0 and n.

def divisiblity(n):
    for i in range(n):
        if(i % 3 == 0 and i % 4 == 0):
            yield i

n = int(input())
nums = [i for i in divisiblity(n)]
print(nums)