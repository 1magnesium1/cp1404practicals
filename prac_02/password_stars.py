MINIMUM_LENGTH = 8


def main():
    """Main function"""
    password = get_password(MINIMUM_LENGTH)
    print_stars(password)


def print_stars(password):
    """Prints stars based on length of password"""
    print('*' * len(password))


def get_password(min_length):
    """Gets user password over minimum length"""
    password = input("Enter your password: ")
    while len(password) < min_length:
        password = input("Password too short. Enter your password: ")
    return password
