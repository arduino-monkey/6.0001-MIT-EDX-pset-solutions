monthlyIntrestRate = annualInterestRate/12
b = balance
low = b/12
high = (b*(1+monthlyIntrestRate)**12)/12
payment = (high + low)/2

def balance_left(b, payment, monthlyIntrestRate):
    for i in range(12):
        b -= payment
        b += monthlyIntrestRate*b
    return b

temp = balance_left(b, payment, monthlyIntrestRate)
while temp < 0 or abs(temp) > 1:
    balance_left_after = balance_left(b, payment, monthlyIntrestRate)
    if balance_left_after < 0:
        high = payment
    else:
        if balance_left_after > high:
            high = payment
        else:
            low = payment
    payment = (high+low)/2
    temp = balance_left(b, payment, monthlyIntrestRate)
print(round(payment,2))