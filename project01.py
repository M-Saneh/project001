name = input("plz inter your name(in letters only):")
age = input ("plz inter your age(in numbers only): ")
while not str.isalpha(name):
    print("This is not a valid name,please inter a correct name:")
    name = input("plz inter your name:")
while not str.isdigit(age):
    print("This is not a valid age,please inter a correct age:")
    age = input("plz inter your age:")
    
print(f"Your name is {name} and your age is {age}")