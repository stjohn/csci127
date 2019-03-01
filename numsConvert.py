#CSci 127 Teaching Staff
#February 2019
#A program that uses functions to print out months.
#Modified by:  ADD YOUR NAME HERE

def num2string(num):
     """
     Takes as input a number, num, and
     returns the corresponding name as a string.
     Examples: num2string(0) returns "zero", num2string(1)returns "one"
     Assumes that input is an integer ranging from 0 to 9
     """
     
     numString = ""

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################

     return(numString)



def main():
     nums = input('Enter a multi-digit number: ')
     print('In words, your number is: ', end="")
     for n in nums:
         word = num2string(int(n))
         print(word, end=" ")
     print('.')


#Allow script to be run directly:
if __name__ == "__main__":
     main()
