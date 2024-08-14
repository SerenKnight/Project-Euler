num = 600851475143
newNum = num - 1
#primeFactors = []
for i in range(2, newNum):
    factor = num%i
    if factor == 0:
        factor1 = i
        factor2 = num/i
        for j in range(2, num):
            if factor1%j == 0:
                break
            else:
                primeFactor = factor1
                print(primeFactor)
                break
        for k in range(2, num):
            if factor2%k == 0:
                break
            else:
                primeFactor = factor2
                print(primeFactor)
                break
                #primeFactors.append(primeFactor)
#print(max(primeFactors))