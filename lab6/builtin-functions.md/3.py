#check whether a passed string is palindrome or not

text = str(input())
reversedText = ''.join(reversed(text))
if(reversedText == text):
    print("is palindrom")
else:
    print("not palindrom")