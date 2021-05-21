#Elaborar um programa que recebe o seu nome,
#endereço e hobby e mostra cada uma das
#informações da seguinte forma:
#Nome -> Letra maiúscula
#Endereço -> Letra minúscula
#Hobby -> Primeira letra maiúscula
nome = str(input('Digite seu nome: ')).upper()
endereço = str(input('Digite seu endereço: ')).lower()
hobby = str(input('Qual o seu hobby? ')).capitalize()
print(nome)
print(endereço)
print(hobby)
