###
### Author: Cumhur Aygar
### Course: CSc 110
### Description: A program to help you sort out your finances
###              using basic calculations.
###

import os
print('''-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------
''')
annual_salary =int(input("What is your annual salary?\n"))

rent =int(input("How much is your monthly mortgage or rent?\n"))

bills = int(input("What do you spend on bills monthly?\n"))

food = int(input("What are your weekly grocery/food expenses?\n"))

travel = int(input("How much do you spend on travel annually?\n"))

annual_salary = format(annual_salary, '11,.2f')
print(f'''
------------------------------------------------------------------------------------------------------
See the financial breakdown below, based on a salary of ${annual_salary}
------------------------------------------------------------------------------------------------------''')
spaces_a = 11 - count(str(annual_salary))
annual_salary = format(annual_salary, '11,.2f')
tax = 0
extra = 0

if annual_salary >= 200000:
   tax =  30/100
elif annual_salary >= 75000:
    tax = 25/100
elif annual_salary >= 15000:
    tax = 20/100
else:
    tax = 10/100
if tax*annual_salary >= 75000:
    tax = 75000

else:
    tax = tax*annual_salary

    extra = (annual_salary - (travel + food + bills + tax)

rent = format(float(rent*12), '11,.2f')
frent = format(float(rent/annual_salary*100), '4.1f')

bills = format(float(bills)*12, '11,.2f')
fbills = format(float(fbills/annual_salary*100)), '4.1f')


food = format(float(food)*52, '11,.2f')
ffood = format(float(food/annual_salary*100), '4.1f')


travel = format(float(travel), '11,.2f')
ftravel = format(float(ftravel/annual_salary*100), '4.1f')

ftax = tax/annual_salary
fextra = extra/annual_salary

print(f'''
| mortgage/rent | $'''{rent}'''|'''{frent}'''|
|         bills | ${bills}|{fbills}|
|          food | ${food}|{ffood}|
|        travel | ${travel}|{ftravel}|
|           tax | ${tax}|{ftax}|
|         extra | ${extra}|{fextra}|
------------------------------------------------------------------------------------------------------
''')


