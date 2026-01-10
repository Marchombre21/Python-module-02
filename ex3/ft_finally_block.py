# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_finally_block.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/10 09:03:47 by bfitte            #+#    #+#             #
#    Updated: 2026/01/10 09:03:47 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

class PlantNameError(Exception):
    def __init__(self):
        message = "Error: Cannot water None - invalid plant!"
        super().__init__(message)


class Plant():
    def __init__(self, name: str):
        self.name = name


def water_plants(plant_list: list):
    print("Opening watering system")
    for plant in plant_list:
        if plant.name:
            print(f"Watering {plant.name}")
        else:
            raise PlantNameError


def test_watering_system():
    name_list = ["Tulipe", "Orthensia", "Marguerite"]
    plant_list: list[Plant] = []
    no_name_list = ["Tomate", None, None]
    no_plant_list = []
    for name in name_list:
        plant_list.append(Plant(name))
    for name in no_name_list:
        no_plant_list.append(Plant(name))
    print("Testing normal watering...")
    try:
        water_plants(plant_list)
        print("Watering completed successfully!\n")
    except PlantNameError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    print("Testing with error...")
    try:
        water_plants(no_plant_list)
        print("Watering completed successfully!\n")
    except PlantNameError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
