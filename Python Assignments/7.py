start, end = input("enter start and end point:\n").split()
a = []
for num in range(int(start),int(end)+1):
    l = list(map(lambda x: x ** 3, [int(i) for i in str(num)]))
    if(sum(l) == num):
        a.append(num)
print("Amstrong Numbers are:")
print(a)    