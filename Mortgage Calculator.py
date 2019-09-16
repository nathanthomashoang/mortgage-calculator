# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:58:34 2019

MORTGAGE CALCULATOR

@author: Nathan Hoang
"""

def fixed_mortgage_payment(principal,rate,months_term):
    return principal*((rate * (1 + rate)**months_term) / \
                      (((1 + rate)**months_term)-1))

def shell():
    print('Welcome to the Mortgage Calculator.\n\nThis program will \
calculate your monthly mortgage payment per month based on your loan amount, \
annual interest rate, and compound period (Optional)')
    while True:
        principal = float(input('Please enter the principal: $'))
        rate = (float(input('\nPlease enter the annual interest rate (%): '))\
                *0.01)
        months_term = int(input('Please enter the term of the mortage in \
MONTHS.\nCommon mortgage terms are 15 years(180 months) or \
30 years(360 months): '))
        while True:
            try:
                compound_dec = input('Adjust compound interval? (Default is \
monthly) select "Y" or "N": ')
            except:
                print('Please select only "Y" or "N"')
            else:
                if compound_dec.lower() == 'y':
                    compound_period = int(input('Please enter a compound \
interval per year (12 is monthly, 32 is semi-weekly, 52 is weekly, \
365 is daily): '))
                    rate = (1 + rate/compound_period)**(compound_period/12)-1
                    monthly_payment = \
                    fixed_mortgage_payment(principal,rate,months_term)
                    
                    total_paid = monthly_payment*months_term
                    total_interest = total_paid - principal
                    print (f'\nMonthly Payment: ${monthly_payment:.2f}')
                    print (f'Total of {months_term} \
payments: ${total_paid:.2f}')
                    print (f'Total interest: ${total_interest:.2f}')
                    break
                if compound_dec.lower() == 'n':
                    rate /= 12
                    monthly_payment = \
                    fixed_mortgage_payment(principal, rate, months_term)
                    total_paid = monthly_payment*months_term
                    total_interest = total_paid - principal
                    print (f'\nMonthly Payment: ${monthly_payment:.2f}')
                    print (f'Total of {months_term} payments: \
${total_paid:.2f}')
                    print (f'Total interest: ${total_interest:.2f}')
                    break
                
        restart = input('Calculate again? \
Select "Y" or any other key to quit: ')
        if not restart.lower() == 'y':
            break

shell()
                
            