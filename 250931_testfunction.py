def string_input(prompt=""):
    return input(prompt)

num_strings = int(input("Amount of strings? "))
strings = []

for i in range(num_strings):
    s = string_input(f"Enter string {i+1}: ")
    strings.append(s)

combined = " ".join(strings)
print(combined)
