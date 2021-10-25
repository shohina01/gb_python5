with open('test.txt') as file:
    file_ln = file.readlines()
    emp = {}
    sum_salary = 0
    for ln in file_ln:
        emp_info = ln.split()
        emp.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
avr_sal = sum_salary / len(emp)
print(f'Average salary = {avr_sal}')

for srn, money in emp.items():
    if money < 20000:
        print(f'{srn} : {money}')
