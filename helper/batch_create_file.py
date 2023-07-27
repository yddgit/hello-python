names = ['a', 'b', 'c>']
for name in names:
    filename = name.replace('>', '') + '.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('')