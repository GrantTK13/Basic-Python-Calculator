import time

print(" ")

print("What is your first number?")

num1 = int(input())

print(" ")

print("What is your operation? (Use operation symbol!)")

operation = input()

print(" ")

print("What is your second number?")

num2 = int(input())

print(" ")

if operation == "+":
  print("The answer is:")
  print(num1 + num2)
elif operation == "-":
  print("The answer is:")
  print(num1 - num2)
elif operation == "*":
  print("The answer is:")
  print(num1 * num2)
elif operation == "/":
  print("The answer is:")
  print(num1 / num2)
else:
  print("Sorry, but that operation doesn't exist!")

time.sleep(5)