import os
import numpy as np

os.system('cls')

monthly_basic_salary  =  float(input('Amount: '))

def sss_contri(salary):
	if salary <= 4249.99:
		contribution = {'msc': 4000.00, 'rer':380.00,'ree':180.00, 'ecc': 10.00}

	elif salary <= 4749.99:
		contribution = {'msc': 4500.00, 'rer':380.00,'ree':180.00, 'ecc': 10.00}














		

	return print(contribution)

sss_contri(monthly_basic_salary)