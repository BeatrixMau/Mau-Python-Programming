num_integers = int(input("Enter The Amount of Integers: "))
integers = []

for n in range(num_integers):
    num = int(input(f"Enter integer {n+1}: "))
    integers.append(num)
    
print(f"Total number of items in the list: {len(integers)}")

print(f"Last item in the list: {integers[-1]}")

print("List in reverse order:", end=" ")
for num in reversed(integers):
    print(num, end=" ")
print()

contains_five = any(num == 5 for num in integers)
if contains_five:
    print("Yes, the list contains a 5.")
else:
    print("No, the list does not contain a 5.")

integers = integers[1:-1]
integers.sort()

print("List after removing first and last items and sorting:", end=" ")
for num in integers:
    print(num, end=" ")
print()