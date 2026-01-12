# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_management.py                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/10 11:57:55 by bfitte            #+#    #+#             #
#    Updated: 2026/01/10 11:57:56 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

class GardenError(Exception):
    def __init__(self, detail: str = None):
        message = f"Caught {self.__class__.__name__}: "
        if detail:
            message += f"{detail}"
        super().__init__(message)


class DoubleError(GardenError):
    pass


class EmptyTank(GardenError):
    pass


class UnknowGarden(GardenError):
    pass


class UnknowPlant(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunError(GardenError):
    pass


class Plant:
    """Mother class for all plants in exercice"""
    def __init__(self, name: str, height: int, age: int):
        self.__name = name.capitalize()
        self.__height = height
        self.__age = age
        self.__water_level = 0
        self.__sun_level = 0

    def info_plant(self):
        print(f"- {self.__name}: {self.__height}cm.")

    def set_height(self, size: int):
        """Modify the plant's height after check if it's a valid value"""
        if (self.__height + size) < 0:
            raise ValueError("Error setting height: Height cannot be negative."
                             )
        else:
            self.__height += size

    def set_age(self, days: int):
        """Modify the plant's age after check if it's a valid value"""
        if (self.__age + days) < 0:
            raise ValueError("Error setting age: Age cannot be negative.")
        else:
            self.__age += days

    def set_water(self, value: int):
        """Modify the plant's water level after check if it's a valid value"""
        if (self.__water_level + value) < 0:
            raise ValueError("Error setting water level:"
                             " Water level cannot be negative.")
        else:
            self.__water_level += value

    def set_sun(self, value: int):
        """Modify the plant's sun level after check if it's a valid value"""
        if (self.__sun_level + value) < 0:
            raise ValueError("Error setting sun level:"
                             " Sun level cannot be negative.")
        else:
            self.__sun_level += value

    def get_water(self):
        return self.__water_level

    def get_sun(self):
        return self.__sun_level

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height


class Garden():
    """Class for garden which contain all possible operations to do"""
    def __init__(self, name: str):
        self.__name = name.capitalize()
        self.__plants: list[Plant] = []
        self.growth = 0
        self.regular = 0

    def add_plant(self, name: str, height: int, age: int):
        plant = Plant(name, height, age)
        self.__plants.append(plant)
        print(f"Added {name.capitalize()} to {self.__name}'s garden.")
        self.regular += 1

    def get_name(self):
        return self.__name

    def watering(self):
        """Simulate watering the garden and call functions which
        modify age and height of plants
        """
        print(f"{self.__name} is helping all plants grow...")
        for plant in self.__plants:
            self.growth += 1
            plant.set_height(1)
            plant.set_age(1)
            plant.set_water(5)
            plant.set_sun(5)
            name = plant.get_name()
            print(f"{name} grew 1cm")

    def get_plants(self) -> list[Plant]:
        return self.__plants

    def garden_report(self):
        """Collect and print all garden's datas"""
        print(f"=== {self.__name}'s garden report ===\n")
        print("Plants in garden:")
        result = 0
        for plant in self.__plants:
            result += 1
            plant.info_plant()
        print("")
        print(f"Plants added: {result}, Total growth: {self.growth}cm\n")


class GardenManager:
    def __init__(self):
        self.__gardens: list[Garden] = []
        self.__tank_level = 0

    def add_garden(self, name: Garden):
        """Add garden to the gardens list"""
        try:
            garden_name = name.get_name()
            for garden in self.__gardens:
                name_garden = garden.get_name()
                if name_garden == garden_name:
                    raise DoubleError("Impossible to add a garden with the"
                                      " same name of a previous one")
            self.__gardens.append(name)
            print(f"{garden_name}'s garden created.")
        except GardenError as e:
            print(e)

    def set_tank_level(self, value: int):
        if (self.__tank_level + value) < 0:
            raise ValueError("You cannot remove more water than the tank "
                             f"contain ({self.__tank_level} liters)")
        self.__tank_level += value
        print(f"Tank level is updated ({self.__tank_level} liters)")

    def add_plant_to_garden(self, name: str, height: int, age: int,
                            garden_name: str):
        try:
            if name == "":
                raise ValueError("Error adding plant: Plant name "
                                 "cannot be empty!"
                                 )
            for garden in self.__gardens:
                name_garden = garden.get_name()
                if name_garden == garden_name.capitalize():
                    garden.add_plant(name, height, age)
        except ValueError as e:
            print(e)

    def check_health(self, name: str, plant_name: str):
        """Check if the attribute's values are in the healthy range"""
        try:
            print("\nChecking plant health...")
            name_error = 1
            for garden in self.__gardens:
                name_garden = garden.get_name()
                if name_garden == name.capitalize():
                    name_error = 0
                    garden_plants = garden.get_plants()
                    name_plant_error = 1
                    for plant in garden_plants:
                        name_plant = plant.get_name()
                        if plant_name.capitalize() == name_plant:
                            name_plant_error = 0
                            water_level = plant.get_water()
                            sun_level = plant.get_sun()
                            if water_level > 10:
                                raise WaterError(f"Error checking {name_plant}"
                                                 f": Water level {water_level}"
                                                 " is too high (max 10)")
                            if water_level < 5:
                                raise WaterError(f"Error checking {name_plant}"
                                                 f": Water level {water_level}"
                                                 " is too low (min 5)")
                            if sun_level > 10:
                                raise SunError(f"Error checking {name_plant}:"
                                               f" Water level {sun_level} is "
                                               "too high (max 10)")
                            if sun_level < 5:
                                raise WaterError(f"Error checking {name_plant}"
                                                 f": Sun level {sun_level}"
                                                 " is too low (min 5)")
                            print(f"{name_plant}: healthy (water: "
                                  f"{water_level}, sun: {sun_level})")
            if name_error == 1:
                raise UnknowGarden(f"No garden named {name}")
            if name_plant_error == 1:
                raise UnknowPlant(f"No plant named {plant_name} "
                                  f"in {name}'s garden")
        except GardenError as e:
            print(e)

    def watering_garden(self, name: str):
        """Simulate watering the garden and call functions which
        modify age and height of plants
        """
        try:
            print("\nOpening watering system")
            if self.__tank_level < 10:
                raise EmptyTank("There is not enough water in tank.")
            for garden in self.__gardens:
                name_garden = garden.get_name()
                if name_garden == name.capitalize():
                    garden.watering()
                    self.set_tank_level(-5)
        except GardenError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)\n")

    def check_tank_level(self):
        try:
            print("\nTesting error recovery...")
            if (self.__tank_level < 5):
                raise GardenError("Not enough water in "
                                  "tank to watering a garden")
        except GardenError as e:
            print(e)
        finally:
            print("System recovered and continuing...")


def main():
    plants_to_add = [
        ["tulipe", 5, 3, "alice"],
        ["", 5, 3, "alice"],
        ["tomate", 6, 7, "gerard"],
        ["géranium", 25, 32, "alice"]
    ]
    gardener = GardenManager()
    gardener.add_garden(Garden("alice"))
    gardener.add_garden(Garden("gerard"))
    gardener.add_garden(Garden("alice"))
    print("\nAdding plants to garden...")
    for plant in plants_to_add:
        gardener.add_plant_to_garden(plant[0], plant[1], plant[2], plant[3])
    print("")
    gardener.check_health("bruno", "tulipe")
    gardener.check_health("alice", "bégonia")
    gardener.check_health("alice", "tulipe")
    gardener.check_tank_level()
    gardener.watering_garden("alice")
    gardener.set_tank_level(25)
    gardener.watering_garden("alice")
    gardener.check_health("alice", "tulipe")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    main()
