#Casandra Villagran
#3/5/2020

#Getting two inputs from a user and checking whether they are equal or not.


#Use a range from 1-100
def numbers():
    number=int(input("Please enter a number between 1 and 100: "))
    if number>0 and number<= 100:
        print("You entered a valid number")
    else:
        print("You must enter a number between 1 and 100")

    numberr= int(input("Please enter another number between 1 and 100 to see if it's equal to the number above: "))
    if numberr>0 and numberr<= 100:
        print("You entered a valid number")
    else:
        print("You must enter a number between 1 and 100")

           
    x=number

    y=numberr

    x==y

    if int (x==y):
        print("And YES they're enqual!")
    else:
        print("But oh no, they're not equal.")
numbers()
