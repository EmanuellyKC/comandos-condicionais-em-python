"""
Exercício 1
Ler um número inteiro entre 0 e 100, informar o quanto ele está distante de um
determinado número chave, também lido no próprio programa. """

num = int(input("Digite um número inteiro entre 1 e 100: "))
numChave = 17
conta1 = num - numChave
conta2 = numChave - num
if num > numChave:
    print("Resposta = ", conta1)
else:
    print("Resposta = ", conta2)

""" 
Exercício 2
A nova regra de aposentadoria leva em conta o tempo de contribuição ao INSS somada à idade do empregado, levando-se em conta a seguinte fórmula:
TC + ID ≥ (Ano pretende aposentar – Ano Atual)//2 + 85 – para Sexo Feminino;
TC + ID ≥ (Ano pretende aposentar – Ano Atual)//2 + 95 – para Sexo Masculino;
Se o resultado da fórmula acima do verdadeiro, o empregado poderá se aposentar. Fazer um algoritmo para ler o Tempo de Contribuição ao INSS (TC); Idade do empregado (ID); Ano pretende aposentar; Ano atual; Sexo do empregado (“M”/”F”).
Escrever mensagem: “O empregado poderá se aposentar”; caso contrário “O empregado não poderá se aposentar”. Se o ano que o empregado pretende aposentar for menor que o ano atual, escrever mensagem: “Ano inválido. Não é possível cálculo”. """

tc = float(input("Qual seu tempo de contribuição:"))
id = float(input("Qual sua idade de trabalho:"))
anoAP = int(input("Em qual ano você pretende aposentar ? :"))
anoAtual = 2024
if anoAP < anoAtual :
    print("Ano invalido. Não é possivel calculo.")
aposentadoriaM = (anoAP - anoAtual)//2 + 95
aposentadoriaH = (anoAP - anoAtual)//2 + 85
somaTCID = tc + id
sexo = input("Digite m para mulher e h para homem: ")
if sexo == "m" :
    if somaTCID >= aposentadoriaM :
        print("O empregado poderá aposentar.")
    else :
        print("o empregado não poderá aposentar.")
if sexo == "h" :
    if somaTCID >= aposentadoriaH :
        print("O empregado poderá aposentar.")
    else :
        print("o empregado não poderá aposentar.")


"""
Exercício 3
Faça um algoritmo para ler um caracter que representará um tipo de média a ser calculado (G – Geométrica; P – Ponderada; H – Harmônica; A – Aritmética) 
e três números reais (x, y, z). Caso seja informado um caracter diferente, escrever mensagem: “Erro. Caracter inválido.” Escrever o tipo de média e o valor da média. """

caracter = input("Digite G (Geométrica), P (Ponderada), H (Harmônica), A (Aritmética): ")
if caracter.lower() != "g" and caracter.lower() != "p" and caracter.lower() != "h" and caracter.lower() != "a":
    print("Caracter invalido!")
else :
    numX = float(input("Informe o valor de X: "))
    numY = float(input("Informe o valor de Y: "))
    numZ = float(input("Informe o valor de Z: "))
    if caracter.lower() == "g":
        geometrica = round((numX * numY * numZ) ** (1/3),2)
        print(f"Geométrica = {geometrica}")
    elif caracter.lower() == "p":
        ponderada = round(numX + 2 * numY + 3 * numZ/6,2)
        print(f"Ponderada = {ponderada}")
    elif caracter.lower() == "h":
        harmonica = round(1/( 1/numX + 1/numY +1/numZ),2)
        print(f"Harmonica = {harmonica}")
    elif caracter.lower() == "a" :
        aritimetica = round(numX + numY + numZ/3 ,2)
        print(f"Aritimetrica = {aritimetica}")


"""
Exercício 4
As tarifas de certo parque de estacionamento seguem a seguinte ordem:
- Até 2ª hora R$ 1,00 cada hora
- Da 3ª até a 5ª hora R$ 1,40 cada hora
- Acima da 5ª hora R$ 1,60 cada hora
Fazer um algoritmo para ler a quantidade de horas que o carro ficou estacionado (inteiro) e escrever o valor pago. """

hora = float(input("Informe quantas horas voce ficou no estacionamento:"))
if horas <= 2:
    preco = horas * 1
    print(f"Você vai pagar R${preco}")
elif horas >= 3 and horas <= 5:
    valor = horas - 2
    preco1 = 2
    preco2 = round(valor * 1.4,2)
    vPago = preco1 + preco2
    print(f"Você vai pagar R${vPago}")
else:
    valor = horas - 5
    preco1 = 2
    preco2 = 3 * 1.4
    preco3 = round(valor * 1.6,2)
    vPago = round(preco1 + preco2 + preco3,2)
    print(f"Você vai pagar R${vPago}")


"""
Exercício 5
Ler 3 números inteiros (considere que não serão informados valores iguais) e escrever a soma dos dois maiores números lidos. """

num1 = int(float("Digite um número : "))
num2 = int(float("Digite outro número : "))
num3 = int(float("Digite mais um número : "))
if num1 == num2 and num1 == num2 or num2 == num1 and num2 == num3:
    print("Evite repitir")
else:
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            soma = num1 + num2
            print(f"A soma é {soma}")
        else:
        soma = num1 + num3
        print(f"A soma é {soma}")
    elif num2 > num1 and num2 > num3:
    if num1 > num3:
        soma = num2 + num1
        print(f"A soma é {soma}")
    else:
         soma = num2 + num3
         print(f"A soma é {soma}")
else:
    if num1 > num2:
        soma = num3 + num1
        print(f"A soma é {soma}")
    else:
        soma = num3 + num2
        print(f"A soma é {soma}")


"""
Exercício 6
Um posto está vendendo combustíveis com as seguintes informações:
- até 20 litros, desconto de 3% por litro - Álcool
- acima de 20 litros, desconto de 5% por litro - Álcool
- até 20 litros, desconto de 4% por litro - Gasolina
- acima de 20 litros, desconto de 6% por litro - Gasolina
Escreva um algoritmo que leia o tipo de combustível, número de litros vendidos e o preço do litro. Calcule e imprima o valor a ser pago pelo cliente. """

combustivel = input("Digite A para alcool ou G para gasolina: ")
if combustivel.lower() != "g" and combustivel.lower() != "a":
    print("Esse combustivel não existe!")
else:
    if combustivel.lower() =="a":
        alcool = float(input("Quantos litros você quer colocar ? : "))
        litroAl = float(input("Qual é o preço do litro do alcool?: "))
        if alcool > 0 and alcool <= 20:
            preço = round((litroAl * alcool) * 0.03,2)
            print(f"Você irá pagar R$ {preço}")
        else:
            preço = round((litroAl * alcool) * 0.05,2)
            print(f"Você irá pagar R$ {preço}")
    elif combustivel.lower() == "g":
        gasolina = float(input("Quantos litros de gasolina voce colocou? : "))    
        litroG = float(input("Qual é o preço do litro do gasolina? : "))
        if gasolina > 0 and gasolina <= 20:
            preço = round((litroG * gasolina) * 0.03,2)
            print(f"Você irá pagar R$ {preço}")
        else :
            preço = round((litroG * gasolina) * 0.05,2)
            print(f"Você irá pagar R$ {preço}")
