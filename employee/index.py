# id, emp_id, first_name, last_name, Middle_name, suffix, birthdate, status,dependent





print("""\
                CAZ HRIS WITH PAYROLL
    (1) Hire Employee                       
    (2) View Employee                      
    (3) Update Employee                    
    (4) Fired Employee                    
    (0) Exit                           	   
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

        case '4':
            print("You can become a backend developer")

        case '0':
            print("You can become a mobile app developer")
            ex = True
            clear()


        case _:
            print("Invalid Number")
clear()            
