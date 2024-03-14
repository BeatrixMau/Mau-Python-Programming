user_passwords = {
    "beatrix_mau": "mau2004",
    "alvina_kue": "123nana",
    "valen_george": "1234567",
    "jane_jackson": "JLO11",
    "najwaILY": "fatin2003",
    "IZZIAN": "nurulIzz4",
    "AnAtAsIa": "myQUEENisMYMUM",
    "AARon": "AARONAziz123",
    "RiRi": "wantmyumbrella?",
    "MattMaltese": "asthew0rldc@ves1n",
    
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in user_passwords:
    if user_passwords[username] == password:
        print("You are now logged in to the system for python.")
    else:
        print("Invalid password.")
else:
    print("You are not a valid user of the system.")