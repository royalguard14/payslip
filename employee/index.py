# id, emp_id, first_name, last_name, Middle_name, suffix, birthdate, status,dependent
import os
import sys
import ast
import pandas as pd
sys.path.insert(0, 'C:/Users/Admin/Desktop/payslip')
from myF import *
os.system('cls')
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
            break
        

        case '2':
            z = open_file('employee')
            ids = []
            emp_id = []
            name = []
            for i in z:
                if i['suffix'] == 'None' or i['suffix'] == 'none':
                    name.append(i['last_name'] + ", " + i['first_name'] + " " + i['middle_name'][0] + ".")
                else:
                    name.append(i['last_name'] + ", " + i['first_name'] + " " + i['middle_name'][0]+". "+ i['suffix'])
                ids.append(i['id'])
                emp_id.append(i['emp_id'])
            df = pd.DataFrame({'id': ids,'employment id': emp_id,'name': name})
            print(df)
        

        case '3':
            #view DataFrame
            print(df)
        

        case '4':
            print("You can become a backend developer")
        

        case '0':
            print("You can become a mobile app developer")
            ex = True
            clear()
        

        case _:
            print("Invalid Number")
clear()            
