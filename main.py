"""
Create a login program that I can use to add and verify 
usernames and passwords.

A dictionary seems like the appropriate item to store 
this information.
"""

accounts = {"ryanhawkins": "beastmode", "testname": "testpass"}


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_status():
        print()
        print("[1] Sign in (current user)")
        print("[2] Sign up (new user)")
        user_status = input("Choose selection: ")
        if user_status == "1":
            Account.sign_in()
            # Account.verify_username()
            # Account.verify_password()
        elif user_status == "2":
            Account.sign_up()
        else:
            user_status()

    def sign_up():
        print("\nWe're glad to have you join us.")
        new_username = Account.approve_new_username()
        new_password = Account.approve_new_password()
        accounts[new_username] = new_password

    def approve_new_username():
        accepted_name = False
        while not accepted_name:
            print("\nYour username must be between 7 and 11 characters long.")
            new_username = input("Choose a username: ")
            if len(new_username) < 7 or len(new_username) > 11:
                print(
                    "Your username must be between 7 and 11 characters long.")
                pass
            elif new_username in accounts.keys():
                print(f"'{new_username}' is already used.")
                pass
            else:
                accepted_name = True
                print(f"The username '{new_username}' was accepted.")
                return new_username

    def approve_new_password():
        accepted_password = False
        # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # letters = []
        new_password_tries = 0
        while not accepted_password:
            new_password = input("Select a password: ")
            if len(new_password) > 5 and len(new_password) < 15:
                accepted_password = True
                return new_password
            else:
                print(
                    "Your password must be between 6 and 14 characters long.")
            new_password_tries += 1
            if new_password_tries >= 3:
                password_help = input(
                    "Would you like an approved password generated for you? "
                ).lower()
                new_password_tries = 0
                if password_help in ["y", "yes", "yeah"]:
                    pass
                if password_help in ["n", "no"]:
                    Account.approve_new_password()

    # def sign_in():
    #     Account.verify_username()
    #     Account.verify_password()
    # def verify_username():
    #     return_username = input("\nEnter your username: ")
    #     if return_username in accounts.keys():
    #         username = return_username
    #         return username
    #         Account.verify_password()
    #     else:
    #         print(f"'{return_username}' is not recognized.")
    #         print("Please, try again.")
    #         Account.user_status
    # def verify_password():
    #     password = input("Enter password: ")
    #     if password in accounts.values(username):
    #         print("Access Granted.")

    def sign_in():
        username_verified = False
        while not username_verified:
            username = input("\nEnter your username: ")
            if username in accounts.keys():
                username_verified = True
            else:
                print(f"{username} is not recognized.")
                print("Please, try again.")

        password_verified = False
        while not password_verified:
            password = input("Enter your password: ")
            if password == accounts[username]:
                print("Access Granted")
            else:
                print("Access Denied")
            # if password in accounts.values(username):
            #     print("Access Granted")
            # else:
            #     print("The password and username do not match.")
            #     Account.sign_in()

    def change_password():
        pass


def main():

    intro()
    Account.user_status()


def intro():
    intro_message = "Welcome to Hawkins Online."
    print()
    print(intro_message)
    print("-" * len(intro_message))


if __name__ == "__main__":
    main()

### Verification of New Account ###
# print()
# for key, value in accounts.items():
#     print(key, value)
