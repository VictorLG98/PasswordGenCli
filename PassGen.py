import random
import string

digitos = []
lista = []
simbolos = ['*', '?', '.', '^', ',', '!']
for letter in string.ascii_letters:
    lista.append(letter)

for num in string.digits:
    digitos.append(num)

todo = digitos + lista + simbolos

def gen_pass(lon):
    password = ""
    for i in range(lon):
        password += random.choice(todo)
    return password

