#A program to print if the year is leap year or not, in a given range

year = int(input("what year do you want to start with?"))
year_check = int(input("how many year do you want to check?"))

for x in range(year,year + year_check + 1):
   if x % 4 == 0 :
     print("{} is leap year".format(x))
   else:
    print( "{} is not leap year".format(x))
   