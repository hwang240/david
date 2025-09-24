# File: homework3.py

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
    return True
  else:
    return False

def fuel_efficiency(miles, gallons): # this function takes in the total distance in miles and fuels used in gallons
  return (miles / gallons)

def secret_code(num):
  last_digit = num % 10  # this gives the last digit of the number
  rest = num // 10 # this gives the remaining numbers without the last digit
  return int(str(last_digit) + str(rest))  # turns the num into string and puts out the num

def square(x, y):
  result = 1
  for num in range(y): # for all the numbers in the range of y, the result would be x * x
    result *= x
  return result

def minimum(list):
  m = list[0]
  for num in list[1:]: # this makes the for loop iterate over all the element in the list
    if num < m:
      m = num
  return(m)

def maximum(list):
  m = list[0]
  for num in list[1:]:
    if num > m:  # if the number is bigger then the previous element, then m become the bigger number
      m = num
  return(m)

def minimum_while(list):
  m = list[0]
  i = 1
  while i < len(list):
    if list[i] < m:  # if the number in the list is less than the first element in the list, it replaces the minimum one
      m = list[i]
    i += 1
  return m

def maximum_while(list):
  m = list[0]
  i = 1
  while i < len(list):
    if list[i] > m: # if the number in the list is greater than the first element in the list, it replaces the maximum one
      m = list[i]
    i += 1
  return(m)

def sum_digits(number):
    sum = 0
    while number > 0:  # all positive numbers work
        sum += number % 10  # this let the sum add the last digit of the number
        number //= 10  # this deletes the last digit and comtinues the loop
    return sum

number = 12345
final_result = sum_digits(number) # finding the summation of all the digits in 12345

print(f" the result of Calculating the Sum (6.3) with number = {number} is {final_result}").