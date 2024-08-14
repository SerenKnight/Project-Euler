count = 0
primesList = []
for i in range(2, 100000):
    prime = True
    for j in range(2, int(i/2)):
        if count >= 10001:
            break
        if i%j == 0:
            prime == False
            break
    if prime == True:
        count += 1
        #print(i)
        primesList.append(i)
print(count)
#print(primesList)