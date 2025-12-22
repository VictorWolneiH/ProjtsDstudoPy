#### TENTANDO CRIAR UM MINI JOGO ####
import random
import time
turno = ''
fugir = False


###pokemons apenas 
### tentando criar a classe dos pokemon e dos atk deles... acho q vai ser complicado pra krl
class Pokemon():
    def __init__(self, nome, hp, defe, movimentos, tipo1, tipo2 = None, raridade = 'comum'):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp
        self.defe = defe
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.moves = movimentos
        self.raridade = raridade

class Movimento(): 
    def __init__(self, nome, dano, chance_erro, tipo, efeito = None, instakill = False):
        self.nome = nome
        self.dano = dano
        self.chance_erro = chance_erro
        self.tipo = tipo
        self.efeito = efeito
        self.instakill = instakill
        
todos_moves = {'waterpulse': Movimento('waterpulse', 20, 100, 'agua', None, False), 
               'earfquake': Movimento('earfquake', 50, 35, 'terra', None, False), 
               'mudslap': Movimento('mudslap', 30, 15, 'terra', None, False), 
               'muddy water': Movimento('Muddy Water', 40, 20, 'agua', None, False),
               'lick': Movimento('Lick', 35, 90, 'fantasma', None, False),
               'shadowball': Movimento('ShadowBall', 50, 40, 'sombrio', None, False),
               'curse': Movimento('Curse', 10, 100, 'sombrio', None, False),
               'shadowpunch': Movimento('ShadowPunch', 35, 60, 'sombrio', None, False),
               'bite': Movimento('Bite', 20, 70, 'sombrio', None, False),
               'mystical fire': Movimento('Mystical Fire', 60, 60, 'fogo', None, False),
               'psybean': Movimento('PsyBean', 45, 55, 'psiquico', None, False),
               'flamewheel': Movimento('FlameWheel', 40, 75, 'fogo', None, False),
               'scratch': Movimento('Scratch', 25, 100, 'normal', None, False),
               'tackle': Movimento('Tackle', 15, 100, 'normal', None, False),
               'wing attack': Movimento('Wing Attack', 35, 100, 'voador', None, False),
               'peck': Movimento('Peck', 25, 100, 'normal', None, False), 
               'echoed voice': Movimento('Echoed Voice', 45, 90, 'normal', None, False),
               'apagamento': Movimento('Apagamento Existencial', 0, 1000000, 'além', None, True),
               'pokebroke': Movimento('Quebrar Pokebolas', 0, 1000000, 'além', 'maldição', False)}

poke_Swampert = Pokemon('Swampert', 180, 20, {1: todos_moves['waterpulse'],
                                              2: todos_moves['earfquake'],
                                              3: todos_moves['mudslap'],
                                              4: todos_moves['muddy water']},
                                               'agua', 'terra', 'foda')

poke_Gegar = Pokemon('Gengar', 110, 12, {1: todos_moves['shadowball'],
                                         2: todos_moves['lick'],
                                         3: todos_moves['shadowpunch'],
                                         4: todos_moves['curse']},
                                         'fantasma', 'veneno', 'foda')

poke_Delphox = Pokemon('Delphox', 125, 10, {1: todos_moves['flamewheel'],
                                         2: todos_moves['bite'],
                                         3: todos_moves['psybean'],
                                         4: todos_moves['mystical fire']},
                                         'fogo', 'psiquico', 'foda')

### inimigos tbm vão ser 3 no momento
poke_Sentrent = Pokemon('Sentrent', 134, 6, {1: todos_moves['scratch'],
                                             2: todos_moves['tackle']},
                                             'normal', None, 'comum')

poke_Zubat = Pokemon('Zubat', 120, 10, {1: todos_moves['bite'],
                                        2: todos_moves['wing attack']},
                                        'voador', 'normal', 'comum')

poke_Hoothoot = Pokemon('HootHoot', 100, 15, {1: todos_moves['peck'],
                                              2: todos_moves['echoed voice']},
                                              'normal', 'voador', 'comum')

poke_Bidoof = Pokemon('BIDOOF', 1000000, 1000000, {1: todos_moves['apagamento'],
                                                   2: todos_moves['pokebroke']},
                                                   'além', None, 'INFINITA')                                        

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