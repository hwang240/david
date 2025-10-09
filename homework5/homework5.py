#file name: homework 5
#3.1 vocab review
# 1) Git vs. GitHub — Git is the local version-control tool; GitHub is a website that hosts remote Git repos for collaboration and backup.
# 2) Terminal vs. Command Line — The Terminal is the window; the command line is where we type commands inside it.
# 3) Local vs. Remote Repository — Local repo lives on your computer; remote repo lives on a server.
# 4) Version Control — A system that tracks changes to files over time, let us revert, branch, and collaborate.
# 5) Staging Area — The “index” where we prepare specific changes to include in the next commit.
# 6) git add — Put file changes into the staging area.
# 7) git commit — Save a snapshot of staged changes to history with a message.
# 8) git push — Send our local commits to a remote repository/branch.
# 9) git status — Show what’s changed, what’s staged, and which branch I am on.
# 10) git pull — Get changes from the remote and merge into my current branch.
# 11) pwd — Print working directory, shows where I am at for my files.
# 12) ls — List files and folders in the current directory.
# 13) cd — Change directory.
# 14) nano — Simple terminal text editor.
# 15) touch — Create an empty file or update a file’s timestamp.
# 16) mv — Move or rename files/directories.
# 17) rm — Remove files.
# 18) cat — Concatenate/print file contents to the terminal.

#3.2 
# 1. pwd
# 2. ls
# 3. cd ../brianna_repo
# git pull origin main
# 4. mv homework.py ~/python_decal/judy_decal/homework/
# 5. cd ~/python_decal/judy_decal/homework/
# 6. cat homework.py
# 7. git add .
# git commit -m "Finish homework"
# git push origin main
# 8. git pull origin main
# git push origin main
# 9. cd ~/Recent/

# 4

#4.1
def checkDataType(var):
  return type(var)

print(checkDataType(100.0))
#4.2
def evenOrOdd(num):
  if num % 2 == 0:
    return("Even")
  else:
    return("Odd")
print(evenOrOdd(4))

#5
numbers = [0, 1, 2, 3, 4, 5]
def sumWithLoop(numbers):
  count = 0
  for num in numbers:
    count += num
  return(count)

print(sumWithLoop(numbers))

#6.1
def dupList(dataset):
  empty = []
  for i in dataset:
    empty.append(i)
    empty.append(i)
  return(empty)
print(dupList(['a', 'b','c']))
#6.2
def square(num):
  return num * num # (missing semicolon :)

print(square(5))
#7.2
numbers = [2, 1, 4, 8, 10, 5]
def sumWithLoop(numbers):
  count = 0
  for num in numbers:
    count += num
  return(count)

print(sumWithLoop(numbers))
