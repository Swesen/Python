# 1
def SqrRoot(x):
    return x ** (1 / 2)

# x = 4
# print(SqrRoot(x))


# 2
def TranslateNumberToText(x):
    translate = ["Noll", "Ett", "Två", "Tre", "Fyra",
                 "Fem", "Sex", "Sju", "Åtta", "Nio"]
    return translate[x]

# x = 4
# print(TranslateNumberToText(x))


# 3
def PrintSquareCube():
    for i in range(1, 11):
        print(str(i) + " " + str(i ** 2) + " " + str(i ** 3))

# PrintSquareCube()


# 4
def PrintTriangularNumberA(x):
    return (x * (x + 1)) / 2


# 5
def PrintTriangularNumberB(x):
    y = 0
    for i in range(x):
        y += i + 1

    return y

# x = 5
# print("Formula: " + str(PrintTriangularNumberA(x)) + " Loop: " + str(PrintTriangularNumberB(x)))


# 6
def SumPrimes(start, end):
    SumOfPrimes = 0
    for i in range(start, end + 1):
        for j in range(2, i + 1):
            if (j >= i):
                SumOfPrimes += i
                break
            elif (i % j == 0):
                break

    return SumOfPrimes

# m = 0
# n = 30
# print(SumPrimes(m, n))