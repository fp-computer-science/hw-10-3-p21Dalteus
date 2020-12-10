# Author: DA 12/10/2020

def count_odds(n):
    y = 0
    x = 1
    while x < n+1:
        if n % 2 != 0:
            y += x
            x += 1
    return y

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)