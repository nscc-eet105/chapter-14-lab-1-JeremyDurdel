#Jeremy Durdel
#Chapter 14 Lab 1
#07/13/2025

class Vehicle:
    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        self.__speed += 1

    def decelerate(self):
        self.__speed -= 1

    def display_speed(self):
        print(f"Current speed: {self.__speed}")


def main():
    car = Vehicle()

    print("Accelerating..")
    car.accelerate()
    car.display_speed()

    print("Accelerating..")
    car.accelerate()
    car.display_speed()

    print("Decelerating..")
    car.decelerate()
    car.display_speed()

    print("Decelerating..")
    car.decelerate()
    car.display_speed()

if __name__ == "__main__":
    main()