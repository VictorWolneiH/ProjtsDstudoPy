#### TENTANDO CRIAR UM MINI JOGO ####
import random
import time

tentativas = [0, 1, 2, 3, 4, 5, 6]
escolha = ''

## vidas
hp_inimigo = 140

hpD = 121
hpS = 180
hpG = 110

###pokemons apenas 3

delphx = ''
ataquesD = ["FlameWheel", "PoisonSticky", "PsyBean", "bite"]

swanpet = ''
ataqueS = ["WaterPulse", "EarthQuake", "MudSlap", "RockPunch"]

genga = ''
ataqueG = ["ShadowBall", "Lick", "ShadowPunch", "Curse"]

def swanpert():
    print("swanpert entra em campo")
    time.sleep(2)

def gengar():
    print ("gengar entrou em campo")
    time.sleep(2)

def delphox():
    print("delphox entra em campo")
    time.sleep(2)
    # atacar = input("O que fazer, lutar ou fugir?  ")
    # while hp_inimigo > 0:
    #     if atacar == "lutar":
    #         print(ataquesD)
    #         ataque = input("escolha um dos ataques: ").lower()
    #         if ataque == "flamewheel":
    #             hp_inimigo-=33
    #             if hp_inimigo > 0:
    #                 print(hp_inimigo)
    #                 print("ataque super efetivo")
    #             else:
    #                 print("você venceu!!!!!!!!!!")

    #     elif atacar == "fugir":
    #         print("tentando fugir....")
    #         # for chances in tentativas:  ## eu to tentando fzr um sistema de chance, mas eu vi q n vai da certo assim, ent vo deixar comentado
    #         #     if chance
    #         print ("você cnseguiu fugir")
    #         break
        
    #     else:
    #         print("erro!!")
    #     if hpD < 1:
    #         print("little poor da delf, foi de arrasta...")
    #         break

def errouatk():
    print("seu pokemon errou o ataque... q pena")
    time.sleep(1)
    print("a vida atual do inimigo é ", hp_inimigo)

def atakV():
    if escolha == "1":
        print(ataquesD)

    elif escolha == "2":
        print(ataqueS)

    elif escolha == "3":
        print(ataqueG)



meutime = ["Delphox", "Swanpert", "Gengar"]
mtn = ["1", "2", "3"]
print("um inimigo apareceu...")

time.sleep(2)
while escolha not in mtn:
    print(meutime)
    escolha = input("escolha um de seus pokemon:  ")
    if escolha == "1":
        print("você escolheu: Delphox")
        time.sleep(1)
        delphox()

    elif escolha == "2":
        print("você escolheu: Swanpert")
        time.sleep(1)
        swanpert()

    elif escolha == "3":
        print("você escolheu: Gengar")
        time.sleep(1)
        gengar()

    else:
        print("esse número não corresponde à nenhum de seus pokemon...")
        time.sleep(2)

defe = ''
hpA = ''


if escolha == "1":
    defe = 7
    hpA = hpD

elif escolha == "2":
    defe = 13
    hpA = hpS

elif escolha == "3":
    defe = 8
    hpA = hpG

else:
    defe = 0
    hpA = 0

ataqueI = random.randint(20, 40)

defB = random.randint(2, 8) 

defA = defB + defe

atki = ataqueI - defA 

Lista_d_atks = [1, 2, 3, 4]
atke = ''
atakado = 0

print("a vida atual do seu pokemon é ", hpA)
time.sleep(1)

print("a vida atual do inimigo é ", hp_inimigo)
time.sleep(1)

ataqueP = random.randint(1, 100)


def ataque_player(dano, chance):
    global hp_inimigo
    global atakado

    taxa = random.randint(1,10)

    if taxa <= chance:
        errouatk()
        atakado = 1
        time.sleep(2)
    else:
        print("seu pokemon ataca")
        time.sleep(0.5)
        hp_inimigo -= dano
        time.sleep(2)

        if hp_inimigo > 0:
            print("a vida atual do inimigo é ", hp_inimigo)
        else:
            print("o HP do inimigo chegou à 0")
        atakado = 1
        time.sleep(1)



if ataqueP % 2 == 0:
    ataqueP = "player"
else:
    ataqueP = "inimigo"
    
while hpA > 0 and hp_inimigo > 0:
    if ataqueP == "player":
        print("é sua vez")
        atakV()
        atakado = 0
        time.sleep(1)
        
        while atakado == 0:
            atakado = 0
            # chance = random.randint(1, 11)

            try:
                atke = int(input("escolha um atk, pelo numero: "))
            except ValueError:
                print("isso não é um numero")
                time.sleep(2)
                break
            if atke == 1:
                ataque_player(20, 1)

            elif atke == 2:
                if chance <= 2:
                    errouatk()
                    atakado = 1
                    time.sleep(2)
                else:
                    print("seu pokemon ataca")
                    time.sleep(0.5)
                    hp_inimigo -= 50
                    time.sleep(2)

                    if hp_inimigo > 0:
                        print("a vida atual do inimigo é ", hp_inimigo)
                    else:
                        print("o HP do inimigo chegou à 0")
                    atakado = 1
                    time.sleep(1)

            elif atke == 3:
                if chance <= 2:
                    errouatk()
                    atakado = 1
                    time.sleep(2)
                else:
                    print("seu pokemon ataca")
                    time.sleep(0.5)
                    hp_inimigo -= 42
                    time.sleep(2)

                    if hp_inimigo > 0:
                        print("a vida atual do inimigo é ", hp_inimigo)
                    else:
                        print("o HP do inimigo chegou à 0")
                    atakado = 1
                    time.sleep(1)

            elif atke == 4:
                if chance <= 2:
                    errouatk()
                    atakado = 1
                    time.sleep(2)
                else:
                    print("seu pokemon ataca")
                    time.sleep(0.5)
                    hp_inimigo -= 33
                    time.sleep(2)

                    if hp_inimigo > 0:
                        print("a vida atual do inimigo é ", hp_inimigo)
                    else:
                        print("o HP do inimigo chegou à 0")
                    atakado = 1
                    time.sleep(1)

            elif atke > 4:
                print("esse atk n tá na lista")
                time.sleep(2)

        ataqueP = "inimigo"
        time.sleep(1)

    elif ataqueP == "inimigo":
        chancei = random.randint(1, 11)

        if chancei > 2:
            print("o inimigo ataca...")
            time.sleep(2)
            hpA -= atki

            if hpA > 0:
                print("a vida atual do seu pokemon é ", hpA)
            else:
                print("o HP do seu pokemon chegou à 0")

        else:
            print("o inimigo errou o atk... q sorte")

        ataqueP = "player"
        time.sleep(2)

if hpA <= 0:
    print("voce deixou seu pokemon morrer, coitadinho")

if hp_inimigo <= 0:
    print("parabens, seu pokemon derrotou o inimigo")

time.sleep(3)

############ PUTA QUE PARIU, EU DESISTO DESSA MERDA #############

########## na vdd acho q agr deu certo hehe XD XD XD XD