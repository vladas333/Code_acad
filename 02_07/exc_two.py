#Create a database (List of privileged users) print a specific message 
# with a personal greeting if the user is a privileged and just "Welcome otherwise"


privileged_users = ["Tom", "Albert", "Stephen", "John"]
# user = "Johnny"
user = str(input(" Enter your name: "))
if user in privileged_users:
    print(f"Welcome VIP...{user}...")
else:
    print(f"Welcome GUEST...{user}...")