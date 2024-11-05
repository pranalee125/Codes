#Name - Pranalee Raut
#Class - SE-2
#PRN - F23112036
#Batch - Q
#Seat N0 - F190320536
'''
Group A-2
Title - Problem Statement: Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency

Code from Data Structure Lab (SPPU - Second Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-se-comp-codes/DSL
'''

# BEGINNING OF CODE
# List for storing marks
marks = []
total = int(input("Total number of students are:\t"))

# Input marks
def marksInput():
    print("\n----------\nNOTE: PLEASE ENTER MARKS OUT OF 50. ENTER '-1' FOR ABSENT STUDENTS.\n----------\n")
    for i in range(total):
        enterMarks = int(input(f"Enter marks for student {i+1}:\t"))
        marks.append(enterMarks)
    print(f"\n-----\nMarks of {total} students are:\t{marks}\n-----")

# Option 1 = Average score
def average_marks():
    marks_withoutAbsent = []
    for i in marks:
        if (i >= 0):
            marks_withoutAbsent.append(i)
        else:
            continue
    average_calc = sum(marks_withoutAbsent) / total
    print(f"\n------\nAverage score of {total} students is:\t{average_calc}\n-----")

# Option 2 = High and low marks
def high_low():
    maxi = marks[0] # Initialise maxi with the first element of the marks list
    mini = marks[0] # Initialise mini with the first element of the marks list
    for i in range(len(marks)):
        if (maxi < marks[i] and marks[i] > -1):
            maxi = marks[i]
    for j in range(len(marks)):
        if (mini > marks[j] and marks[j] > -1):
            mini = marks[j]
    print(f"\n-----\nHighest score is:\t{maxi}\nLowest score is:\t{mini}\n-----")

# Option 3 = Absent count
def absent():
    absent_count = 0;
    for i in marks:
        if (i < 0):
            absent_count+=1
        else:
            continue
    print(f"\n-----\nTotal absent students are:\t{absent_count}\n-----")

# Option 4 = Highest frequency
def high_freq():
    freq_count = 0 # Initialise frequency counter
    for i in range(len(marks)): # Iterate through marks list using i
        if (marks[i] >= 0): # Only consider non-negative marks (since -1 is absent)
            temp_count = 0 # Initialise temporary counter
            for j in range(len(marks)): # Iterate through marks list using j again
                if (marks[i] == marks[j]):
                    temp_count+=1
            if (freq_count < temp_count): # If temp_count is greater than freq_count value, then
                freq_count = temp_count # Make freq_count equal to temp_count
    print(f"\n-----\nHighest frequency is:\t{freq_count}\n-----")

def main():
    marksInput()
    
    while (1):
        print("\n----- MAIN MENU -----")
        print("1 -> Average score of class")
        print("2 -> Highest and lowest score of class")
        print("3 -> Total absent students")
        print("4 -> Marks with highest frequency")
        print("5 -> Exit")
        
        optn = int(input("Choose an option (1-5):\t"))
        
        if (optn == 1):
            average_marks()
        elif (optn == 2):
            high_low()
        elif (optn == 3):
            absent()
        elif (optn == 4):
            high_freq()
        elif (optn == 5):
            print("\n\n## END OF CODE\n\n")
            quit()
        else:
            print("\n\nPlease choose a valid option (1-5)\n\n")
main()

'''
Output -
Total number of students are:   5

----------
NOTE: PLEASE ENTER MARKS OUT OF 50. ENTER '-1' FOR ABSENT STUDENTS.
----------

Enter marks for student 1:      36
Enter marks for student 2:      40
Enter marks for student 3:      44
Enter marks for student 4:      47
Enter marks for student 5:      49

-----
Marks of 5 students are:        [36, 40, 44, 47, 49]
-----

----- MAIN MENU -----
1 -> Average score of class
2 -> Highest and lowest score of class
3 -> Total absent students
4 -> Marks with highest frequency
5 -> Exit
Choose an option (1-5): 1

------
Average score of 5 students is: 43.2
-----

----- MAIN MENU -----
1 -> Average score of class
2 -> Highest and lowest score of class
3 -> Total absent students
4 -> Marks with highest frequency
5 -> Exit
Choose an option (1-5): 2

-----
Highest score is:       49
Lowest score is:        36
-----

----- MAIN MENU -----
1 -> Average score of class
2 -> Highest and lowest score of class
3 -> Total absent students
4 -> Marks with highest frequency
5 -> Exit
Choose an option (1-5): 3

-----
Total absent students are:      0
-----

----- MAIN MENU -----
1 -> Average score of class
2 -> Highest and lowest score of class
3 -> Total absent students
4 -> Marks with highest frequency
5 -> Exit
Choose an option (1-5): 4

-----
Highest frequency is:   1
-----

----- MAIN MENU -----
1 -> Average score of class
2 -> Highest and lowest score of class
3 -> Total absent students
4 -> Marks with highest frequency
5 -> Exit
Choose an option (1-5): 5
'''