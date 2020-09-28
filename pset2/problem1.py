monthlyIntrestRate = annualInterestRate/12
for i in range(12):
    MinimumMonthlyPayment = monthlyPaymentRate*balance
    balance -= MinimumMonthlyPayment
    balance += monthlyIntrestRate*balance
print(round(balance,2))