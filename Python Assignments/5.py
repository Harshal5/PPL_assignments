l = []
while(True):
    n = str(input("Enter page: "))
    if(n == '-1'):
        break
    l.append(n)
x = []
for page in l:
    if('-' in page):
        x.extend(range(int(page.split('-')[0]), int(page.split('-')[1])+1))
    else:
        x.append(int(page))
missing = list(set([n for n in range(1,26)]) - set(x))
print(missing)