# Write Python code to iterate through the first 10 numbers and,
# in each iteration, print the sum of the current and previous number.
j=0
for i in range(0,10):
    print('current number',i,'previous number',j,'sum =',i+j)
    j=i
