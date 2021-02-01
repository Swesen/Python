import math

# a = b / tan(&)
# c^2 = a^2 + b^2
# c = squareRoot((b / tan(b))^2 + b^2)


def CalculateLadderLength(height, angle):
    return math.ceil(math.sqrt(math.pow(height / math.tan(math.radians(angle)), 2) + math.pow(height, 2)))


print(CalculateLadderLength(3.5, 70))
print(CalculateLadderLength(2, 45))
print(CalculateLadderLength(2, 25))