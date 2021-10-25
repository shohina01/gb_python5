with open('test.txt') as file:
    file_ln = file.readlines()
    str_count = 0
    for num, ln in enumerate(file_ln):
        str_count += 1
        w_count = len(ln.split())
        print(f'#{num + 1} - {w_count} words')
    print(f'{str_count} lines')