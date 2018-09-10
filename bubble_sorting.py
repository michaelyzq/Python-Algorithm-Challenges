#
'''
https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/tutorial/
You have been given an array A of size N . you need to sort this array non-decreasing oder using bubble sort. However, you do not need to print the sorted array . You just need to print the number of swaps required to sort this array using bubble sort

Input Format

The first line consists of a single integer N denoting size of the array. The next line contains N space separated integers denoting the elements of the array.

Output Format Print the required answer in a single line



'''

size = int(raw_input("First input"))
input  =  raw_input("second input").split(' ')

a = 0
b = 0
count =0
while b < size-1:
    a = 0
    while a < size-1-b:
        print "compare"
        if int(input[a]) > int(input[a+1]):
            inputa = input[a]
            inputa_p1 = input[a+1]
            input[a] = inputa_p1 
            input[a+1] = inputa
            count = count +1
        a = a +1
    b = b+1
print count