import os
import numpy as np

os.system('cls')

monthly_basic_salary  =  float(input('Amount: '))

def sss_contri(salary):
	if salary <= 4249.99:
		contribution = {'mscec': 4000.00,'mscwisp':0, 'rer':380.00,'ree':180.00, 'ecc': 10.00,'wisper':0.00, 'wispee':0.00}

	elif salary <= 4749.99:
		contribution = {'mscec': 4500.00,'mscwisp':0, 'rer':427.50,'ree':202.50, 'ecc': 10.00,'wisper':0.00, 'wispee':0.00}

	elif salary <= 5249.99:
		contribution = {'mscec': 5000.00,'mscwisp':0, 'rer':475.00,'ree':225.00, 'ecc': 10.00,'wisper':0.00, 'wispee':0.00}














	return print(contribution)

sss_contri(monthly_basic_salary)