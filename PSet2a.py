balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
months = 0
#expected tp = 1165.63 <3
#expected ub = 4961.11 -> 4621.78

#set initial values for b, r, p, tp
b = balance
r = annualInterestRate
p = round(balance * monthlyPaymentRate, 2)
#totalAmountPaid
tp = 0

while months < 12:
    #unpaidBalance
    ub = round( b - p , 2)
    #monthlyInterest
    i = round((r/12.0) * ub, 2)
    tp += p
    print(i)
    print('Months: ' + str(months))
    print('Minimum monthly payment: ' + str(p))
    print('Remaining balance: ' + str(ub))
    #outStandingBalance for next month
    b = round( (ub + i) , 2)
    #minimumAmountToPay for next month
    p = round( b * monthlyPaymentRate , 2)
    
    months += 1
    print('')
print(tp)

