def square(n):
    return n * n

def average(a, b, c):
    return (a + b + c) / 3

num = int(input("Enter Number: "))
print("Square =", square(num))

x = float(input("Enter First Number: "))
y = float(input("Enter Second Number: "))
z = float(input("Enter Third Number: "))

print("Average =", average(x, y, z))