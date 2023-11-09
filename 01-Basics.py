value = input("Enter a value: ")

print('you said ' + value)
print('lenth of the input is ' + str(len(value)) + ' characters')
while value != 'quit':
    value = input("Enter a value: ")
    print('you said ' + value)
    print('lenth of the input is ' + str(len(value)) + ' characters')
print('bye')

for i in range(1, 10):
    print(i);