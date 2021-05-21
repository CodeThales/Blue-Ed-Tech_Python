#Escreva um programa que receba uma string digitada pelo usuário;
#Caso a string seja "medieval", exiba no console "espada";
#Caso contrário, se a string for "futurista", exiba no console "sabre de luz";
#Caso contrário, exiba no console "Tente novamente"
escolha = str(input('''<<< ESCOLHA SEU MODO DE JOGO >>> 
Medieval ou Futurista ''')).strip().capitalize()
if escolha == 'Medieval':
    print('Para o modo Medieval sua arma é a ESPADA!')
elif escolha == 'Futurista':
    print('Para o modo Futurista sua arma é o SABRE DE LUZ!')
