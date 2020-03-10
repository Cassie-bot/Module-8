#Casandra Villagran
#3/5/2020

#A function that takes two inputs from a user and prints
#whether the sum is greater than 10, less than 10, or equal to 10


#Use a range from 1-10
def Numbers():
    number=int(input("Please enter a number between a number: "))

    numberr= int(input("Please enter another number to see if both of your inputs added are less than/greater than/equal to 10: "))


    x=number

    y=numberr

    x+y>10 or x+y<10 or x+y==10

    if int (x+y>10):
        print("And the sum is greater than 10")
    if int (x+y<10):
        print("And the sum is less than 10")
    if int (x+y==10):
        print("And the sum is equal to 10")
Numbers()
