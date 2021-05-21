#Ex03: Crie uma função que receba uma string como
#argumento e retorne a mesma string em letras maiúsculas. 
#Faça uma chamada à função, passando como parâmetro uma string.
def maiusculas(txt):
    return txt.upper()


txt = str(input('Digite uma frase: '))
print(maiusculas(txt))
