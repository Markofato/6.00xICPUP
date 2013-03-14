balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

b,r,p,m,tp = balance, annualInterestRate, balance * monthlyPaymentRate, 0, 0

while m < 12:
    ub = b - p
    #monthlyInterest
    i = (r/12.0) * ub
    print("Months: {0}\nMinimum monthly payment: {1}".format(m,round(p,2)))
    tp += p
    #outStandingBalance for next month
    b = ub + i
    if m != 11:
        print('Remaining balance: {0}'.format(round(ub,2)))
    else:
        print('Remaining balance: {0}'.format(round(b,2)))
    #minimumAmountToPay for next month
    p = b * monthlyPaymentRate
    m += 1
print("Total Paid: {0}\nRemaining Balance: {1}".format(round(tp,2), round(b,2)))
    
#Passed both TestCases.
