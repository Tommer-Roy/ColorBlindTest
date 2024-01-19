"""
    Student: Tommer Ben-Joseph
    Semester: Fall 2023

    Helps with testing color_tester.py
"""

import color_tester

def test_delta() -> int:
    """Tests the delta function. 
    
    Returns the number of tests that failed.
    """
    # 255, 255, 255, 0, 0, 0 - should give a difference of 1
    failed = 0
    if color_tester.delta(255, 255, 255, 0, 0, 0) != 1:
        print("Failed delta test with (255, 255, 255) and (0, 0, 0)") 
        failed += 1
    # 255, 255, 255, 255, 255, 255 - should give a difference of 0
    if color_tester.delta(255, 255, 255, 255, 255, 255) != 0:
        print("Failed delta test with (255, 255, 255) and (255, 255, 255)") 
        failed += 1
    # 255, 255, 255, 127, 127, 127 - should give a difference of 0.5
    delta = round(color_tester.delta(255, 255, 255, 127, 127, 127), 2) #rounding because of floating point errors
    if  delta != 0.5:
        print(f"Failed delta test with (255, 255, 255) and (127, 127, 127), delta = {delta}") #this way we can see what it was 
        failed += 1
    return failed    


def test_different_colors() -> int:
    """Tests the different_colors function. 
    
    Returns the number of tests that failed.
    """
    # 255, 255, 255, 0, 0, 0 - should give a difference of 1
    failed = 0
    if color_tester.different_colors(255, 255, 255, 0, 0, 0) != True:
        print("Failed different_colors test with (255, 255, 255) and (0, 0, 0)") 
        failed += 1
    # 255, 255, 255, 255, 255, 255 - should give a difference of 0
    if color_tester.different_colors(255, 255, 255, 255, 255, 255) != False:
        print("Failed different_colors test with (255, 255, 255) and (255, 255, 255)") 
        failed += 1
    # 255, 255, 255, 127, 127, 127 - should give a difference of 0.5
    different_colors = round(color_tester.different_colors(255, 255, 255, 127, 127, 127), 2) #rounding because of floating point errors
    return failed    

    
def test_check_protanopia() -> int:
    """Tests the check_protanopia function. 
    
    Returns the number of tests that failed.
    """
    # 255, 255, 255, 0, 0, 0 - should give a difference of 1
    failed = 0
    if color_tester.check_protanopia(230, 13, 255, 123, 200, 255) != False:
        print("Failed check_protanopia test with (255, 255, 255) and (0, 0, 0)") 
        failed += 1
    return failed


def test_check_deuteranopia() -> int:
    """Tests the check_deuteranopia function. 
    
    Returns the number of tests that failed.
    """
    # 255, 255, 255, 0, 0, 0 - should give a difference of 1
    failed = 0
    if color_tester.check_deuteranopia(255, 255, 255, 0, 0, 25) != True:
        print("Failed check_deuteranopia test with (255, 255, 255) and (0, 0, 0)") 
        failed += 1
    return failed


def test_check_tritanopia() -> int:
    """Tests the check_tritanopia function. 
    
    Returns the number of tests that failed.
    """
    # 255, 255, 255, 0, 0, 0 - should give a difference of 1
    failed = 0
    if color_tester.check_tritanopia(230, 13, 255, 200, 0, 255) != False:
        print("Failed check_tritanopia test with (255, 255, 255) and (0, 0, 0)") 
        failed += 1
    return failed


def test_print_html_values() -> int:
    """Tests the print_html_values function. 
    
    Returns the number of tests that failed.
    """
    # 255, 255, 255, 0, 0, 0 - should give a difference of 1
    expected_html = print("\tStandard:\t#e60dff")
    print("\tProtanopia:\t#0000ff")
    print("\tDeuteranopia:\t#e600ff")
    print("\tTritanopia:\t#e60d00")
    failed = 0
    if color_tester.print_html_values(230, 13, 255) != expected_html:
        print("Failed print_html_values test with (230, 13, 255)") 
        failed += 1
    return failed


def test_run_checks() -> int:
    """Tests the run_checks function. 
    
    Returns the number of tests that failed.
    """
    # 255, 255, 255, 0, 0, 0 - should give a difference of 1
    expected_output = print("Normal vision:  Different")
    print("Protanopia:  Too similar")
    print("Deuteranopia:  Different")
    print("Tritanopia:  Different")
    failed = 0
    if color_tester.run_checks(230, 13,255, 123,200,255) != expected_output \
       and color_tester.run_checks(230, 13,255, 123,200,255) != False:
        print("Failed run_checks test with (230, 13,255, 123,200,255)") 
        failed += 1
    return failed



def test_get_number_from_client() -> int:
    """Tests the get_number_from_client function. 
    
    Returns the number of tests that failed.
    """
    failed = 0        
    # Test with a valid input message and expected result
    if int(color_tester.get_number_from_client(25)) != 25:
        print("Failed get_number_from_client test")
        failed += 1
    return failed


def test_main():
    expected_output = """
Welcome to color checker.
Enter the RGB values for two colors.
Enter your first color:
Red: 230
Green: 13
Blue: 255
Enter your second color:
Red: 123
Green: 200
Blue: 255
The HTML values for the Color 1 are: 
	Standard:   #e60dff
	Protanopia: #0000ff
	Deuteranopia:   #e600ff
	Tritanopia: #e60d00
The HTML values for the Color 2 are: 
	Standard:	 #7bc8ff
	Protanopia:	 #0000ff
	Deuteranopia:	 #7b00ff
	Tritanopia:	 #7bc800
Normal vision:  Different
Protanopia:  Too similar
Deuteranopia:  Different
Tritanopia:  Different
The colors are too similar.
"""
    failed = 0
    if color_tester.main() != expected_output:
        print("Failed main test")
        failed += 1
    return failed







def run_all() -> None:
    """Runs all tests, continue to update this with functions as you add them"""
    fail_count = 0
    fail_count += test_delta()
    fail_count += test_different_colors()
    fail_count += test_check_protanopia()
    fail_count += test_check_deuteranopia()
    fail_count += test_check_tritanopia()
    fail_count += test_print_html_values()
    fail_count += test_run_checks()
    fail_count += test_get_number_from_client()
    fail_count += test_main()
    
    ## add more here as you add more functions, notice the += above adding teh return value to the fail_count


    ## and then giving feedback
    print(f"Failed {fail_count} tests")



if __name__ == '__main__':
    run_all() 
