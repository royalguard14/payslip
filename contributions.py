def pagibig_contri(salary): #2022
	if salary in range(0, 1500+1):
		contribution = salary * 0.01
	elif salary in range(1500, 5000+1):
		contribution = salary * 0.02
	else:
		contribution = 100
	return contribution


def philhealth_contri(salary): #2022
	if salary < 10000:
		contribution = 0
	else:
		contribution = salary * .04
	return contribution


def sss_contri(salary): #2023
	if salary in range(0, 4250):
		contribution = {"mscr": 4000,"mscwisp": 0,"ecc": 10}
	elif salary in range(4250, 4750):
		contribution = {"mscr": 4500,"mscwisp": 0,"ecc": 10}
	elif salary in range(4750, 5250):
		contribution = {"mscr": 5000,"mscwisp": 0,"ecc": 10}
	elif salary in range(5250, 5750):
		contribution = {"mscr": 5500,"mscwisp": 0,"ecc": 10}
	elif salary in range(5750, 6250):
		contribution = {"mscr": 6000,"mscwisp": 0,"ecc": 10}
	elif salary in range(6250, 6750):
		contribution = {"mscr": 6500,"mscwisp": 0,"ecc": 10}
	elif salary in range(6750, 7250):
		contribution = {"mscr": 7000,"mscwisp": 0,"ecc": 10}
	elif salary in range(7250, 7750):
		contribution = {"mscr": 7500,"mscwisp": 0,"ecc": 10}
	elif salary in range(7750, 8250):
		contribution = {"mscr": 8000,"mscwisp": 0,"ecc": 10}
	elif salary in range(8250, 8750):
		contribution = {"mscr": 8500,"mscwisp": 0,"ecc": 10}
	elif salary in range(8750, 9250):
		contribution = {"mscr": 9000,"mscwisp": 0,"ecc": 10}
	elif salary in range(9250, 9750):
		contribution = {"mscr": 9500,"mscwisp": 0,"ecc": 10}
	elif salary in range(9750, 10250):
		contribution = {"mscr": 10000,"mscwisp": 0,"ecc": 10}
	elif salary in range(10250, 10750):
		contribution = {"mscr": 10500,"mscwisp": 0,"ecc": 10}
	elif salary in range(10750, 11250):
		contribution = {"mscr": 11000,"mscwisp": 0,"ecc": 10}
	elif salary in range(11250, 11750):
		contribution = {"mscr": 11500,"mscwisp": 0,"ecc": 10}
	elif salary in range(11750, 12250):
		contribution = {"mscr": 12000,"mscwisp": 0,"ecc": 10}
	elif salary in range(12250, 12750):
		contribution = {"mscr": 12500,"mscwisp": 0,"ecc": 10}
	elif salary in range(12750, 13250):
		contribution = {"mscr": 13000,"mscwisp": 0,"ecc": 10}
	elif salary in range(13250, 13750):
		contribution = {"mscr": 13500,"mscwisp": 0,"ecc": 10}
	elif salary in range(13750, 14250):
		contribution = {"mscr": 14000,"mscwisp": 0,"ecc": 10}
	elif salary in range(14250, 14750):
		contribution = {"mscr": 14500,"mscwisp": 0,"ecc": 10}
	elif salary in range(14750, 15250):
		contribution = {"mscr": 15000,"mscwisp": 0,"ecc": 30}
	elif salary in range(15250, 15750):
		contribution = {"mscr": 15500,"mscwisp": 0,"ecc": 30}
	elif salary in range(15750, 16250):
		contribution = {"mscr": 16000,"mscwisp": 0,"ecc": 30}
	elif salary in range(16250, 16750):
		contribution = {"mscr": 16500,"mscwisp": 0,"ecc": 30}
	elif salary in range(16750, 17250):
		contribution = {"mscr": 17000,"mscwisp": 0,"ecc": 30}
	elif salary in range(17250, 17750):
		contribution = {"mscr": 17500,"mscwisp": 0,"ecc": 30}
	elif salary in range(17750, 18250):
		contribution = {"mscr": 18000,"mscwisp": 0,"ecc": 30}
	elif salary in range(18250, 18750):
		contribution = {"mscr": 18500,"mscwisp": 0,"ecc": 30}
	elif salary in range(18750, 19250):
		contribution = {"mscr": 19000,"mscwisp": 0,"ecc": 30}
	elif salary in range(19250, 19750):
		contribution = {"mscr": 19500,"mscwisp": 0,"ecc": 30}
	elif salary in range(19750, 20250):
		contribution = {"mscr": 20000,"mscwisp": 0,"ecc": 30}
	elif salary in range(20250, 20750):
		contribution = {"mscr": 20000,"mscwisp": 500,"ecc": 30}
	elif salary in range(20750, 21250):
		contribution = {"mscr": 20000,"mscwisp": 1000,"ecc": 30}
	elif salary in range(21250, 21750):
		contribution = {"mscr": 20000,"mscwisp": 1500,"ecc": 30}
	elif salary in range(21750, 22250):
		contribution = {"mscr": 20000,"mscwisp": 2000,"ecc": 30}
	elif salary in range(22250, 22750):
		contribution = {"mscr": 20000,"mscwisp": 2500,"ecc": 30}
	elif salary in range(22750, 23250):
		contribution = {"mscr": 20000,"mscwisp": 3000,"ecc": 30}
	elif salary in range(23250, 23750):
		contribution = {"mscr": 20000,"mscwisp": 3500,"ecc": 30}
	elif salary in range(23750, 24250):
		contribution = {"mscr": 20000,"mscwisp": 4000,"ecc": 30}
	elif salary in range(24250, 24750):
		contribution = {"mscr": 20000,"mscwisp": 4500,"ecc": 30}
	elif salary in range(24750, 25250):
		contribution = {"mscr": 20000,"mscwisp": 5000,"ecc": 30}
	elif salary in range(25250, 25750):
		contribution = {"mscr": 20000,"mscwisp": 5500,"ecc": 30}
	elif salary in range(25750, 26250):
		contribution = {"mscr": 20000,"mscwisp": 6000,"ecc": 30}
	elif salary in range(26250, 26750):
		contribution = {"mscr": 20000,"mscwisp": 6500,"ecc": 30}
	elif salary in range(26750, 27250):
		contribution = {"mscr": 20000,"mscwisp": 7000,"ecc": 30}
	elif salary in range(27250, 27750):
		contribution = {"mscr": 20000,"mscwisp": 7500,"ecc": 30}
	elif salary in range(27750, 28250):
		contribution = {"mscr": 20000,"mscwisp": 8000,"ecc": 30}
	elif salary in range(28250, 28750):
		contribution = {"mscr": 20000,"mscwisp": 8500,"ecc": 30}
	elif salary in range(28750, 29250):
		contribution = {"mscr": 20000,"mscwisp": 9000,"ecc": 30}
	elif salary in range(29250, 29750):
		contribution = {"mscr": 20000,"mscwisp": 9500,"ecc": 30}
	elif salary > 29750:
		contribution = {"mscr": 20000,"mscwisp": 10000,"ecc": 30}

	comp = (contribution['mscr'] * 0.045) + contribution['ecc']
	return comp


def witholding_tax(gross_taxable_earnings, non_taxable_deductions): #2022
	taxable_income = gross_taxable_earnings - non_taxable_deductions 
	if taxable_income < 20833:
		contribution = {"base":0.00, "persentage":0, "over":0}
		dd = 'bracket 1'

	elif taxable_income in range(20833,33332+1):
		contribution = {"base":0.00, "persentage":0.15, "over":20833}
		dd = 'bracket 2'

	elif taxable_income in range(33333,66666+1):
		contribution = {"base":1875.00, "persentage":0.20, "over":33333}
		dd = 'bracket 3'

	elif taxable_income in range(66667,166666+1):
		contribution = {"base":8541.80, "persentage":0.25, "over":66667}
		dd = 'bracket 4'

	elif taxable_income in range(166667,666666+1):
		contribution = {"base":33541.80, "persentage":0.30, "over":166667}
		dd = 'bracket 5'

	elif taxable_income >= 666667:
		contribution = {"base":183541.80, "persentage":0.35, "over":666667}		
		dd = 'bracket 6'

	wht = (contribution['base'] + contribution['persentage'] * (taxable_income - contribution['over']))
	return wht	