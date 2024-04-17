#CSci 127 Teaching Staff
#October 2017
#A program that converts hex numbers to decimal, but filled with errors...  
Modified by:  Olufisayomi Lekan Michael

def convert(s):
    """Takes a hex string as input.
    Returns decimal equivalent."""
    total = 0
     
    for c in s:
        total = total * 16
        ascii_val = ord(c)
        if ord('0') <= ascii_val <= ord('9'):
            # It's a decimal number, and return it as decimal:
            total = total + ascii_val - ord('0')
        elif ord('A') <= ascii_val <= ord('F'):
            # It's a hex number between 10 and 15, convert and return:
            total = total + ascii_val - ord('A') + 10
        elif ord('a') <= ascii_val <= ord('f'):
            # Check if they used lower case:
            # It's a hex number between 10 and 15, convert and return:
            total = total + ascii_val - ord('a') + 10
        else:
            # Not a valid number!
            return -1
    return total

def main():
    hexString = input("Enter a number in hex: ")
    print("The number in decimal is", convert(hexString))

# Allow script to be run directly:
if __name__ == "__main__":
    main()
 
