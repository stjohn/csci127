#CSci 127 Teaching Staff
#October 2017
#A program that uses functions to print out months.
#Modified by:  CHANGLONG WANG / GitHub: Peterwang0211

def monthString(monthNum):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     
     monthString = ""

     if monthNum=1:
          print("January")
     elif monthNum=2:
          print("February")
     elif monthNum=3:
          print("March")
     elif monthNum=4:
          print("April")
     elif monthNum=5:
          print("May")
     elif monthNum=6:
          print("June")
     elif monthNum=7:
          print("July")
     elif monthNum=8:
          print("August")
     elif monthNum=9:
          print("September")
     elif monthNum=10:
          print("October")
     elif monthNum=11:
          print("December")
     else:
          print("December")

     return(monthString)



def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
