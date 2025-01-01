# Substring in a string problem
# Count all valid strings (where substrings make up the strings)
    # Invalid strings is when any substring cannot make up part of the string
# Sliding window technique
    # Window size = 1, i = 0
        # If this is in our substring set
            # i += 1, window size stays the same
        # If it's not
            # window Size += 1, i = 0
        # While window size + i < len(string):
            # the window size + i, is the end of the window
        # When we find a string, i = window_size + i, window_size = 1
            # Move to the next char, repeat until end of string

# Read file input
    # First half are our substrings, put these in a set
    # End when we hit the new line
    # Second half are our strings, put these in a list

# Loop through our strings
    # Do the sliding window technique and check if the window string is a substring
    # We COULD theoretically end this early, probably with a regex check
        # Could end based off the longest length of the substring too
            # This would be simpler than regex

    # For simplicity, going until end of string length, since it's not so long to begin with
        # If it was longer, would likely end it earlier
