#Casandra Villagran
#3/5/2020

#A function that takes a year as a parameter
#and returns True if the year is a leap year, False if it is otherwise.

def checkYear(year): 
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                return True
            else: 
                return False
        else: 
             return True
    else: 
        return False
  
year = 2000
if(checkYear(year)): 
    print("Leap Year") 
else: 
    print("Not a Leap Year") 
