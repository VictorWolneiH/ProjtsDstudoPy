#### TENTANDO CRIAR UM MINI JOGO ####
import random
import time
turno = ''
fugir = False


###pokemons apenas 

swampert = {"nome": 'swampert',  'hp': 180, 'def': 13, 'ataques': {
            1: {'nome': 'Waterpulse', 'dano': 20, 'chance_erro': 100},
            2: {'nome': 'earfquake', 'dano': 50, 'chance_erro': 35},
            3: {'nome': 'mudslap', 'dano': 30, 'chance_erro': 15},
            4: {'nome': 'muddy water', 'dano': 40, 'chance_erro': 20}}}

gengar = {"nome": 'gengar',  'hp': 110, 'def': 8, 'ataques': {
            1: {'nome': 'shadowball', 'dano': 20, 'chance_erro': 1},
            2: {'nome': 'lick', 'dano': 50, 'chance_erro': 35},
            3: {'nome': 'shadowpunch', 'dano': 30, 'chance_erro': 15},
            4: {'nome': 'curse', 'dano': 40, 'chance_erro': 20}}}

delphox = {"nome": 'delphox',  'hp': 121, 'def': 7, 'ataques': {
            1: {'nome': 'flamewheel', 'dano': 20, 'chance_erro': 1},
            2: {'nome': 'psybean', 'dano': 50, 'chance_erro': 35},
            3: {'nome': 'bite', 'dano': 30, 'chance_erro': 15},
            4: {'nome': 'mystical fire', 'dano': 40, 'chance_erro': 20}}}

### inimigos tbm vão ser 3 no momento
sentrent = {'nome': 'sentrent', 'hp': 134, 'def': 6, 'peso': 33, 'ataques': {
            1: {'nome': 'scratch', 'dano': 25, 'chance_erro': 1},
            2: {'nome': 'tackle', 'dano': 15, 'chance_erro': 1}}}

zubat = {'nome': 'zubat', 'hp': 120, 'def': 10, 'peso': 33, 'ataques': {
            1: {'nome': 'bite', 'dano': 30, 'chance_erro': 1},
            2: {'nome': 'wing attack', 'dano': 35, 'chance_erro': 1}}}

hoothoot = {'nome': 'hoothoot', 'hp': 100, 'def': 16, 'peso': 33, 'ataques': {
            1: {'nome': 'peck', 'dano': 25, 'chance_erro': 1},
            2: {'nome': 'echoed voice', 'dano': 45, 'chance_erro': 1}}}

###agr eu vou criar um bidoof deus só de meme
bidoof = {'nome': 'bidoof', 'hp': 1000000, 'def': 1000000, 'peso': 1, 'ataques': {
            1: {'nome': 'apagamento existencial', 'instakill': True, 'chance_erro': 1},
            2: {'nome': 'quebrar pokeballs', 'efeito': 'amaldiçoar', 'chance_erro': 1}}}

####listas dos times
meutime = [delphox, swampert, gengar]
inimigo = [zubat, hoothoot, sentrent, bidoof]

### vo tenta deixar as função tudo juntinha
def pokebroke():
    time.sleep(1)
    print('aparentemente BIDOOF está de mal-humorl...')
    time.sleep(2)
    print('você foi amaldiçoado...')      ####isso é só a maldição do bidoof, já q ele n tem atk real
    time.sleep(2)
    print('toda pokebola que tocares se partirá...')
    time.sleep(0.5)
    print('inclusive as que possui agora...')
    time.sleep(4)
    print('todos seus pokémon foram libertos e fugiram.')

def atacamento(atacante, bola, goleiro):
    ataque = atacante['ataques'][bola]

    nome_do_ataque = ataque['nome']
    dano = ataque['dano']
    chance_erro = ataque['chance_erro']

    print(f'{atacante['nome']} usou {nome_do_ataque}')

    dice = random.randint(1, 100)

    if dice > chance_erro:
        print("o ataque falhou")
        return 
    
    dano_liquido = dano - goleiro['def']
    if dano_liquido < 0:
        dano_liquido = 0

    goleiro['hp'] -= dano_liquido

    print(f'{nome_do_ataque} causou {dano_liquido} de dano')

    if goleiro['hp'] > 0:
        print(f'HP de {goleiro['nome']}: {goleiro['hp']}')
    else:
        print(f'{goleiro['nome']} foi derrotado')

def bolas(pokemon):
    print(f'ataques de {pokemon['nome']}: ')
    for numero, atake in pokemon['ataques'].items():
        print(f'{numero} - {atake['nome']}')
    return pokemon

def listagem(time):
    numeroT = 0
    print('seu time:')
    for pok in time:
        numeroT +=1
        print(numeroT, '- ', pok['nome'], '- HP', pok['hp'])

def escolha_D_pokemon(escolha, time):
    if escolha < 1 or escolha >len(time):
        return None
    return time[escolha - 1]

def escalacao():
    while True:
        try:
            escolhendo = int(input('escolha um dos seus pokemon pelo número: '))
            escolhido = escolha_D_pokemon(escolhendo, meutime)

            if escolhido is None:
                print('esse número não corresponde à nenhum pokemon')
                continue
            escolhido = meutime[(escolhendo) - 1]

            return escolhido
        
        except ValueError:
            print('Digite um NÚMERO!!')

def escolha_a_bola(pokemon):
    while True:
        try:
            ataque = int(input('escolha um ataque pelo número: '))
            if ataque in pokemon['ataques']:
                return ataque
            else:
                print("digite um numero valido")

        except ValueError:
            print("digite um número, pls")
            
def inimizades(inimigos):
    picina = []

    for mdf in inimigos:
        picina += [mdf] * mdf['peso']

    return random.choice(picina)

def bola_inimga(inimigos):
    ataqe = list(inimigos['ataques'].keys())
    atkI = random.choice(ataqe)
    return atkI

def derrota_completa(time):
    for poke in time:
        if poke['hp'] > 0:
            return False
    return True


perdeu = derrota_completa
inimizmo = inimizades(inimigo)
bolinha = bola_inimga

print('um inimigo apareceu...')
time.sleep(1)

listagem(meutime)
pokemon_escolhido = escalacao()
time.sleep(2)
if random.randint(1, 100) % 2 == 0:
    turno = 'player'
else:
    turno = 'inimigo'

while True:
    if turno == 'player':
        sair = input('qé metê o pé?? ')
        if sair == 'sim':
            break
        ataqueE = escolha_a_bola(bolas(pokemon_escolhido))
        atacamento(pokemon_escolhido, ataqueE, inimizmo)
        if inimizmo['hp'] <= 0:
            break
        time.sleep(2)
        turno = 'inimigo'

    if turno == 'inimigo':
        atacamento(inimizmo, bolinha(inimizmo), pokemon_escolhido)
        if perdeu(meutime):
            break
        turno = 'player'