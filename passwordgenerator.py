import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exception = 'il1Lo0O'
chars = ''
passwords = []
n = ''
while not isinstance(n, int):
    try:
        n = int(input('How many passwords do you want to generate?'))
    except ValueError:
        print('Enter number!')
        n = ''
for i in range(1, n + 1):
    print(f'Enter data for password #{i}:')
    paslen = ''
    while not isinstance(paslen, int):
        try:
            paslen = int(input("What password length do you want?"))
        except ValueError:
            print('Enter number!')
            paslen = ''
    digit = input('Include digits? y/n?')
    ualpha = input('Include upper case? y/n?')
    lalpha = input('Include lower case? y/n?')
    spec = input('Include special symbols? y/n?')
    exc = input('Exclude ambiguous characters il1Lo0O? y/n')
    if digit == 'y':
        chars += digits
    if ualpha == 'y':
        chars += uppercase_letters
    if lalpha == 'y':
        chars += lowercase_letters
    if spec == 'y':
        chars += punctuation
    if exc == 'y':
        for j in exception:
            if j in chars:
                chars = chars.replace(j, '')


    def generate_password(paslen, chars):
        password = ''
        for i in range(paslen):
            password += chars[random.randrange(len(chars))]
        return password


    password = generate_password(paslen, chars)
    print(f'Password №{i}: {password}')
    passwords.append(password)
print('Your passwords:')
for i in range(len(passwords)):
    print(f'Password #{i + 1}: {passwords[i]}')
