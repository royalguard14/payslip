#NOTE: This is limited to PRIVATE EMPLOYEE thats why SSS contibution is must.

import os, time, sys
from style import *
from contributions import *
from myFunc import *
from datetime import datetime

clear()
bc = bcolors()

# loading()
# print(bc.CLEAN_SCREEN)
info = {}
emp_no = input("Input Employee no.: ")
z = open_file('employee')
for i in z:
    if i['emp_id'] == emp_no.upper():
        
        #for name
        if i['suffix'] == 'None' or i['suffix'] == 'none' or i['suffix'] == 'N/A':
            info['name'] = i['last_name'] + ", " + i['first_name'] + " " + i['middle_name'][0] + "."
        else:
            info['name'] = ['last_name'] + ", " + i['first_name'] + " " + i['middle_name'][0]+". "+ i['suffix']
        
        info['emp_id'] = i['emp_id']
        info['datehired'] = i['datehired']
        info['status'] = i['status']
        

        basic_salary = float(input("Enter your Monthly Basic Salary: "))
        ta = float(input("Enter your Taxable Allowance: "))
        nta = float(input("Enter your Non-taxable Allowance: "))
        nd = float(input("Enter your Night Differentialy: "))
        op = float(input("Enter your Overtime Pay: "))

        ntd = sss_contri(basic_salary) + philhealth_contri(basic_salary) + pagibig_contri(basic_salary)
        tg = basic_salary + ta + nta + nd + op
        td = sss_contri(basic_salary) + philhealth_contri(basic_salary) + pagibig_contri(basic_salary) + witholding_tax(tg,ntd)




        #PAYSLIP TEMPLATE
        clear()
        print(bc.DEFAULT_WARNING + "REPUBLIC OF THE PHILIPPINES".center(100) +bc.DEFAULT_ENDC)
        print(bc.DEFAULT_WARNING + "CAZ DEVELOPER".center(100) +bc.DEFAULT_ENDC)
        print(bc.DEFAULT_WARNING + "OFFICIAL PAYROLL SLIP".center(100) +bc.DEFAULT_ENDC)
        print('FOR THE MONTH {} {}\n'.center(95).format(datetime.now().strftime('%B'), datetime.now().strftime('%Y')))
        
        print(bc.DEFAULT_HEADER + bc.UNDERLINE + " ".center(100) + bc.DEFAULT_ENDC)
        print(bc.DEFAULT_HEADER + bc.UNDERLINE +"EMPLOYEE INFORMATION".center(100) +bc.DEFAULT_ENDC)


        print("Name:\t{}						Position: Developer".format(info['name']))
        print("employee_no:\t{}					Contact no.: {}".format(info['emp_id'],'0927-7294457'))
        print("date hiring:\t{}					Status: {}".format(info['datehired'],info['status'].title()))
       
        print(bc.DEFAULT_HEADER + bc.UNDERLINE + " ".center(100) + bc.DEFAULT_ENDC)
        print(bc.DEFAULT_HEADER + bc.UNDERLINE +"GROSS SALARY".center(100) +bc.DEFAULT_ENDC)
        

        print("Basic Pay:\t\t\t\t{}".format(basic_salary))
        print("Taxable Allowance:\t\t\t{}".format(ta))
        print("Non-taxable Allowance\t\t\t{}".format(nta))
        print("Night Differential:\t\t\t{}".format(nd))
        print("Overtime Pay:\t\t\t\t{}".format(op))
        print("\nTOTAL:\t\t\t\t\t{}".format(tg))


        print(bc.DEFAULT_HEADER + bc.UNDERLINE + " ".center(100) + bc.DEFAULT_ENDC)
        print(bc.DEFAULT_HEADER + bc.UNDERLINE +"DEDUCTIONS".center(100) +bc.DEFAULT_ENDC)



        print("SSS Contribution:\t\t\t{}".format(sss_contri(basic_salary)))
        print("Philhealth Contribution:\t\t{}".format(philhealth_contri(basic_salary)))
        print("PAG-IBIG Contribution:\t\t\t{}".format(pagibig_contri(basic_salary)))
        print("Withholding Tax:\t\t\t{}".format(witholding_tax(tg,ntd)))
        print("\nTOTAL:\t\t\t\t\t{}".format(td))

        print(bc.DEFAULT_HEADER + bc.UNDERLINE + " ".center(100) + bc.DEFAULT_ENDC)
        print(bc.DEFAULT_HEADER + bc.UNDERLINE +"NET PAY".center(100) +bc.DEFAULT_ENDC)

        

        print("\nTOTAL:\t\t\t\t\t{}".format(tg - td))



        

		
























    else:
        pass






# #sss_computation
# sss_table = sss_contri(basic_salary)







