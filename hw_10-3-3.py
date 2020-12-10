# Author: DA 12/10/2020

def three_letter_words(a):
    total = 0
    while total < a:
        if len(total) == 3:
            total += 1
    return total

print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)