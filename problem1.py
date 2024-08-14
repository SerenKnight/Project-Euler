def multiples_of_3_or_5():
    sum = 0
    for number in range(0, 1000):
        if number%3 == 0:
            sum += number
        elif number%5 ==0:
            sum += number
    print(sum)
multiples_of_3_or_5()