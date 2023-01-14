from myF import *

print("""\
                CAZ HRIS WITH PAYROLL
    (1) Dashboard                      Display Data Static 
    (2) Employee                       Manage Employees
    (3) Generate                       Generate Payslip
    (0) Exit                           Exit program
""")

ex = False
while ex != True:
    module_option = input("Select the number of the Module you want to Access: ")
    match module_option:
        case '1':
            print("Dashboard Under Construction")

        case '2':
            print("You can become a Data Scientist")

        case '3':
            print("You can become a backend developer")

        case '0':
            print("You can become a mobile app developer")
            ex = True
            clear()


        case _:
            print("Invalid Number")
clear()            
