"""
Homework 3: Test Game Helper
============================
Student:  Tommer Ben-Joseph
Semester: Fall 2023

Run tests on game_helper
"""

import game_helper


def test_area_sq() -> int:
    """Test function for area_sq"""
    print("Testing area_sq")
    fail_count = 0
    if (game_helper.area_sq(5) != 25.0):
        fail_count += 1
        print("....Failed area_sq(5)")
    if (game_helper.area_sq(10.5) != 110.25):
        fail_count += 1
        print("....Failed area_sq(10.5)")
    if (fail_count < 1):
        print("....all tests passed for area_sq()")
    return fail_count


def test_area_rec() -> int:
    """Test function for area_rec"""
    print("Testing area_rec")
    fail_count = 0
    if (game_helper.area_rec(5, 4) != 20.0):
        fail_count += 1
        print("....Failed area_rec(5,4)")
    if (game_helper.area_rec(10, 5) != 50.0):
        fail_count += 1
        print("....Failed area_rec(10,5)")
    if (fail_count < 1):
        print("....all tests passed for area_rec()")
    return fail_count


def test_vol_cube() -> int:
    """Test function for vol_cube"""
    print("Testing vol_cube")
    fail_count = 0
    if (game_helper.vol_cube(5, 5, 5) != 125.0):
        fail_count += 1
        print("....Failed vol_cube(5,5,5)")
    if (game_helper.vol_cube(10, 50, 10) != 5000.0):
        fail_count += 1
        print("....Failed vol_cube(10,50,10)")
    if fail_count < 1:
        print("....all tests passed for vol_cube()")
    return fail_count


def test_area_triangle() -> int:
    """Test function for area_triangle"""
    print("Testing area_triangle")
    fail_count = 0
    if (game_helper.area_triangle(10, 5) != 25.0):
        fail_count += 1
        print("....Failed area_triangle(10,5)")
    if (game_helper.area_triangle(6, 8) != 24.0):
        fail_count += 1
        print("....Failed area_triangle(6,8)")
    if fail_count < 1:
        print("....all tests passed for area_triangle()")
    return fail_count


def test_vol_pyramid() -> int:
    """Test function for vol_pyramid"""
    print("Testing vol_pyramid")
    fail_count = 0
    if (game_helper.vol_pyramid(4, 6) != 32.0):
        fail_count += 1
        print("....Failed vol_pyramid(4,6)")
    if (game_helper.vol_pyramid(3, 2) != 6.0):
        fail_count += 1
        print("....Failed vol_pyramid(3,2)")
    if fail_count < 1:
        print("....all tests passed for vol_pyramid()")
    return fail_count


def test_can_add() -> int:
    """Test function for can_add"""
    print("Testing can_add")
    fail_count = 0
    if (game_helper.can_add(25, 5, 31) != True):
        fail_count += 1
        print("....Failed can_add(25,5,31)")
    if (game_helper.can_add(15, 5, 3) != False):
        fail_count += 1
        print("....Failed can_add(15,5,3)")
    if (fail_count < 1):
        print("....all tests passed for can_add()")
    return fail_count


def test_roll_dice() -> int:
    """Test function for roll_dice"""
    print("Testing roll_dice")
    fail_count = 0
    first_test = game_helper.roll_dice(20)
    second_test = game_helper.roll_dice(110)
    if not (1 <= first_test <= 20):
        fail_count += 1
        print("....Failed roll_dice(20)")
    if not (1 <= second_test <= 6):
        fail_count += 1
        print("....Failed roll_dice(110)")
    if (fail_count < 1):
        print("....all tests passed for roll_dice()")
    return fail_count


### example main, use as you want. 
def main() -> None:
    print("Running all tests")
    fail_count = 0

    fail_count += test_area_sq()
    fail_count += test_area_rec()
    fail_count += test_vol_cube()
    fail_count += test_area_triangle()
    fail_count += test_vol_pyramid()
    fail_count += test_can_add()
    fail_count += test_roll_dice()

    if (fail_count > 0):
        print(f"Failed {fail_count} tests.")



if __name__ == '__main__':
    main()
