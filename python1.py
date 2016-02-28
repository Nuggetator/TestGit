#factorial function
num = int(raw_input("Please enter a number fo factorialization: "))
factorial = 0
while num > 0:
    factorial += num
    num -= 1
print factorial
