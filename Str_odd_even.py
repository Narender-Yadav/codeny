user_string = input('Enter the string')
print('Original String:', user_string)
len_input = len(user_string)

for i in range(1, len_input - 1, 2):
    print('Even values : index[", i, "]', user_string[i])

for i in range(0, len_input + 1, 2):
    print('Odd values : index[", i, "]', user_string[i])

