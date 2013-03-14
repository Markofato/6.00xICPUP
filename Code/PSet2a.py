balance = 500000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
months = 0
#expected tp = 1165.63 <3
#expected ub = 4961.11 -> 4621.78

#set initial values for b, r, p, tp
b = balance
r = annualInterestRate
p = balance * monthlyPaymentRate
#totalAmountPaid
tp = 0

while months < 12:
    #unpaidBalance
    #if months == 11:
       # m12ub = b
    ub = b - p
    #monthlyInterest
    i = (r/12.0) * ub
    tp += p
    print(i)
    print('Months: ' + str(months))
    print('Minimum monthly payment: ' + str(p))
    
    #outStandingBalance for next month
    b =(ub + i)
    if months != 11:
        print('Remaining balance: ' + str(ub))
    else:
        print('Remaining balance: ' + str(b))
    #minimumAmountToPay for next month
    p =b * monthlyPaymentRate
    
    months += 1
    print('')
print(tp)

