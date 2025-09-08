# File: homework1.py

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a real number that can have decimal points or fractional components

c = 3j
print(c)
print(type(c)) # c is a complex, specifying a real number and an imaginary number

d = "hello"
print(d)
print(type(d)) # d is a string, represents sequences of characters

e = [1,2,3]
print(e)
print(type(e)) # e is a list, lists are used to store multiple items in a single variable

f = {"name" : "Ellen", "favorite fruit" : "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a collection that stores data in key-value pairs

g = (1,2)
print(g)
print(type(g)) # g is a tuple, used to store multiple items in a single variable

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, used to store multiple items in a single variable

i = True
print(i)
print(type(i)) # i is a boolean, represents truth values, true or false

j = None 
print(j)
print(type(j)) # j is a NoneType, represents the absence of a value or a null object reference

k = [True, "Blue", 12]
print(k)
print(type(k)) # k is a list, used to store muliple items

l = str(14)
print(l)
print(type(l)) # l is a string, represents sequence of characters

m = 1e4
print(m)
print(type(m)) # m is a float, a real number that can have decimal points or fractional components

# 1. I find total of 9 different variables
# 2. The datatypes are float, str, list, NoneType, bool, int, tuple, dict, complex.
# 3. variables m and b have the same datatype, and l and d have same datatype, k and h and e have the same datatype.
# 4. the datatype of l is a string, it is not an integer because the integer 14 is inside str(), 
# str() takes the input and outputs as a string.
# 5.  A different datatype would be set, an unordered collection of unique elements.


# --- Booleans ---
print(bool(10 > 9)) #True, 10 is greater than 9
print(bool(10 == 9)) #False, 10 does not equal to 9
print(bool(10 <= 9)) #False, 10 is not less than or equal to 9 
print(bool("abc"))  # True, non-empty string is true
print(bool(123))  # True non-zero number is true
print(bool(["apple", "cherry", "banana"]))  # True non-empty list is true
print(bool(True))  # True
print(bool(False))  # False
print(bool(0))  # False, zero is false
print(bool(""))  # False, empty string is false
print(bool(" "))  # True, space makes the string non-empty
print(bool(()))  # False, empty tuple
print(bool([]))  # False, empty list
print(bool({}))  # False, empty dict
print(bool(True and False))  # False, having one true and one false makes it false
print(bool(True and True))  # True, both sides are true
print(bool(False and False))  # False, both sides are false
print(bool(True or False))  # True, having one true in "or" statements makes it true
print(bool(True or True))  # True, both are true
print(bool(False or False))  # False, both are false
print(bool(not(False)))  # True, the opposite of false is true
print(bool(not(True)))  # False, the opposite of true is false

# 1. Some patterns I noticed returning True or False is that all the empty sets, lists, strings etc will result False, 
# and non-empty ones are True.
# 2. bool(" "), this expressions surprises me, because having a "space" inside the string made it True.
# 3. bool({0}) this expression will result true, because having a single value in the set makes it non-empty.
# 4. bool(set()) this expression will result false, because empty set its also false.


# --- Operators ---
# --- 3.3.1 Arithmetic Operators ---
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs division
print(5 % 2) # 1, % is modulo, it gives the remainder after division
print(3 ** 2) # 9, ** is exponential, 3 to the power of 2
print(15 // 2) # 7. // is floor division, it rounds down

# --- 3.3.2 Comparison Operators ---
print(5 == 2) # False, 5 does not equal 2
print(10 != 10) # False, 10 does equal to 10, != means does not equal
print(2 < 5) # True, 2 is less than 5
print(12 > 5) # True, 12 is greater than 5
print(5 <= 6) # True, 5 is less than or equal to 6
print(1 >= 10) # False, 1 is not greater than or equal to 10

# --- 3.3.3 Assignments Operators ---
x = 5
x += 5 # x results in 10, same as x = x + 5
x -= 4 # x results in 1, same as x = x - 4
x *= 3 # x results in 15, same as x = x * 3

# --- 3.3.4 Logical Operators ---
# 1. AND: True only if both sides are True.
# print((5 > 3) and (2 < 4))     # True, both comparisons are True
# print((5 > 3) and (2 > 4))     # False, right side is False

# 2. OR: True if at least one side is True. 
# print((5 < 3) or (2 < 4))      # True, right side is True
# print((1 > 2) or (3 < 1))      # False, both sides are False

# 3. NOT: logical negation.
# print(not (3 < 2))             # True, because (3 < 2) is False
# print(not (5 > 2))             # False, because (5 > 2) is True

# --- More Questions ---
# 1. / is true division, which returns a float; // is floor division -> quotient rounded DOWN toward -∞.
# 2. // gives the floor-quotient; % gives the remainder.
# 3. Use %, example: print(23 % 6)  # 5
# 4. Assignment operators basically update a variable using an operation with its current value. Like x = x + 1, x += 1.


# --- Strings ---
my_string = "hello"
print(my_string[0])     # h, because its the first character of the string
print(my_string[1])     # e, second character
print(my_string[2])     # l, third character
print(my_string[3])     # l, fourth character
print(my_string[4])     # o, fifth character
print(my_string[-1])    # o, negative index means the last character
print(my_string[1:3])   # el, it starts from the 1st index to the 3rd one but not including the third
print(my_string[0:5:2]) # hlo, takes every second character from 0 to 4
print(len(my_string))   # 5, length
print(my_string + "goodbye") # hellogoodbye, creates a new string
print(7 * my_string)         # hellohellohellohellohellohellohello, it repeats 7 times

# --- 3.4.1 Questions ---
# 1. Slicing means taking a substring by indices using start:stop:step. 
# In the earlier questions, slicing was used in: my_string[1:3] and my_string[0:5:2].
# 2.  
name = "Oski"
print("Hello, my name is", name)       # Hello, my name is Oski
# print with two arguments, print() inserts a space between them by default.
# 3.
name = "Oski"
print(f"Hello, my name is {name}")     # Hello, my name is Oski
# f-string, it evaluates {name} and inserts its value into one string.

# 4.
# - First line passes two arguments to print; print joins them a space.
# - Second line builds one formatted string via an f-string.


# --- Terminal Commands ---
# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# Lists files and folders in the current directory.
# Example: ls

# ls -a
# Lists all files, including hidden “dotfiles”.
# Example: ls -la

# mkdir
# Creates a new directory (folder).
# Example: mkdir hw1_folder

# cat
# Prints a file’s contents to the terminal.
# Example: cat homework1.py

# pwd
# Prints the full path of the current working directory.
# Example: pwd

# cd ..
# Moves to the parent directory (one level up).
# Example: cd ..

# cd .
# Refers to the current directory.
# Example: cd .

# cd ~
# Jumps to your home directory.
# Example: cd ~

# cp
# Copies files (use -r to copy directories).
# Example: cp notes.txt backup.txt

# mv
# Moves or renames files or directories.
# Example: mv draft.txt final.txt

# rm
# Deletes files; permanent (use -i to confirm, -r for directories). Be careful!
# Example: rm -i old.txt

# clear
# Clears the terminal screen.
# Example: clear

# grep
# Searches for lines matching a text pattern in files.
# Example: grep -n "def " *.py

#Questions
# 1. 
# touch
# Creates an empty file or updates a file's timestamp.
# Example: touch notes.txt

# less
# Opens a file in a paged viewer (scroll with ↑/↓, q to quit).
# Example: less homework1.py

# wc
# Counts lines/words/bytes in files (use -l, -w, -c).
# Example: wc -l homework1.py

# 2. Differences between ls and ls -a is that ls lists visible files and folders in the current directory, while
# ls - a lists all files, and hidden ones too.

# 3. Any file or folder whose name starts with a dot (.) is considered hidden by convention.
# It won’t appear with ls command.

# 4. 
# 1) ls -l
# "long" listing: shows permissions, owner, size, date.

# 2) ls -h
# "human-readable" sizes (KB/MB/GB). Usually combined with -l.

# 3) grep -n
# Show line numbers for matches. 