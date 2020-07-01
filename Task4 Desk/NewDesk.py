a = int(input("Enter Total count Pupils for 1 class: "))
b = int(input("Enter Total count Pupils for 2 class: "))
c = int(input("Enter Total count Pupils for 3 class: "))
print("RESULT: Number of desks for Pupils: ", a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)