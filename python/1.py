# Write Python code to iterate through the first 10 numbers and,
# in each iteration, print the sum of the current and previous number.
j=0
for i in range(0,10):
    print('current number',i,'previous number',j,'sum =',i+j)
    j=i
========================= 
# Write a Python code to display numbers from a list divisible by 5
list=[10,20,33,46,55]
print('given list is:',list)
for number in list:
 if number % 5 == 0:
     print(number)
=========================
# Write a code to generates a complete multiplication table for numbers 1 through 10.
for i in range(1,11):
    for j in range(1,11):
        c=i*j
        print(c,end=' ')
    print()
========================
# Write a program to take three names as input from the user in a single call to the input() function.
names =input('enter three string:').split()
if len(names) !=3:
    print('please enter three string')
else:
    for i in range(3):
        print(f'Name{i+1}: {names[i]}')
=========================
# You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78].
# Print these lists as a simple table with columns “Name” and “Score”.

names = ["Alice","Bob","Charlie"]
scores = [85,72,90]

print("Name    Score")
print("----------------")

for i,name in enumerate(names):
        print(f'{name:<9}{scores[i]}')
============================= 
# Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.

word=input('Enter a word: ')
num=int(input('Enter a number: '))

print(f'{word:>20}{num}')
=============================

=============================
============================
=================



