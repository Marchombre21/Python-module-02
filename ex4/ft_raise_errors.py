# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_raise_errors.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/10 11:35:43 by bfitte            #+#    #+#             #
#    Updated: 2026/01/10 11:35:44 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if not (1 < water_level < 10):
        raise ValueError("Error: Water level 15 is too high (max 10)")
    if not (2 < sunlight_hours < 12):
        raise ValueError("Error: Sunlight hours 0 is too low (min 2)")
    print(f"Plant {plant_name} is healthy!")


def test_plant_checks():
    print("\nTesting good values...")
    try:
        check_plant_health("Tulipe", 5, 11)
    except ValueError as e:
        print(e)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 11)
    except ValueError as e:
        print(e)
    print("\nTesting bad water level...")
    try:
        check_plant_health("Tulipe", 0, 11)
    except ValueError as e:
        print(e)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Tulipe", 5, 13)
    except ValueError as e:
        print(e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
