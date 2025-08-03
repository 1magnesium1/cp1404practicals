from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi


def main():
    """"This is a taxi simulator with menu options"""

    menu = "(Q)uit (C)hoose taxi (D)rive"
    total_bill = 0
    taxis = [Taxi("Camery Altise", 100), SilverServiceTaxi("Urus", 100, 15),
             SilverServiceTaxi("Phantom", 100, 20)]
    current_taxi = None
    print("Lets drive")
    print(menu)
    menu_choice = input(">>> ".lower())
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Your taxi options: ")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose your taxi: "))
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi")

        elif menu_choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Enter distance to drive: "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"The cost of current trip is: ${trip_cost}.")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi first.")
        else:
            print("Invalid choice")
        print(menu)
        menu_choice = input(">>> ".lower())

    print(f"Running tab: ${total_bill}")
    print(f"Current available taxis:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Displays taxis in a numbered list"""
    for i, taxi in enumerate(taxis):
        print(f"{i}.  {taxi}")


main()
