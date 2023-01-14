from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///caz.db', echo=True)
meta = MetaData()

#Migration
company = Table(
		'company' , meta,
		Column('id', Integer, primary_key=True),
		Column('company_code', String),
		Column('name', String),
		Column('address', String),
		Column('contact', String),
		Column('in', String),
		Column('out', String),
	)

holiday = Table(
	'holidays' , meta,
	Column('id', Integer, primary_key=True),
	Column('company_code', String),
	Column('name', String),
	Column('date', String),
	Column('type', String),
	Column('access', String),

	)

withholding_tax = Table(
	'withholding_tax' , meta,
	Column('id', Integer, primary_key=True),
	Column('payroll_frequency', String),
	Column('bracket', String),
	Column('from', String),
	Column('to', String),
	Column('fix_tax', String),
	Column('tax_rate_on_xcess', String),
	)


sss_contribution = Table(
	'sss_contribution' , meta,
	Column('id', Integer, primary_key=True),
	Column('range_of_compensation_from', String),
	Column('range_of_compensation_to', String),
	Column('monthly_salary_credit_regular_ec', String),
	Column('monthly_salary_credit_wisp', String),
	Column('regular_er', String),
	Column('regular_ee', String),
	Column('ec_ecc', String),
	Column('wisp_er', String),
	Column('wisp_ee', String),
	)


#Seeds








meta.create_all(engine)

