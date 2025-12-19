#### TENTANDO CRIAR UM MINI JOGO ####
import random


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
    hp_inimigo = 140
    hpS = 180
    print("swanpert entra em campo")

def gengar():
    hp_inimigo = 140
    hpG = 110
    print ("gengar entrou em campo")

def delphox():
    hp_inimigo = 140
    hpD = 121
    print("delphox entra em campo")
    atacar = input("O que fazer, lutar ou fugir?  ")
    while hp_inimigo > 0:
        if atacar == "lutar":
            print(ataquesD)
            ataque = input("escolha um dos ataques: ").lower()
            if ataque == "flamewheel":
                hp_inimigo-=33
                if hp_inimigo > 0:
                    print(hp_inimigo)
                    print("ataque super efetivo")
                else:
                    print("você venceu!!!!!!!!!!")

        elif atacar == "fugir":
            print("tentando fugir....")
            # for chances in tentativas:  ## eu to tentando fzr um sistema de chance, mas eu vi q n vai da certo assim, ent vo deixar comentado
            #     if chance
            print ("você cnseguiu fugir")
            break
        
        else:
            print("erro!!")
        if hpD < 1:
            print("little poor da delf, foi de arrasta...")
            break


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


while escolha not in mtn:
    print(meutime)
    escolha = input("escolha um de seus pokemon:  ")
    if escolha == "1":
        print("você escolheu: Delphox")
        delphox()

    elif escolha == "2":
        print("você escolheu: Swanpert")
        swanpert()

    elif escolha == "3":
        print("você escolheu: Gengar")
        gengar()

    else:
        print("esse número não corresponde à nenhum de seus pokemon...")

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

print(hpA)

while hpA > 0:
    ataqueP = random.randint(1, 100)
    if ataqueP % 2 == 0:
        hpA -= atki
        print(hpA)

############ PUTA QUE PARIU, EU DESISTO DESSA MERDA #############