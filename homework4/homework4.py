# File : Homework4.py
# 3.1 List Operations

favFood = ['Ramen', 'Rice', 'Pizza', 'Cookies', 'IceCream']

print(favFood[1])
print(favFood[-1])
favFood.append('Chocolate')
favFood.insert(0, 'Apple')
favFood.remove('Pizza')
print(len(favFood))
for food in favFood:
  print(food.upper())

newFavFood = favFood[0::5]
for food in favFood:
  if food == 'Potato':
    print("A Potato")
  else:
    print("No Potato")  #This checks each food in the list, and if there is a potato it says A potato, and else No potato.

# 3.2 Slicing and Striding
numbers = list(range(21))

def get_first_15(numbers):
  return(numbers[:15])

def get_every_5th(lst):
  return(lst[::5])

def reverse_and_stride(lst):
  return(lst[::-1][::3])

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step1)
print(step2)
print(step3)

# 3.3 nested lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers[2]) # gives the third row
print(numbers[1][1]) # gives the second item in the second row
numbers.append([10, 11, 12]) # adds [10, 11, 12] in to the matrix
def sum_nested(matrix):
  total = 0
  for row in matrix:
    row_sum = 0
    for x in row:
      row_sum += x
    total += row_sum
  return(total)

# 3.4 Create a 5x5 list

def make_5x5():
  grid = [] # I created an empty matrix list
  n = 1
  for r in range(5): #this print each row
    row = []
    for c in range(5):  # this checks for each col and by adding n+1 we will have 1-25 for each range(5)
      row.append(n)
      n += 1
    grid.append(row)
  return grid

def replace_multiples_of_3(mat):
  updated = []
  for row in mat:
    new_row = []
    for x in row:
      new_row.append("?" if (x % 3 == 0) else x)  # this adds a ? for each multiple of 3 in the list
    updated.append(new_row)
  return updated

def sum_of_all(mat):
  total = 0
  for row in mat:
    for x in row:
      if x != "?":
        total += x   # this adds all non-? and it is stored in total as a sum
  return total

# 4.1 Dictionary Operations
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for key, value in ages.items( ):
  print(f"{key} = {value}")


# 5 Running my Code
grid = make_5x5()
masked = replace_multiples_of_3(grid)
total = sum_of_all(masked)

print(grid)
print(masked)
print(total)