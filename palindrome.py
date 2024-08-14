palindromes = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        multiply = i * j
        forwardMultiply = str(multiply)
        backwardMultiply = str(multiply)[::-1]
        if forwardMultiply == backwardMultiply:
            palindromes.append(multiply)
print(max(palindromes))