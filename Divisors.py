############### Divisors #################


MyNummer = int(input("Enter Number : "))
devided = []
for i in range(1, MyNummer):
    if MyNummer % i == 0:
        devided.append(i) 

for num in devided:
    print(num)