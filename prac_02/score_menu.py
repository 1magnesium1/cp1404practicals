MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Main function that prints menu and takes user input"""
    score = -1
    print(MENU)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "G":
            score = get_valid_score()
        elif user_choice == "P":
            if score == -1:
                print(f"Set score first!")
            else:
                determine_grade(score)
        elif user_choice == "S":
            if score == -1:
                print(f"Set score first!")
            else:
                print_stars(score)
        else:
            print(f"Invalid choice")
        print(MENU)
        user_choice = input(">>>").upper()
    print("Goodbye :-)")


def get_valid_score():
    """Gets a score from user between zero and one hundred inclusive"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        score = input("Enter score: ")
    return score


def determine_grade(score):
    """Determines user grade based on score"""
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_stars(score):
    """Prints same number of stars as user score"""
    for i in range(score):
        print("*", end=" ")
    print()


main()
