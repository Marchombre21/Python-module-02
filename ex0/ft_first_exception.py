# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_first_exception.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/08 10:40:09 by bfitte            #+#    #+#             #
#    Updated: 2026/01/08 10:40:09 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

def check_temperature(temp_str: str):
    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
        else:
            if temp < 0:
                print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            else:
                print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    except ValueError:
        print("Oops!  That was no valid temperature.  Try again...")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    for n in range(4):
        temp = input("\nTesting temperature: ")
        check_temperature(temp)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
