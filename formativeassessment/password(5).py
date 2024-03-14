password = "ILoveYou3000"
attempts = 0

while attempts < 5:
    user = input("Enter Password: ")

    if user == password:
        print("You have successfully logged in")

    else:
        print("Invalid Password. Try again")
        attempts += 1
    
    if attempts == 5:
        print("You are blocked from the system.")