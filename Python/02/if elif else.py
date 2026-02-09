height = float(input('身高（cm）：'))
weight = float(input('体重（kg）：'))
bmi = weight / (height / 100) ** 2
print('bmi = %.2f' % bmi)
print(f'bmi = {bmi:.2f}')
if 18.5 <= bmi < 24:
    print('你的身体很棒！')
elif bmi < 18.5:
    print('你太瘦了！')
else:
    print('你太胖了！')
