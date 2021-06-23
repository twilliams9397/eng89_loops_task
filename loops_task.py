for _ in range(10):
    print("hello")

list_names = [] # setting initial empty list
for _ in range(5):
    name = input("What is your name?  ").capitalize()
    list_names.append(name)

print(list_names)

list_names_lower = []

for names in list_names:
    lower_name = names.lower()
    list_names_lower.append(lower_name)

print(list_names_lower)

for names in list_names_lower:
    if len(names) % 2 == 0:
        print(f"{names} is even!")
    else:
        print(f"{names} is not even!")

