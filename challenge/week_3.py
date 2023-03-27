#  - Capture 2 números do teclado (A e B) e caso o primeiro seja maior que o segundo apresente na tela a mensagem "O primeiro número digitado é maior", caso contrário imprima a seguinte mensagem "O segundo número digitado é maior";
num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))

if num1 > num2: 
     print ("O primeiro número digitado é maior!")
else:
     print ("O segundo número digitado é maior!")


# - Digite no teclado a cidade que você nasceu. Caso seja "Recife" a mensagem "Recifense ?" deve aparecer na tela, caso seja "Olinda"  a mensagem "Olindense ?" deve aparecer na tela, caso contrário a mensagem "Legal!" deve aparecer na tela;

cidade = (input("Qual a cidade em que você nasceu? "))

city = ['Recife', 'Olinda']

if cidade == city[0]:
     print ("Tu é recifense, tabacudo!")
elif cidade == city[1]:
     print ("Tu é Olindense!")
else:
     print ("Vem Pra Recife!")



# - Capture 2 números do teclado (A e B) e caso o primeiro seja maior que o segundo apresente na tela a mensagem "O primeiro número digitado é maior";
#          * Caso o primeiro seja par e o segundo seja maior que 10  imprima a seguinte mensagem "Par maior que 10";
#          * Caso o primeiro seja impar e o segundo seja maior que 10  imprima a seguinte mensagem "Impar maior que 10";
#          * Caso o primeiro seja par e o segundo seja menor ou igual a 10  imprima a seguinte mensagem "Par menor ou igual a 10";
#          * Caso o primeiro seja impar e o segundo seja menor ou igual a 10  imprima a seguinte mensagem "Impar menor ou igual a 10";
# - Capture 2 números do teclado (A e B) e
#          * Caso o primeiro seja par ou o segundo seja maior que 10  imprima a seguinte mensagem "Ou é par ou é maior que 10";
#          * Caso o primeiro seja impar e o segundo seja menor que 10  imprima a seguinte mensagem "Ou é Impar menor que 10";
#          * Caso contrário  imprima a seguinte mensagem "Número 10";

num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))

if num1%2 == 0  and num2 > 10:
     print ("Par maior que 10")
elif num1%2 !=0  and num2 > 10:
     print ("Impar maior que 10")
elif num1%2 ==0  and num2 <= 10:
     print ("Par menor ou igual a 10")   
elif num1%2 !=0  and num2 <= 10:
     print ("Impar menor ou igual a 10")     
elif num1%2 ==0  or num2 > 10:
     print ("Ou é par ou é maior que 10")     
elif num1%2 !=0  or num2 > 10:
     print ("Ou é Impar menor que 10") 
else:
    print ("Número 10")

#- Capture 2 números do teclado (A e B) e caso o primeiro seja maior que o segundo apresente na tela a mensagem "O primeiro número digitado é maior", caso contrário imprima a seguinte mensagem "O segundo número digitado é maior";

num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))

if num1 != num2:
     print ("Números diferentes")
else :
     print ("Números diferentes")
     