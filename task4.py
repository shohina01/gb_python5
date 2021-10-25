nums = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре"
}
with open('test.txt') as file, open('n_file.txt', 'w') as n_file:
    file_ln = file.readlines()
    for ln in file_ln:
        data = ln.split()
        rus_num = nums.get(data[0])
        n_file.write(f'{ln.replace(data[0], rus_num)}')

