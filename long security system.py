correct_pass ="admin123"
for i in range(3):
    password = input("enter your password:")
    if password == correct_pass:
        print("login successful")
        break
    else:
        print("incorrect password")
        if i == 2:
            print("account locked")