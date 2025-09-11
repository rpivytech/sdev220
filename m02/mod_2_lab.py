'''
Riley Poulin
mod_2_lab.py
Determines if the student made the Dean's List or the Honor Roll.
'''

lName = str("")
fName = str("")
gpa = float(0.0)
deans = float(3.5)
honors = float(3.25)
quit = str("ZZZ")
doStuff = bool(True)

while doStuff == True:
    lName = input("Please enter the student's last name, or ZZZ to quit: ")
    if lName == "ZZZ":
        print("Quitting...")
        doStuff = False
    else:
        fName = input("Please enter the student's first name: ")
        gpa = float(input("Please enter the student's GPA: "))
        if gpa >= deans:
            print(fName, lName, "has made the Dean's List.")
        elif gpa < deans and gpa >= honors:
            print(fName, lName, "has made the Honor Roll.")
        else:
            print(fName, lName, "has not made the Dean's List nor the Honor Roll.")
