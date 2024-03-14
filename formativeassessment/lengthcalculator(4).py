length = float(input("Enter the Length in CM: "))

if length < 0:
    print("Invalid Input")
    
elif length >= 1:
    inches = length / 2.54
    print(f"{length} cm is equal to {inches} inches.")
    

