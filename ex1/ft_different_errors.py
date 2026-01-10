# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_different_errors.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/08 13:42:14 by bfitte            #+#    #+#             #
#    Updated: 2026/01/08 13:42:14 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

def garden_operations(test: str):
    if test == "value":
        int("abc")
    elif test == "zero":
        print(f"{10/0}")
    elif test == "file":
        file_object = open("unknow_file.py", 'r')
        file_object.close()
    elif test == "key":
        dictionnary = dict(number=5, word="coucou")
        print(f"{dictionnary['issue']}")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    tests = ["value", "key", "zero", "file"]
    for test in tests:
        try:
            garden_operations(f"{test}")
        except ValueError as e:
            print("Testing ValueError...")
            print(f"Caught ValueError: {e}")
        except KeyError as e:
            print("Testing KeyError...")
            print(f"Caught KeyError: {e}")
        except ZeroDivisionError as e:
            print("Testing ZeroDivisionError...")
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print("Testing FileNotFoundError..")
            print(f"Caught FileNotFoundError: {e}")
    print("\n=== Garden Multiple Error Types Demo ===\n")
    for test in tests:
        try:
            garden_operations(test)
        except (
            ValueError, KeyError,
            ZeroDivisionError, FileNotFoundError
        ) as e:
            print(f"Caught the error {e}, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
