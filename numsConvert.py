#CSci 127 Teaching Staff
#February 2019
#A program that uses functions to print out months.
#Modified by: Samuel Michnik

def num2string(num):
     
     ##Takes as input a number, num, and
     ##returns the corresponding name as a string.
     ##Examples: num2string(0) returns "zero", num2string(1)returns "one"
     ##Assumes that input is an integer ranging from 0 to 9
     
     
     numString = ""
     if num == 0:
          numString = 'zero'
          elif num == 1:
               numString = 'one'
               elif num == 2:
                    numString = 'two'
                    elif num == 3:
                         numString = 'three'
                         elif num == 4:
                              numString = 'four'
                              elif num == 5:
                                   numString = 'five'
                                   elif num == 6:
                                        numString = 'six'
                                        elif num == 7:
                                             numString = 'seven'
                                             elif num == 8:
                                                  numString = 'eight'
       
     else:
          numString = 'nine'
         

     return(numString)



def main():
     nums = input('Enter a multi-digit number: ')
     newStr = ""
     for n in nums:
         word = num2string(int(n))
         newStr = newStr + " " + word
     msg = 'In words, your number is:' + newStr + "."
     print(msg)   


#Allow script to be run directly:
if __name__ == "__main__":
     main()
