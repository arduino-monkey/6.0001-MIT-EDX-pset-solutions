b = balance
monthlyIntrestRate = annualInterestRate/12
lowestPayment = 10

def f(b,lowestPayment,monthlyIntrestRate):
    for i in range(12):
        b -= lowestPayment
        b += monthlyIntrestRate*b
    return b

while f(b, lowestPayment,monthlyIntrestRate) > 0:
    lowestPayment += 10

print(lowestPayment)