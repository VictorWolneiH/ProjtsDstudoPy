### LOOP... O PROPRIO NOME JÁ DIZ, É UM CODIGO Q FICA EM LOOP ATÉ ALGO PARAR ELE ## 

##nesse exemplo criamos um contador q vale 10, ent while(enquanto, pros q n entende english) vai ser o nosso "looper". basicamente ele ta falando 'enquanto tal coisa acontecer, manteha o codigo rodando'

# contador = 10 
# while contador >= 1:  #nesse caso ele ta falando pro codigo rodar enquanto o contador for 1 ou mais.
#     print(f"contagem atual: {contador}")  # aqui ta rodando o print mostrando em quanto o contador tá
#     contador-=1  # e aqui ele tá tirando 1 do contador cada vez q o codigo roda, ent vai chegar um momento q o contador vai ser menor q 1, daí ele vai parar de rodar o codigo XD



# ###### SEGUNDO EXEMPLO ######

# pokemon = "delphox" # aqui eu defini um bagulho pra adivinhar
# tenta_adivinhar = ''    # n entendi direito pq o professor fez assim, mas acho q é pra criar a variavel, mas deixar ela com nada definido dentro, pra fzr isso mais tarde, depois eu pergunto pro chatgpt sobre...

# while pokemon != tenta_adivinhar: # o != significa diferente, ent isso é tipo: enquanto a tentativa for diferente...
#     tenta_adivinhar = input("qual pokemon eu to pensando? ") # aqui diz oq é feito, ...aparece a "pergunta"
#     if tenta_adivinhar != pokemon: # aqui praticamente repete, mas com outra condião, aqui ele avisa q ta errado
#         print("errado, tenta dnovo ")
#     else:
#         print("MY FUCKING PARABENS PARCERO")   #aqui é quando ta certo

#     ### esse bagulho ta basicamente assim: 'enquanto a tentativa não der certo (vulgo, n acertar o pokemon)...', daí faz os baguho q manda, nesse caso. "enquanto n acertar, faz a pergunta, SE a resposta n estiver certa, mostra a mensagem de errado e fica no loop, CASO CONTRARIO, diz q ta certo e acaba o loop"



#####LOOOP FOR######

## PRIMERO EXEMPLO 

time_pokemon = ["misdreavus", "swanpert", "gardevoir", "slowbro", "halucha", "volcarona"] #definindo os item da lista
tirar='' #variavel indefinida pra fzr o loop do while
def pikomon():   ####AQUI EU TO FZND UMA FUNÇÃO##
    for poke in time_pokemon: # a função é tipo uma variavel, mas ela pode meioq guardar qlqr coisa, como esse codigozin do FOR
        print(poke) ### ent o loop for é pra listas, por isso eu dedini uma lista antes, ele basicamente roda a lista. tipo aqui ta escrito "pra cada poke na lista time_pokemon mostre os poke"... poke (pode ser qualquer coisa escrita ali) é a variavel q o for precisa, é basicamente o nome dos itens q tão na lista. e o print é o mostrar. basicamente isso "pra cada item na lista: mostras os itens" daí ele mostra todos os itens... um exemplo mais realista aqui "uma cambada de vagabundo" cambada seria a lista, vagabundo seria os itens, cada pessoa desse grupo equivale a um item na lista, esse exemplo é só pra mostrar q o nome do bagulho n importa mt

pikomon() #aqui eu to ativando a função q foi definida

while time_pokemon:   ##aqui é o loop anterior, a diferença ta na condição dele, aqui eu n to comparado os bagulho diretamente, mas sim o estado da lista... como a lista n foi alterada ainda ela é true, verdadeira, vulgo tá normal... ent quando ela ficar sem o itens, ela vai ta vazia, ent vai ser false, e já q o codigo é "ENQUANTO TIVER COISA NA LISTA..." ent quando ela esvaziar o loop para

    tirar = input ("escolha um pokemon pra remover:  ") #variavel normal de input. eu gosto de descrever as variaveis como papeis, ela vale oq ta escrito nela. o input meio q cria um tipo de pergunta, ent oq tu responder vai ser escrito no papel... tipo chegar alguem em ti e te entregar um papel, ele te pergunta qualquer coisa "qual o melhor jogador de futebol de todos os tempos?" daí tu escreve ali no papel q é o "meia de demolidor"... nessa analogia: o input pede "tira um pokemon aí fi", daí tu escreve no 'tirar' o nome doq tu quiser, lembrando q tu pode escrever qualquer coisa, ent o codigo temq tá preparado pra caso tu escreva alguma bosta nada a ve... e essa preparação nós vê abaixo

    if tirar in time_pokemon:  # aqui tá: se oq tiver escrito no 'tirar' estiver na lista...'  daí acontece o resto
        time_pokemon.remove(tirar) #vai remover o nome q tu falou, aqui ta escrito algo tipo "remova o nome q foi escrito em 'tirar' da lista"
        pikomon() # antes eu tava mostrando a lista no fim do codigo, mas achei meio ruim aparecendo toda hora, msm q n tivesse mudado nada, ent resolvi colocar aqui, assim ele só vai abrir a lista dnovo se eu mudar ela

    else:
        print("N TEM ESSE POKEMON NA LISTA") #aqui é um else (caso contrario, ou se não... pros menos afortunados da lingua inglesa) 

        ###esse if e else é assim "se tal coisa acontecer, faça isso, se não acontecer, faça aquilo" no meu codigo ele funciona assim: SE o nome escrito em 'tirar' é igual algum nome da lista, ent remova o nome da lista, SE NÃO for igual, avise q n é igual e n faça mais nada


    # pikomon() #ativando a função dnovo pra ver como tá a lista agora.  eu botei essa função no if, mas deixei comentado aqui pra ver o baguho



####### no fim esse, q era pra ser um exemplo de for loop, acabu virando uma brincadeira um pouco maior, quase n apareceu o for loop no exemplo. ent vo fzr oto


# lista= ["nome1", "nome2", "nome3", "nome4"] #criando uma lista

# for nomes in lista: # pra cada nome na lista, mostre os nomes
#     print(nomes)


# ########### agr um exemplo com numeros 

# listn= [2, 3, 5, 2, 7, 6, 4, 5, 6, 8, 2, 4, 9]

# for numeros in listn:
#     print(numeros)