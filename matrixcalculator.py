print("Matrix Calculator")
print("What you wanna do: ")
print("Addition-Press 1")
print("Multiplication-Press 2")
print("Subtraction-Press 3")
print("Inverse-Press 4")
m=int(input())
if m==1:
    print("Button for addition is pressed")
    print("Order of first matrix")
    m, n = list(map(int, input().split()))
    m1 = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input("Enter the number")))
        m1.append(a)

    for i in range(m):
        for j in range(n):
            print(m1[i][j], end=" ")
        print()

    print("Order of second matrix")
    p, q = list(map(int, input().split()))
    m2 = []
    for i in range(p):
        b = []
        for j in range(q):
            b.append(int(input("Enter the number")))
        m2.append(b)

    for i in range(p):
        for j in range(q):
            print(m2[i][j], end=" ")
        print()
    if m == p and n == q:
        result = [[0 for i in range(n)] for i in range(p)]

        for i in range(m):
            for j in range(n):
                result[i][j] = m1[i][j] + m2[i][j]
        print("The sum is: ")
        for r in result:
            print(r)
    else:
        print("Addition not possible")
if m==2:
    print("Button for multiplication is pressed")
    print("Enter the order of 1st matrix")
    m, n = list(map(int, input().split()))
    m1 = []
    print("Enter value row wise")
    for i in range(m):
        print("Enter row", i, "value:")
        row = list(map(int, input().split()))
        m1.append(row)
    print("Enter order of 2nd matrix:")
    p, q = list(map(int, input().split()))
    print("Enter value row wise")
    m2 = []
    for j in range(p):
        print("Enter row", j, "value:")
        row = list(map(int, input().split()))
        m2.append(row)
    print("Matrix 1:", m1)
    print("Matrix 2:", m2)
    if n == p:
        resultant = []
        for i in range(m):
            row = []
            for j in range(q):
                row.append(0)
            resultant.append(row)
        print("Matrix Multiplication: ")
        for i in range(m):
            for j in range(q):
                for k in range(n):
                    resultant[i][j] += m1[i][k] * m2[k][j]
        for row in resultant:
            print(row)
    else:
        print("Matrix Multiplication not possible")
if m==3:
    print("Button for subtraction is pressed")
    print("Order of first matrix")
    m, n = list(map(int, input().split()))
    m1 = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input("Enter the number")))
        m1.append(a)

    for i in range(m):
        for j in range(n):
            print(m1[i][j], end=" ")
        print()

    print("Order of second matrix")
    p, q = list(map(int, input().split()))
    m2 = []
    for i in range(p):
        b = []
        for j in range(q):
            b.append(int(input("Enter the number")))
        m2.append(b)

    for i in range(p):
        for j in range(q):
            print(m2[i][j], end=" ")
        print()
    if m == p and n == q:
        result = [[0 for i in range(n)] for i in range(p)]

        for i in range(m):
            for j in range(n):
                result[i][j] = m1[i][j] - m2[i][j]
        print("The diff. is: ")
        for r in result:
            print(r)
    else:
        print("Subtraction not possible")
if m==4:
    print("Button for inverse is pressed")
    import numpy as np

    print("Enter the order of the matrix")
    m = int(input())
    m1 = []
    for i in range(m):
        a = []
        for j in range(m):
            a.append(int(input("Enter the number")))
        m1.append(a)

    for i in range(m):
        for j in range(m):
            print(m1[i][j], end=" ")
        print()
    m1 = np.array(m1)
    print(np.linalg.inv(m1))
