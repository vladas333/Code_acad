# Create a variables containing strings for username and password. 
# Start Endless loop allowing to enter username and password. 
# If credentials are correct stop endless loop and print 
# greeting message.

name_list = ["Algis", "Tomas", "Petras"]
passw_list = ["sigla", "samot", "sartep"]


a = 0
while a < 1:
    user_input_n = input("Please enter your name: ")
    if user_input_n in name_list:
        print(user_input_n)
        user_input_p = input("Please enter your password: ")    
        if user_input_p in passw_list:
            a += 1
            print("Correct")
        continue

    

