from decimal import *



num1 = Decimal(10)
num2 = Decimal("26.897323")


print(num1, num2, sep=" | ")
print(num1 + num2)
num1 = num1 / num2
print(num1)

getcontext().prec = 6

num1 = num1 / num2
print(num1)

# num1 = Decimal("10.666666666666")
num1 = Decimal("10.666666666666")
num2 = num1.quantize(Decimal("1.00"))

print(num2)

