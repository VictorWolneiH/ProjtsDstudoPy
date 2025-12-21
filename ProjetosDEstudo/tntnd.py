#### TENTANDO CRIAR UM MINI JOGO ####
import random
import time

tentativas = [0, 1, 2, 3, 4, 5, 6]
escolha = ''

###pokemons apenas 3
swampert = {"nome": 'swampert',  'hp': 180, 'def': 13, 'ataques': {
            1: {'nome': 'Waterpulse', 'dano': 20, 'chance_erro': 1},
            2: {'nome': 'earfquake', 'dano': 50, 'chance_erro': 35},
            3: {'nome': 'mudslap', 'dano': 30, 'chance_erro': 15},
            4: {'nome': 'rockpunch', 'dano': 40, 'chance_erro': 20}}}

gengar = {"nome": 'gengar',  'hp': 110, 'def': 8, 'ataques': {
            1: {'nome': 'shadowball', 'dano': 20, 'chance_erro': 1},
            2: {'nome': 'lick', 'dano': 50, 'chance_erro': 35},
            3: {'nome': 'shadowpunch', 'dano': 30, 'chance_erro': 15},
            4: {'nome': 'curse', 'dano': 40, 'chance_erro': 20}}}

delphox = {"nome": 'delphox',  'hp': 121, 'def': 7, 'ataques': {
            1: {'nome': 'flamewheel', 'dano': 20, 'chance_erro': 1},
            2: {'nome': 'psybean', 'dano': 50, 'chance_erro': 35},
            3: {'nome': 'bite', 'dano': 30, 'chance_erro': 15},
            4: {'nome': 'poisonsticky', 'dano': 40, 'chance_erro': 20}}}

### inimigos tbm vão ser 3 no momento
sentrent = {'nome': 'sentrent', 'hp': 134, 'def': 6, 'ataques': {
            'scratch': {'dano': 25, 'chance': 1},
            'tackle': {'dano': 15, 'chance': 1}}}

zubat = {'nome': 'zubat', 'hp': 120, 'def': 10, 'ataques': {
            'bite': {'dano': 30, 'chance': 1},
            'wing attack': {'dano': 35, 'chance': 1}}}

hoothoot = {'nome': 'hoothoot', 'hp': 100, 'def': 16, 'ataques': {
            'peck': {'dano': 25, 'chance': 1},
            'echoed voice': {'dano': 45, 'chance': 1}}}

###agr eu vou criar um bidoof deus só de meme

bidoof = {'nome': 'bidoof', 'hp': 1000000, 'def': 1000000, 'ataques': {
            'apagamento existencial': {'instakill': True, 'chance': 1},
            'quebrar pokeballs': {'efeito': 'amaldiçoar'}}}

def pokebroke():
    time.sleep(1)
    print('aparentemente BIDOOF está de mal-humorl...')
    time.sleep(2)
    print('você foi amaldiçoado...')
    time.sleep(2)
    print('toda pokebola que tocares se partirá...')
    time.sleep(0.5)
    print('inclusive as que possui agora...')
    time.sleep(4)
    print('todos seus pokémon foram libertos e fugiram.')


def errouatk():
    print("seu pokemon errou o ataque... q pena")
    time.sleep(1)
    print("a vida atual do inimigo ainda é ", hp_inimigo)

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

def status_pokemon(DefP, HpPo):
    global
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

    taxa = random.randint(1, 100)

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
                print("isso não é um numero, perdeu a vez")
                time.sleep(2)
                break
            if atke == 1:
                ataque_player(20, 1)

            elif atke == 2:
                ataque_player(50, 35)

            elif atke == 3:
                ataque_player(30, 15)

            elif atke == 4:
                ataque_player(40, 20)

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