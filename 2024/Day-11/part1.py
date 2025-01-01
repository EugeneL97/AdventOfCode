# Overview
    # We have these stones with numbers on them, on each line of input, the digits separated by spaces are these stones
    # Their digits are their values
    # Everytime we iterate, these stones will split and change their values based off three conditions
        # Condition 1: If the value is 0, change it to 1
        # Condition 2: If the value has an even amount of digits (99, 1001, 2000)
            # Split them into two ((9,9), (10, 1), (20, 0))
                # Notice how the leading zeroes are lost
        # Condition 3: Condition 1 or 2 don't apply. Multiply the value by 2024
    
    # After iteration, in our case, 25 times
        # Return the amount of stones we have

# Implementation
    # Read the file input and store this into an array(?)
        # Because of stone splitting, it'll make sense to use an array, find the index of the current stone
        # and append that new stone to the left of it
        # This way we still track the length of the array
        
    # NUMBER_OF_BLINKS = 25
    # for i in range(NUMBER_OF_BLINKS):
        # for j in range(len(array)):