#!/usr/bin/env/ python3

# Created by Malcolm Tompkins
# Created on April 28, 2021
# Calculates the cost of pizza with user input diameter


def main():
    # Function that calculates surface area of the pyramid
    width = int(input("Input width of pyramid (cm): "))
    height = int(input("Input height of the pyramid (cm): "))
# User input
    Base_Area = width * width
    Lateral_area = (height * width) / 2
    Total_area = Base_Area + Lateral_area
# Process
    print("The area of the base is: {} cm²".format(Base_Area))
    print("The lateral area is: {} cm²".format(Lateral_area))
    print("The total surface area is: {} cm²".format(Total_area))
# Output


if __name__ == "__main__":
    main()
