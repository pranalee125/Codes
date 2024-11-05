#Name - Pranalee Raut
#Class - SE-2
#PRN - F23112036
#Batch - Q
#Seat N0 - F190320536
'''
 Group B-15
 Title - Write a python program to store second year percentage of students in array. Write function for sorting array of floating
 point numbers in ascending order using 
 a) Insertion Sort
 b) Shell Sort and Display top five scores  
'''

def InsertionSort(list):

    for i in range(1,len(list)):

        key = list[i]
        j = i-1

        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key

    return list

def ShellSort(list):

    n = len(list)
    interval = n//2
    while interval>0:

        for i in range(interval,n):
            temp = list[i]
            j=i

            while j>=interval and list[j-interval]>list[j]:
                list[j] = list[j-interval]
                j-=interval
            list[j] = temp

        interval//=2

    return list

scores = []
print("Enter float scores separated by a space: ",end="")
my_list = list(map(float, input().split()))
sort_by_insertion = my_list
print("Insertion-Sorted Scores: ",InsertionSort(sort_by_insertion))

print("\nShell Sort Scores: ",ShellSort(my_list))

print("Top 5 Scores: ")
j=1
for i in range(-1,-5,-1):
    print(j,": ",my_list[i])
    j+=1

'''
Output -
Enter float scores separated by a space: 12 23 34 45 56 67 78 89 90
Insertion-Sorted Scores:  [12.0, 23.0, 34.0, 45.0, 56.0, 67.0, 78.0, 89.0, 90.0]

Shell Sort Scores:  [12.0, 23.0, 34.0, 45.0, 56.0, 67.0, 78.0, 89.0, 90.0]
Top 5 Scores:
1 :  90.0
2 :  89.0
3 :  78.0
4 :  67.0
'''