##LISTAS##

pokemon = ["lugia", "banette", "delphox"]   #isso é uma lista, precisa dos []

pokemon[1] = "darkrai"  #esse aqui substitui um dos itens da ista, o q tá entre [] é o numero doq vai substituir, no caso aqui é o 1, banette, já q começa no 0, ent o lugia é 0 e o banette é 1

pokemon.append("glaceon")   #aqui temq colocar o .append na variavel, o bicho cria tipo um apendice msm, tlgd, um negocio no final, ent é facil de deduzir e lembrar, "o .append adiciona um item no fim da lista"... lembrar q é  com o . e q n precisa do = antes dos ()

pokemon.insert(2, "swampert")   #o .insert vai, obviamente, inserir algo. põe ele grudado na variavel de lista, n precisa do =, é grudado direto nos (), primeiro tu bota o número q o item vai ficar na fila, depois da , tu coloca o item, obviamente entre "" pq é em forma de texto. lembrando q esse n substitui, ele colo um item a mais, então o antigo numero 2 passa a ser o 3, e todos depois dele tbm pulam um numero pra tras, obviamente. no caso ali a delphox vai pra trás.

#ent, invés do 'lugia, banette, delphox' q era antes, ele vai virar 'lugia, darkrai, swampert, delphox, glaceon'. pq o darkrai substitui o banette, o '.append' adiciona o glaceon no final da lista, e o '.insert' adiciona o swampert no lugar da delphox, q faz a fila ir pra trás... tipo: *antes* (lugia0, banette1, delphox2). *agr* (lugia0, darkrai1, swampert2, delphox3, glaceon4)

# pika = input("adivinha um dos pokemon q to pensando  ")

# if pika in pokemon:
#     print("acerto mizeravi")

# else:
#     print("errado")

print(pokemon) 




###TUPLAS###

##tupla é basicamente uma lista, mas n pode substituir os itens dela#

carros = ("opala", "camaro", "mustang", "corolla", "chevete", "monza")
print(carros [2])

###é possivel fazer tanto uma lista de tuplas, quanto uma tupla de varias listas...#

lista_de_tuplas = [("zekrom", "charmander", "gengar"), ("gol", "golf", "savero")]#  isso é uma lista de tuplas!! tem duas tuplas nela#

### pra mostrar um item especifico no print, precisa primeiro dizer em qual das tuplas está, depois qual item é, são separados por numero, exatamente igual a lista (isso tbm se aplica às tuplas, n só listas... como demonstrado no exeplo dos carros). primeiro tu põe a lista q tu quer, daí especifica o numero da tupla q quer, depois o numero do item. Ex.: 'print(lista [2] [6])'
print(lista_de_tuplas [0] [1])


#####DICIONARIOS#####

##basicamente dentro de UMA unica variavel, temos mais de UMA informação, utiliza {} e os valores ficam dentro dela##

exemplos = {"pokemon":"sviny", "carro":"lancer"}    #invés de criar uma variavel pra pokemon, e outra pra carro, eu coloquei as informações dentro de apenas uma. eu posso botar no print pra aparecer tudo [só fzr da froma basica msm 'print(exemplos)'] mas eu tbm posso pegar o valor de forma individual.
print(exemplos["carro"])

##pra alterar um valor dentro é facil, vou alterar o pokemon como exemplo:
exemplos["pokemon"] = "magikarp"
print(exemplos["pokemon"]) ##dando um print só pra ver


