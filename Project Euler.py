sequence = [1, 2]
evens = [2]
sum = 2
new = 0
i = 2

while new < 4000000:
    new = sequence[i-1] + sequence[i-2]
    sequence.append(new)
    i+=1
    if new%2 ==0:
        evens.append(new)
        sum = sum + new

print(sum)
