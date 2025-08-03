from prac_09.unreliable_car import UnreliableCar


def main():
    """Test unreliable car"""

    reliable_car = UnreliableCar("Camery Altise", 100, 80)
    unreliable_car = UnreliableCar("VW Polo", 100, 20)

    for i in range(1, 10):
        print(f"{reliable_car.name} drove {reliable_car.drive(i)}km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(i)}km")

    print(reliable_car)
    print(unreliable_car)


main()
