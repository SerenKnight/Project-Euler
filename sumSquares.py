sumSquares = 0
squareSum = 0
sum = 0
for i in range(1, 101):
    sumSquares += i**2
    sum += i
squareSum = sum**2
diff = squareSum - sumSquares
print(diff)