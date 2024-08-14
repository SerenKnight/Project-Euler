def pythagorean_triple(n):
    solutions = []
    for i in range(1, int(n / 2)):
        for j in range(1, int(n / 2)):
            for k in range(1, int(n / 2)):
                if i + j + k == 1000 and i**2 + j**2 == k**2 and k > j > i:
                    solutions.append([i, j, k])
    product = solutions[0][0] * solutions[0][1] * solutions[0][2]
    print(product)


pythagorean_triple(1000)
