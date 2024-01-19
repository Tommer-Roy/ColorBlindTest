""" 
Student: Tommer Ben-Joseph
Term: Fall 2023

Compares two colors, both normal, and with various color blindness conditions applied

"""
import math

MIN_DIFFERENCE = .20


# provided functions, no need to change

def delta(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> float:
    """Uses the following formula to compare two different colors. This
    is a simplified way to compare two colors as it doesn't take
    into account hue or saturation differences. If you are curious
    about a more standard approach, one should look up the CIEDE2000 formula. 

    euclidean = (R_1 - R_2)^2 + (G_1 - G_2)^2 + (B_1 - B2)^2
    euclidean = sqrt(euclidean)  # the two lines are known as the euclidean distance and common for a lot of things
    scaled = floor(euclidean) / 441  #scales the distance between 0 and 1

    Args:
        red_one (int): a color range between 0 and 255 representing the red for the first color
        green_one (int): a color range between 0 and 255 representing the green for the first color
        blue_one (int):a color range between 0 and 255 representing the blue for the first color
        red_two (int): a color range between 0 and 255 representing the red for the second color
        green_two (int): a color range between 0 and 255 representing the green for the second color
        blue_two (int): a color range between 0 and 255 representing the blue for the second color


    Returns:
        float: a value between 0 and 1, representing how different colors are. Lower numbers are more similar. 
    """
    return int(math.sqrt((red_one - red_two) ** 2 + 
                         (green_one - green_two) ** 2 + 
                         (blue_one - blue_two) ** 2)) / 441

def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """Converts an RBG color to a HEX string value often used for HTML color pallets. 

    The conversion format string is  f"#{red:02x}{green:02x}{blue:02x}"

    Args:
        red (int): red color value
        green (int): green color value
        blue (int): blue color value

    Returns:
        str: the formatted string
    """
    return f"#{red:02x}{green:02x}{blue:02x}"

## end provided functions

# add your functions here - remember to indent properly! so def 
# starts on the far side, then everything is indented under for each function, use the other functions as examples

def different_colors(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """
    Compares two color RGB values to determine if they are different enough.

    Args:
        red_one (int): A color range between 0 and 255 representing the red component of the first color.
        green_one (int): A color range between 0 and 255 representing the green component of the first color.
        blue_one (int): A color range between 0 and 255 representing the blue component of the first color.
        red_two (int): A color range between 0 and 255 representing the red component of the second color.
        green_two (int): A color range between 0 and 255 representing the green component of the second color.
        blue_two (int): A color range between 0 and 255 representing the blue component of the second color.

    Returns:
        bool: True if the difference between the two colors is greater than .20 True means the colors are different.
    """
    color_difference = delta(red_one, green_one, blue_one, red_two, green_two, blue_two)
    return color_difference > MIN_DIFFERENCE


def check_protanopia(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """
    Compares two RGB values to determine if they are too similar when viewed by someone with protanopia.

    Protanopia is when there is 0 red and greens, and only blues, so all colors become their blue value when viewed by someone with protanopia.

    Args:
        red_one (int): A color range between 0 and 255 representing the red component of the first color.
        green_one (int): A color range between 0 and 255 representing the green component of the first color.
        blue_one (int): A color range between 0 and 255 representing the blue component of the first color.
        red_two (int): A color range between 0 and 255 representing the red component of the second color.
        green_two (int): A color range between 0 and 255 representing the green component of the second color.
        blue_two (int): A color range between 0 and 255 representing the blue component of the second color.

    Returns:
        bool: True if the colors are too similar when viewed by someone with protanopia.
    """
    # When viewed by someone with protanopia, all colors become their blue value
    blue_value_one = blue_one
    blue_value_two = blue_two

    # Compare the blue values using the `different_colors` function
    return different_colors(0, 0, blue_value_one, 0, 0, blue_value_two)


def check_deuteranopia(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """
    Compares two RGB values to determine if they are too similar when viewed by someone with deuteranopia.

    Deuteranopia is defined as when someone loses all greens in an RGB value scheme.

    Args:
        red_one (int): A color range between 0 and 255 representing the red component of the first color.
        green_one (int): A color range between 0 and 255 representing the green component of the first color.
        blue_one (int): A color range between 0 and 255 representing the blue component of the first color.
        red_two (int): A color range between 0 and 255 representing the red component of the second color.
        green_two (int): A color range between 0 and 255 representing the green component of the second color.
        blue_two (int): A color range between 0 and 255 representing the blue component of the second color.

    Returns:
        bool: True if the colors are too similar when viewed by someone with deuteranopia.
    """
    # When viewed by someone with deuteranopia, all greens become 0
    red_value_one = red_one
    red_value_two = red_two
    blue_value_one = blue_one
    blue_value_two = blue_two

    # Compare the adjusted colors using the `different_colors` function
    return different_colors(red_value_one, 0, blue_value_one, red_value_two, 0, blue_value_two)


def check_tritanopia(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """
    Compares two RGB values to determine if they are too similar when viewed by someone with tritanopia.

    Tritanopia is when someone sees only red and green values of an RGB color scheme.

    Args:
        red_one (int): A color range between 0 and 255 representing the red component of the first color.
        green_one (int): A color range between 0 and 255 representing the green component of the first color.
        blue_one (int): A color range between 0 and 255 representing the blue component of the first color.
        red_two (int): A color range between 0 and 255 representing the red component of the second color.
        green_two (int): A color range between 0 and 255 representing the green component of the second color.
        blue_two (int): A color range between 0 and 255 representing the blue component of the second color.

    Returns:
        bool: True if the colors are too similar when someone has tritanopia, otherwise False.
    """
    # When viewed by someone with tritanopia, they see only red and green values
    red_value_one = red_one
    red_value_two = red_two
    green_value_one = green_one
    green_value_two = green_two

    # Compare the red and green values using the `different_colors` function
    return different_colors(red_value_one, green_value_one, 0, red_value_two, green_value_two, 0)


def print_html_values(red: int, green: int, blue: int):
    """Prints out the HTML values of each color as the standard
    color scheme and the three color-blind filters applied.

    Args:
        red (int): Red color value (0-255).
        green (int): Green color value (0-255).
        blue (int): Blue color value (0-255).
    """
    # Calculate standard HTML color value
    standard_html = rgb_to_hex(red, green, blue)
    
    # Apply color blindness filters and calculate their HTML values
    protanopia_html = rgb_to_hex(red, 0, blue)
    deuteranopia_html = rgb_to_hex(red, green, blue)
    tritanopia_html = rgb_to_hex(red, green, 0)
    
    # Print the HTML values with labels
    print(f"\tStandard:\t{standard_html}")
    print(f"\tProtanopia:\t{protanopia_html}")
    print(f"\tDeuteranopia:\t{deuteranopia_html}")
    print(f"\tTritanopia:\t{tritanopia_html}")


def run_checks(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """Checks if there is a difference between two colors for standard vision,
    Protanopia, Deuteranopia, and Tritanopia. Prints the results for each
    vision type and returns True if every color is different under all vision types,
    but False if only one vision type the colors are too similar.

    Args:
        red_one (int): Red color value for the first color (0-255).
        green_one (int): Green color value for the first color (0-255).
        blue_one (int): Blue color value for the first color (0-255).
        red_two (int): Red color value for the second color (0-255).
        green_two (int): Green color value for the second color (0-255).
        blue_two (int): Blue color value for the second color (0-255).

    Returns:
        bool: True if every color is different under all vision types, False if
        only one vision type the colors are too similar.
    """
    # Calculate differences for each vision type
    normal_diff = different_colors(red_one, green_one, blue_one, red_two, green_two, blue_two)
    protanopia_diff = check_protanopia(red_one, 0, blue_one, red_two, 0, blue_two)
    deuteranopia_diff = check_deuteranopia(red_one, green_one, blue_one, red_two, green_two, blue_two)
    tritanopia_diff = check_tritanopia(red_one, green_one, 0, red_two, green_two, 0)

    # Print the results for each vision type
    print(f"Normal vision:  {'Different' if normal_diff else 'Too similar'}")
    print(f"Protanopia:  {'Different' if protanopia_diff else 'Too similar'}")
    print(f"Deuteranopia:  {'Different' if deuteranopia_diff else 'Too similar'}")
    print(f"Tritanopia:  {'Different' if tritanopia_diff else 'Too similar'}")

    # Return True if every color is different under all vision types, False otherwise
    return normal_diff and protanopia_diff and deuteranopia_diff and tritanopia_diff


def get_number_from_client(msg: str) -> int:
    """Gets a number from a client using input.
    Ensures the number is between 0 and 255, prompting the user to reenter
    if the input is invalid. Does not check for invalid numbers, just range!

    Args:
        msg (str): A string for the message to print as part of the input prompt.

    Returns:
        int: A number between 0 and 255.
    """
    num = int(input(msg))
    if 0 <= num <= 255:
        return num
    else:
        print("--Invalid number. Must be between 0 and 255--")
        return get_number_from_client(msg)


# Example usage:
#number = get_number_from_client("Red: ")
#print("You entered:", number)





def main():
    """
    Main driver of the program.

    1. Welcomes the client
    2. Prompts them to enter two colors, by asking for the
       RBG values for the first color, and then second. 
    3. Displays the HTML values for the each color including the variations
       they would look like with various types of color blindness.
    4. Runs checks on each of the colors to determine similarity
    5. If the colors are two similar prints "The colors are too similar", 
       or states they are different if they are different enough.
    6. ends program
    """
     #UNCOMMENT lines after you finish the related functions!! 
     #You will probably finish other functions and **test** them
     #well before you uncomment parts of the main!

    print("Welcome to color checker.")
    print("Enter the RGB values for two colors.")
    print("Enter your first color:")
    red_one = get_number_from_client("Red: ")
    green_one = get_number_from_client("Green: ")
    blue_one = get_number_from_client("Blue: ")
    print("Enter your second color:")
    red_two = get_number_from_client("Red: ")
    green_two = get_number_from_client("Green: ")
    blue_two = get_number_from_client("Blue: ")

    print("The HTML values for the Color 1 are: ")
    print_html_values(red_one, green_one, blue_one)
    print("The HTML values for the Color 2 are: ")
    print_html_values(red_two, green_two, blue_two)

    valid = run_checks(red_one, green_one, blue_one, red_two, green_two, blue_two)

    if valid:
        print("The colors are different.")
    else:
        print("The colors are too similar.")

  


if __name__ == "__main__":
    main()
