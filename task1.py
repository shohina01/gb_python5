with open('test.txt', 'w') as file:
    input_tx = input('Text: \n')
    while input_tx:
        file.write(f'{input_tx}\n')
        input_tx = input('Text: \n')
