# ------------------------------------------------- # 
# Title: Assignment 07 Part 2 
# Description: An example of error handling  
# ChangeLog: (Who, When, What) 
# Kelsey Kawaguchi,11.24.2019,Created Script 
# ------------------------------------------------- # 

# Error Handling  
try: 
    days = int(input("Enter the amount of calendar days left until Christmas: "))
    weeks = days/7
except ValueError: 
    print("\n There was an error! The program will only work if you input an integer. \n")
else: 
    print("\n There are %.2f weeks left until christmas! \n" % weeks)
    
   





    

