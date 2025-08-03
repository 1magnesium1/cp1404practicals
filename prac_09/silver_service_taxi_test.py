from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Corolla 1", 100, 10)
    taxi.drive(20)
    print(taxi)
    print(taxi.get_fare())


main()
