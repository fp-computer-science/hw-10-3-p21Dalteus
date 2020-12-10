# Author: DA 12/10/2020

def sum_odds(lst):
    nums = 0
    while x < lst:
        if x % 2 > 0:
            nums += x
    return nums

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)