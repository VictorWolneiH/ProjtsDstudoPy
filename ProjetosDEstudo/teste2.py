# print("calcunlandum...")

# prN = int(input("escolha um numero "))
# sgN = int(input("agora outro numero "))

# # print(prN+sgN)
# # print(prN-sgN)
# # print(prN*sgN)
# # print(prN/sgN)
# # print(prN**sgN)
# # print(prN%sgN)

# usresultsdasoma = prN + sgN

# print(f"a o resultado de {prN} mais {sgN} é {usresultsdasoma}")

# # print(55 + 45)
# ## 55 + 55 = 110

# palavra=input("qual o pikomon mais pik?")

# print(palavra)



#### exercicio de estado... eu acho, sla, bagulho booleano, if, elif, else...###

# ##1: simulador de comprar pão kkkkk. fzr o preço do pão, pedir quanto de grana o cara tem, se ele tiver a grana, compra, se n tiver, n compra...

# preco = 8.66
# print("o pão tá 8 e 66")
# grana = float(input("Quanto tu tem aí? ó, não faz eu perder meu tempo!  ")) # o 'float' traduz a resposta pra numero, tipo o int, mas ele permite ser um numero quebrado
# if grana == preco:
#     print("trouxe o dinheiro contado, ein? pega aqui teu pão")

# elif grana < preco:
#     print("ti some daqui, mandei n me fzr perder tempo... SEM DESCONTOS")

# elif grana > 500:
#     print("veio comprar a padaria? eu n andaria com tanto dinheiro assim por essas ruas... toma aqui teu pão")

# elif grana > preco:
#     print("aqui seu pão, tenha um bom dia")


# ###2: pedir a temperatura e falar se ta frio, quente, ou normal...

# temperatura = float(input("quantos grau tá aí paizão?  "))
# if temperatura < -5:
#     print("não reclama, aqui em curitiba tá -598423 e os piá tão correndo pelado na rua")

# elif temperatura < 17:
#     print("tá um friozin gostozo ein")

# elif temperatura <= 26:
#     print("tá gostoso n tá? e nós tá como?... só no recolhe")

# elif temperatura > 60:
#     print("como tu n morreu ainda? botou em fahrenheit o bagulho?")

# elif temperatura > 26:
#     print("tá calor fi, vamo toma um banho na sanga")


####3: é pra fzr mensagem de bom dia/noite conforme a hora... achei meio complicado pra um exercicio de iniciante, mas ok. bora tentar
import time
def hora():
    horaagora = time.asctime()
    return(horaagora[11], horaagora[12])
if hora() == ("1", "2") or hora() == ("1", "3") or hora() == ("1", "4") or hora() == ("1", "5") or hora() == ("1", "6") or hora() == ("1", "7"):
    print("poa tarte pra tu tambem ali né")

elif hora() == ("0", "6") or hora() == ("0", "7") or hora() == ("0", "8") or hora() == ("0", "9") or hora() == ("1", "0") or hora() ==("1", "1"):
    print("Good Morning, Sunshine ")

elif hora() == ("1", "8") or hora() == ("1", "9") or hora() == ("2", "0") or hora() == ("2", "1") or hora() == ("2", "2") or hora() == ("2", "3"):
    print("até oto tia então né, ta tarte, temq ta panho no nene ainda")

else:
    print("é o dormes, n tem como")
### eu acho q vai dá  boa tarde msm quando for 21, já q, mt provavelmente a ordem n importa, e eu n sei fzr a ordem importar... tbm vai ter bagulho as 01 e 02 sipá... eu mexi um pouco, tlvz agr a ordem passe a importar, vamo vê daí


# ####4 e ultimo: temq botar algumas condições com and e or em apenas um if

# idadeA = int(input("what iour idadi? ")) 
# condic = input("tu tá bonzin? ")
# medico = False

# if (idadeA >= 18 and idadeA <= 35) and (condic == "sim" or medico):   
#     print("então pode ir")
# elif idadeA <18:                        ###### fiz varios elif, mas acho q atendi o exercicio, pq fiz certin no if, o resto nem importa, é só meme
#     print("nem desmamou ainda, guri... xispa daqui")
# elif idadeA >35:
#     print("se levantar os braço Deus puxa, pode ir pra casa, e cuida pra n cair e quebrar a bacia")
# else:
#     print("vai morrer")


# #######EXERCICIOS DE LOOOOOOP
# #1: exibir numeros de 1 a 10 com while... n entendi direito, pq parece bem facil sla
# num = 0
# while num < 10:
#     num +=1    
#     print(num)

# ###2: criar uma tabuada interativa por input, escolhe um numero e mostra a tabuada dele
# escolhaumnumero = int(input("quer ver a tabuada de qual numero?  "))
# multiplicadores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n in multiplicadores:
#     n *= escolhaumnumero
#     print(n)


# ###3: tabuada de 1 a 100
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n in lis:
#     for m in range(1, 101):
#         m *= n
#         print(m)

# ###4:  contar as vogais de uma str
# ndv = 0
# vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'à', 'ã', 'â', 'ä', 'é', 'è', 'ẽ', 'ê', 'ë', 'í', 'ì', 'ĩ', 'î', 'ï', 'ó', 'ò', 'õ', 'ô', 'ö', 'ú', 'ũ', 'ù', 'û', 'ü']
# apalavara = input("digite qualquer coisa: ")
# for letra in apalavara:
#     if letra in vogais:
#         ndv +=1         ################# EU NÃO SEI FAZER ISSOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!
#                 #######CONSEGUIIIIIIIIIIIIIII!!!!!!!!!! POHAAAAAAAAAAAAAAA
# print(f"A quantidade de VOGAIS em '{apalavara}' é: {ndv}")




