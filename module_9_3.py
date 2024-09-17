first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x[0])-len(x[1])) for x in list(zip(first, second)) if len(x[0]) != len(x[1]))
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(0, min(len(first), len(second))))
print(list(second_result))
