##Written by rishin patra on 9-feb-2021
##gmit training python 
##Accepting the marks in integer value between 0 to 100 
grade=int(input("Enter the marks(0-100): "))
##Checking for valid number
if 0>grade or grade>100:
    print("!!INVALID INPUT!!")
##Grading according to the marks
else:
    if grade>=91:
        print("Grade = O")
    elif grade>=81:
        print("Grade = E")
    elif grade>=71:
        print("Grade = A")
    elif grade>=61:
        print("Grade = B")
    elif grade>=50:
        print("Grade = C")
    else:
        print("Grade = Fail")
    