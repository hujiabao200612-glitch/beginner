total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{i}*{j}={i*j}', end='\t')
    print()
