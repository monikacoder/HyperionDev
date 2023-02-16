#A program to print the numbers in the range 1 to 12

number = int(input("pls enter the number:"))
for x in range (1,13) :
  print("{} * {} = {}".format(number , x ,x*number))
