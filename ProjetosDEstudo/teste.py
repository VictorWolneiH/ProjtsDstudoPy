import time

# imput1=input("qual seu nome?  ")
# imput2=input("qual sua idade?  ")
# name=("nome: ")+imput1
# idadi=("idade: ")+imput2
# certo=("certin")
# erro=("errou feio")
# nemsei=("viajo, fi")

# print(name)
# print(idadi)

# imput3=input("tão novinho? UwU... vamo vê se sabe dos bagui...  quantos?  ")

# if imput3==("todos"):
#     print(certo)
# elif imput3==("todes"):
#     print(erro)
# elif imput3==("todis"):
#     print(erro)
# else:
#     print(nemsei)



      ######CALCULATOR FODA#####

# num1= int(input("escoia 1 numero: "))
# num2= int(input("agr oto: "))

# rstdSoma= num1 + num2
# rstdMulti= num1 * num2
# rstdDiv= num1 / num2
# rstdSub= num1 - num2
# rstdPot= num1 ** num2
# rstdRestDiv= num1 % num2



# print("olá! Eu sou um protótipo de calculadora... vamos começar?")
# operasao = ''
# encerrar = ("fechar")

# while operasao != encerrar:
#      operasao = input("escolha uma operação ou feche a calculadora:  ")
     
#      if operasao == ("somar"):
#         num1= int(input("escoia 1 numero: "))
#         num2= int(input("agr oto: "))
#         rstdSoma= num1 + num2
#         print(f"a soma de {num1} com {num2} resulta em {rstdSoma}")
        
#      elif operasao == ("multiplicar"):
#         num1= int(input("escoia 1 numero: "))
#         num2= int(input("agr oto: "))        
#         rstdMulti= num1 * num2
#         print(f"a multiplicação de {num1} com {num2} resulta em {rstdMulti}")

#      elif operasao == ("dividir"):
#         num1= int(input("escoia 1 numero: "))
#         num2= int(input("agr oto: "))
#         rstdDiv= num1 / num2
#         print(f"a divisão de {num1} por {num2} resulta em {rstdDiv}")

#      elif operasao == ("subtrair"):
#         num1= int(input("escoia 1 numero: "))
#         num2= int(input("agr oto: "))
#         rstdSub= num1 - num2
#         print(f"a diferença entre {num1} e {num2} é {rstdSub}")

#      elif operasao == ("elevar"):
#         num1= int(input("escoia 1 numero: "))
#         num2= int(input("agr oto: "))
#         rstdPot= num1 ** num2
#         print(f"{num1} na potência {num2} resulta em {rstdPot}")

#      elif operasao == encerrar:
#         print ("fechando")

#      else:
#         print("operação não encontrada:", operasao)
    
    



 ####I CAN FIX HER####   olha o espacinho q ela ocupou, compara com a primeira q eu fiz... pqp as função salva msm

somar = ["soma", "somar", "+", "mais", "som", "adição", "adicionar", "adicionamento", "s"]
multiplicar = ["multi", "mult", "mul", "multiplicar", "multiplicação", "multiplicacao", "multiplicaçao", "multiplicacão", "*", "x", "vezes", "v"]
divisao = ["dividir", "divi", "div", "/", "dividido", "divisão", "divisao", "divisionamento", "d"]
subt = ["subtração", "subtraçao", "subtrasao", "subtracao", "subtracão", "diminuir", "subtrair", "menos", "sub", "-", "m"]
eleva = ["elevar", "elevação", "elevaçao", "elevacao", "elevecão", "elevasao", "potência", "potencia", "potenciação", "elevado", "^", "e", "p"]
### ^^^^^^^umas listas com  os nome das função q a calculadora vai ter^
x = '' # criando o X e o Y, mas deixando indefinido pra poder usar depois 
y = ''
fecha= ["fechar", "fecha", "para", "parar", "pare", "encerrar", "encerrando", "encerre", "cala a boca", "por favor para eu te imploro", "burra", "estupida", "estúpida", "idiota", "divide por 0 aí", "divide por zero aí", "calculadora ibecil", "fdp", "daibo", "filha da puta", "smt", "kys", "deus com d minusculo", "eu como cocô no café da manhã e no almoço, amo beber mijo antes de dormir"]  # se eu digitar alguma coisa q tiver dentro dessa lista, a calculadora fecha
operacao = ''  # criando sem definir tbm...
def soma(x, y):    #### função, é um bloquinho de codigo q pode ser nomeado e usado depois, eu to usando pras operações da calculadra, cada operação vai ter uma, e eles são praticamente iguais, só muda, obviamente, a operação de cada um###
      
      rstd = x + y  # X e Y são os numeros q vão ser escolhidos depois, aqui é só uma soma, bem simples msm
      print(f"o resultado é: {rstd}")   ## aqui só tá falando pra mostrar o resultado

def multi(x, y):
      rstd = x * y
      print(f"o resultado é: {rstd}")
   
def divi(x, y):
      try:    ### só a divisão é diferente, pq n da pra dividir por 0, ent eu botei isso pra n da erro, ele só n divide daí
         rstd = x / y
         print(f"o resultado é: {rstd}")    ### resumindo aqui ta escrito tipo: "tenta dividir aí, menos se for dividir por 0, daí só fala q n da"
      except ZeroDivisionError:
         time.sleep(1)
         print("calma aí...")
         time.sleep(4)
         print("não da pra dividir por zero, né fi")

def sub(x, y):
      rstd = x - y
      print(f"o resultado é: {rstd}")

def elev(x, y):
      rstd = x ** y 
      print(f"o resultado é: {rstd}")
      if x == 10 and y == 100:
          print("isso é um GOOGLE")

print("Olá, sou uma calculadora capaz de lidar com as 4 operações básicas e com potências")
time.sleep(3) ### esse negócio é tipo um atrazador, eu coloquei aqui pras coisas n serem tão secas e rapidas
while operacao not in fecha:  ## a condição do loop é, ele só para se eu digitar "fechar" invés de escolher uma operação pra fazer
   operacao = input("escolha uma operação, ou digite 'FECHAR' para sair:  ").lower() #aqui é a "pergunta" q a pessoa vai responder pra fechar ou escolher a operação, o .lower serve pra deixar a resposta em minusculo independente de como a pessoa escrever
   if operacao in somar or operacao in multiplicar or operacao in divisao or operacao in subt or operacao in eleva:  ## começa a brincadeira com 'se a operação estiver na lista...'
      try:
         x = float(input("escolha um numero: "))  ###se a pessoa escolher uma operação valida, aqui ela vai definir o X e o Y, vulgo, escolher os numero
         y = float(input("outro:  "))
      except ValueError:
          print("isso nem é número")
          break
      if operacao in somar:  ### se a pessoa escolheu soma, vai carregar a função de soma, e assim serve pra todas outras
         soma(x, y)

      elif operacao in multiplicar:
         multi(x, y)

      elif operacao in divisao:
         divi(x, y)

      elif operacao in subt:
         sub(x, y)

      elif operacao in eleva:
         elev(x, y)


   elif operacao in fecha:  ### esse elif corresponde ao primero if, ent se oq a pessoa escolher n estiver na lista, mas for "fechar", ent ele vai mostrar o 'fechando', esperar 2sec e fechar o programa.
      print("fechando...")
      time.sleep(2)
   else: ## aqui tbm corresponde à mesma linha, se a pessoa n digitar 'fechar' e não escolher nenhuma função da lista, ent vai mostrar q é invalido
      print(f"digitaste certo? não consegui encontrar nada correspondente à '{operacao}' no meu banco de operações")
      time.sleep(3)#### e vai manter no loop