def fibonacci():
    fibonacci = [1, 2]
    evens = []
    number = 0
    count_evens = 0
    i = 0
    while number < 4000001:
        number = fibonacci[i + 1] + fibonacci[i]
        fibonacci.append(number)
        i += 1
    print(fibonacci)

    for j in fibonacci:
        if j%2 == 0:
            evens.append(j)
            count_evens += j
    print(evens)
    print(count_evens)

fibonacci()