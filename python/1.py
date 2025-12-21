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
