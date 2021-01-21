print("Enter a balance and an amount to take out")
x = input().split()
request = float(x[0])
balance = float(x[1])
if balance <= 0:
    print("You have no money")
    exit()
elif (request % 5 != 0) or (balance < request):
    print(balance)
else:
    balance = balance - request -  0.5
    print(balance)