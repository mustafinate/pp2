#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def evens(n):
    for i in range(n):
        if(i % 2 == 0):
            yield i

n = int(input())
mylist = list(evens(n))
print(mylist)