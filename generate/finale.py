import os
os.system('cls')

#information
e_name = input("Employee Name: ")
r_hours = int(input("Rendered Hours: "))
rate = float(input("Rate per Hours: "))
sss= float(input("SSS Contribution: "))
philhealth = float(input("PhilHealth Contribution: "))
loans = float(input("Loans: "))

#computation
gross = r_hours * rate

total_deduct = sss + philhealth + loans 
net_salary = gross - total_deduct

#fix Style
fe_name =("Employee Name: {}".format(e_name))
fr_hours =("Rendered Hours: {}".format(r_hours))
frate =("Rate per Hours: {}".format(rate))
fsss =("SSS: {}".format(sss))
fphilhealth =("PhilHealth: {}".format(philhealth))
floans =("Loans: {}".format(loans))
fgross =("Gross Salary: {}".format(gross))
ftotal_deduct = ("Total Deductions: {}".format(total_deduct))
fnet_salary = ("Php: {}".format(net_salary))


os.system('cls')

print("================PAYSLIP================")
print("=========EMPLOYEE INFORMATION==========")
print(fe_name)
print(fr_hours)
print(frate)
print(fgross)
print("===============DEDUCTIONS===============")
print(fsss)
print(fphilhealth)
print(floans)
print(ftotal_deduct)
print("===============NET SALARY===============")
print(fnet_salary)