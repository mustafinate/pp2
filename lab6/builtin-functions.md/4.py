#invoke square root function after specific milliseconds

import time
import math

def my(num, miliseconds):
    time.sleep(miliseconds / 1000) #пауза выполнения программы
    # на определенное количество секунд
    # указанное в аргументе функции. Аргументы только секунды
    res = math.sqrt(num)
    return res

num = int(input())
miliseconds = int(input())
output = my(num, miliseconds)
print(f"Square root of {num} after {miliseconds} miliseconds is", output)