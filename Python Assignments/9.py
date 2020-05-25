def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

divisor = []
har_num = []
count = 0
import statistics 
for i in range (1, 10000):
    if count >= 10:
        break
    divisor = [j for j in range(1, i + 1) if i % j == 0]
    num = (statistics.harmonic_mean(divisor))
    if is_integer_num(num):
        har_num.append(int(i))

print(har_num)