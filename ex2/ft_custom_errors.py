# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_custom_errors.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/10 06:34:55 by bfitte            #+#    #+#             #
#    Updated: 2026/01/10 06:34:55 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

class GardenError(Exception):
    def __init__(self, detail: str = None):
        message = f"Caught a {self.__class__.__name__}: "
        if (detail):
            message += f"{detail}"
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_water(value: int):
    if value < 10:
        raise WaterError("Not enough water in the tank!")
    else:
        print("All is good!")


def test_wilting(value: int):
    if value != 1:
        raise PlantError("The tomato plant is wilting!")
    else:
        print("There is no wilting")


def main():
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting WaterError...")
    try:
        test_water(5)
    except WaterError as e:
        print(e)
    try:
        test_water(11)
    except WaterError as e:
        print(e)
    print("\nTesting PlantError...")
    try:
        test_wilting(1)
    except PlantError as e:
        print(e)
    try:
        test_wilting(5)
    except PlantError as e:
        print(e)
    print("\nTesting catching all garden errors...")
    try:
        test_water(5)
    except GardenError as e:
        print(e)
    try:
        test_wilting(5)
    except GardenError as e:
        print(e)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
