a = float(input("Enter a starting number: "))
r  = float(input("Enter a common ratio: "))
i = 0
print("Geometric series starting with {} and with comman difference of {} is:\n".format(a, r))
l = [a * (pow(r,n)) for n in range(10)]
print(l)
sum(l)