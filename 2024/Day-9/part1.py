# Overview: Read the file input and translate that into a string since this is single line. 
    # Once we structure this string, we have two pointers, one at the start of the free space (first dot we encounter), and one at the end of the last digits. 
    # Swap the dots in the beginning with the digit at the end. 
    # Repeat until we get a continuous line of dots at the end. 
    # Multiply the index with the ID and sum those for our output

# Read the file input
    # File input is structured [i] as length of file and [i + 1] as the length of free space
    # The digits that occupy the length of file are the IDs
    # They increment throughout the file (0, 1, .., n - 1, n)
# Once we are done looping through the input to get our new string, we’ll setup our two pointers
    # While l <= r
    # Left = first instance of dots
    # Right = first instance of digit (probably len(string) - 1)
# swap(left, right)
    # While(string[left:left+len(digit)] != ‘.’) #  if it’s a digit
    # Left += len(digit)
    # While(string[right] == ‘.’) 
    # Right -= 1

# DISREGARD BELOW
# Note: we need to handle digits of len > 1
    # Should we track the length of the last digit?
        # Yes we should
        # That determines how many dots occupy the first set of dots
        # Consider if len(digits) > dots
            # In this case, we’ll while loop the len(digits) and skip digits to occupy the dots.
