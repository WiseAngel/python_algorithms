def pascale_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i+1)
        for j in range(i+1):
            if j != 0 and j != i:
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    for r in triangle:
        print(r)


pascale_triangle(10)
