
a = int(input("a=")) 
b = int(input("b="))
print(f"Before swap a={a}, b={b}")
a = a+b
b = a - b
a = a - b
print(f"After swap a={a}, b={b}")

