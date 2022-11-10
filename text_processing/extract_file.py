path = input().split('\\')
name, extension = '', ''
for query in path:
    if '.' in query:
        name, extension = query.split('.')
print(f'File name: {name}\nFile extension: {extension}')
