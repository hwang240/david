# File: homework2.py

def say_goodbye(name):
  print("Goodbye, " , name)

def circle_area(radius):
  print(3.14 * (radius ** 2)) # calculate area of circle by pi * r^2

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def min_max_temp(readings):  #given a list of temperature for readings
  return (min(readings), max(readings))  # determines the min and max of the temp (numbers) in the list

def is_weekend(day):
  if day == 6 or day == 7:  #if the days are saturday or sunday, then it is weekend, else false
    return true
  else:
    return false

def fuel_efficiency(miles, gallons): # this function takes in the total distance in miles and fuels used in gallons
  return (miles / gallons)

def secret_code(num):
  last_digit = num % 10  # this gives the last digit of the number
  rest = num // 10 # this gives the remaining numbers without the last digit
  return int(str(last_digit) + str(rest))  # turns the num into string and puts out the num

