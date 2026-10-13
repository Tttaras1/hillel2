height = int(input('Type in height for rect: '))
width = int(input('Type in width for rect: '))

for n in range(0, height):
    for i in range(0, width):
        print('*', end = '')
    print('')

# right-angled triangle
for n in range(0, height + 1):
    print(n*'*')
    
print('')
# reversed right-angled triangle
for n in range(height, 0, -1):
    print(n*'*')

print('')
# Rect with spaces
for n in range(0, height):
    is_first_or_last_line = n != 0 and n != height - 1
    for i in range(0, width):
        symbol = '*'
        is_middle = i != 0 and i != width - 1
        if is_first_or_last_line and is_middle:
            symbol = ' '
        print(symbol, end = '')
    print('')
