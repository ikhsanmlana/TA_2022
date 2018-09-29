#Pascal's Triangle

import math
def combination(n,k):
    return int((math.factorial(n))/((math.factorial(k)) * (math.factorial (n-k))))

def pascal(rows):
    num = []
    number = 0
    for number in range(rows):
        row = []
        for element in range (number + 1):
            row.append(combination(number,element))
        num.append(row)
    return num

for row in pascal(int(input("How many rows do you want? "))):
    print(row)

