def main():
    """Main function takes user input and feeds it to other function"""
    score = float(input("Enter score: "))
    print(determine_grade(score))


def determine_grade(score):
    """Determines user grade based on score"""
    if score > 100 or score < 0:
        print("Invalid")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
