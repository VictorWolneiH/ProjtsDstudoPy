#### TENTANDO CRIAR UM MINI JOGO ####
import random
import time
turno = ''
qntTurnos = random.randint(2, 6)
##efeito do bidoof
def pokebroke():     #####interface
    time.sleep(1)
    print('aparentemente BIDOOF está de mal-humor...')
    time.sleep(2)
    print('você foi amaldiçoado...')      ####isso é só a maldição do bidoof, já q ele n tem atk real
    time.sleep(2)
    print('toda pokebola que tocares se partirá...')
    time.sleep(0.5)
    print('inclusive as que possui agora...')
    time.sleep(4)
    print('todos seus pokémon foram libertos e fugiram.')
    time.sleep(3)
###vou criar as funções de efeito aqui em cima
def queima(pokemon):
    dano = 7
    pokemon.hp -= dano
    print(f'{pokemon.nome} sofreu {dano} de dano por queimadura!')

def maldicao():
    pokebroke()
    
def veneno(pokemon):
    dano = 13
    pokemon.hp -= dano
    print(f'{pokemon.nome} sofreu {dano} de dano por veneno!')

def defesa_baixa(pokemon):
    pokemon.defe -= 5
    print(f"A defesa de {pokemon.nome} caiu!")

def status_up(usuario):
    usuario.defe += 5
    usuario.hp += 10
    print(f"{usuario.nome} teve todos os status aumentados!")

### tentando criar a classe dos pokemon e dos atk deles... 
class Pokemon():
    def __init__(self, nome, hp, defe, movimentos, tipo1, tipo2 = None, raridade = 'comum'):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp
        self.defe = defe
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.movimentos = movimentos
        self.raridade = raridade
        self.efeitos = []

class Movimento(): 
    def __init__(self, nome, dano, chance_erro, tipo, efeito = None, instakill = False):
        self.nome = nome
        self.dano = dano
        self.chance_erro = chance_erro
        self.tipo = tipo
        self.efeito = efeito
        self.instakill = instakill

##listas
lista_efeitos = {'queimar': queima,
                 'veneneo': veneno}

todos_moves = {'waterpulse': Movimento('Water Pulse', 45, 100, 'agua', None, False), 
               'earfquake': Movimento('Earthquake', 80, 100, 'terra', None, False), 
               'mudslap': Movimento('Mud Slap', 30, 95, 'terra', None, False), 
               'muddy water': Movimento('Muddy Water', 65, 85, 'agua', None, False),
               'lick': Movimento('Lick', 35, 100, 'fantasma', 'paralisar', False),
               'shadowball': Movimento('ShadowBall', 75, 100, 'sombrio', None, False),
               'curse': Movimento('Curse', 20, 100, 'sombrio', 'maldito', False),
               'shadowpunch': Movimento('ShadowPunch', 55, 1000, 'sombrio', None, False),
               'bite': Movimento('Bite', 40, 100, 'sombrio', None, False),
               'mystical fire': Movimento('Mystical Fire', 70, 100, 'fogo', 'queimar', False),
               'psybean': Movimento('PsyBean', 60, 100, 'psiquico', None, False),
               'flamewheel': Movimento('FlameWheel', 55, 95, 'fogo', 'queimar', False),
               'scratch': Movimento('Scratch', 35, 100, 'normal', None, False),
               'tackle': Movimento('Tackle', 30, 100, 'normal', None, False),
               'wing attack': Movimento('Wing Attack', 45, 100, 'voador', None, False),
               'peck': Movimento('Peck', 30, 100, 'normal', None, False), 
               'echoed voice': Movimento('Echoed Voice', 40, 100, 'normal', None, False),
               'apagamento': Movimento('Apagamento Existencial', 0, 1000000, 'além', None, True),
               'pokebroke': Movimento('Quebrar Pokebolas', 0, 1000000, 'além', 'maldicao', False),
               'precipice blades': Movimento('Precipice Blades', 80, 85, 'terra', None, False),
               'hammer arm': Movimento('Hammer Arm', 60, 90, 'lutador', None, False),
               'eruption': Movimento('Eruption', 90, 100, 'fogo', None, False),
               'solar beam': Movimento('Solar Beam', 70, 100, 'planta', None, False),
               'ominous wind': Movimento('Ominous Wind', 40, 100, 'fantasma', 'status_up', False),
               'nightmare': Movimento('Nightmare', 20, 100, 'fantasma', 'maldicao', False),
               'dream eater': Movimento('Dream Eater', 65, 100, 'psiquico', None, False),
               'dark void': Movimento('Dark Void', 0, 80, 'sombrio', 'dormir', False),
               'dark pulse': Movimento('Dark Pulse', 50, 100, 'sombrio', 'recuar', False),
               'rock slide': Movimento('Rock Slide', 45, 90, 'rocha', 'recuar', False),
               'crunch': Movimento('Crunch', 55, 100, 'sombrio', 'defesa_baixa', False),
               'stone edge': Movimento('Stone Edge', 70, 80, 'rocha', None, False),
               'bone rush': Movimento('Bone Rush', 40, 90, 'terra', None, False),
               'metal claw': Movimento('Metal Claw', 35, 95, 'aço', 'ataque_sobe', False),
               'close combat': Movimento('Close Combat', 80, 100, 'lutador', 'defesa_baixa', False),
               'aura sphere': Movimento('Aura Sphere', 50, 1000, 'lutador', None, False),
               'draco meteor': Movimento('Draco Meteor', 95, 90, 'dragao', None, False),
               'extreme speed': Movimento('Extreme Speed', 45, 100, 'normal', None, False),
               'outrage': Movimento('Outrage', 75, 100, 'dragao', None, False),
               'dragon ascent': Movimento('Dragon Ascent', 85, 100, 'voador', 'defesa_baixa', False),
               'water spout': Movimento('Water Spout', 90, 100, 'agua', None, False),
               'thunder': Movimento('Thunder', 65, 70, 'eletrico', 'paralisar', False),
               'ice beam': Movimento('Ice Beam', 50, 100, 'gelo', 'congelar', False),
               'origin pulse': Movimento('Origin Pulse', 80, 85, 'agua', None, False)}

###pokemon
poke_Swampert = Pokemon('Swampert', 180, 13, {1: todos_moves['waterpulse'],
                                              2: todos_moves['earfquake'],
                                              3: todos_moves['mudslap'],
                                              4: todos_moves['muddy water']},
                                               'agua', 'terra', 'foda')

poke_Gengar = Pokemon('Gengar', 110, 12, {1: todos_moves['shadowball'],
                                         2: todos_moves['lick'],
                                         3: todos_moves['shadowpunch'],
                                         4: todos_moves['curse']},
                                         'fantasma', 'veneno', 'foda')

poke_Delphox = Pokemon('Delphox', 125, 10, {1: todos_moves['flamewheel'],
                                         2: todos_moves['bite'],
                                         3: todos_moves['psybean'],
                                         4: todos_moves['mystical fire']},
                                         'fogo', 'psiquico', 'foda')

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

poke_Groundon = Pokemon('Groundon', 300, 15, )

####listas dos times
meutime = [poke_Delphox, poke_Swampert, poke_Gengar]
inimigo = [poke_Zubat, poke_Hoothoot, poke_Sentrent, poke_Bidoof, poke_Delphox, poke_Gengar, poke_Swampert]

valor_de_raridades = {'comum': 70, 'raro': 35, 'incomum': 45, 'lendario': 10, 'mitico': 10, 'foda': 3, 'INFINITA': 1} 

### vo tenta deixar as função tudo juntinha
def efeito_feito(pokemon):
    for efeito in pokemon.efeitos:
        lista_efeitos[efeito](pokemon)

def atacamento(bola, goleiro):  ###logica
    dice = random.randint(1, 100)
    if dice > bola.chance_erro:
        return {"sucesso": False, "motivo": "falhou", "ataque_nome": bola.nome}

    if bola.instakill:
        dano_final = goleiro.hp
        goleiro.hp = 0
        return {"sucesso": True, "dano": dano_final, "instakill": True, "ataque_nome": bola.nome}

    dano_liquido = max(0, bola.dano - goleiro.defe)
    goleiro.hp -= dano_liquido

    efeito_aplicado = None
    
    if bola.efeito == 'maldicao':
        return {
        "sucesso": True,
        "ataque_nome": bola.nome,
        "fim_batalha": "pokebroke",
        "instakill": False
    }


    elif bola.efeito is not None:
        efeito_aplicado = bola.efeito
        if efeito_aplicado not in goleiro.efeitos:
            goleiro.efeitos.append(efeito_aplicado)



    return {
        "sucesso": True, 
        "dano": dano_liquido, 
        "ataque_nome": bola.nome,
        "instakill": False,
        "efeito": efeito_aplicado
    }

def atacamentoI(atacante, goleiro, resultado, move_nome):   ####interface
    time.sleep(2)
    if resultado.get("fim_batalha") == "pokebroke":
        pokebroke()
        return
    
    print(f'\n{atacante.nome} usou {move_nome}!')
    time.sleep(3)

    if not resultado["sucesso"]:
        print(f"O ataque de {atacante.nome} falhou!")
        time.sleep(2)
        return

    if resultado.get("instakill"):
        print(f"Bidoof foi bondoso com você hoje! {move_nome} APAGOU {goleiro.nome}!")
        time.sleep(2)
    else:
        print(f"Causou {resultado['dano']} de dano!")
        time.sleep(2)

    if goleiro.hp > 0:
        print(f'HP de {goleiro.nome}: {goleiro.hp}/{goleiro.hp_max}')
    else:
        print(f'--- {goleiro.nome} foi derrotado! ---')
    time.sleep(2)

def listagem(mtime):  ####interface
    time.sleep(2)
    numeroT = 0
    print('seu time:')
    for pok in mtime:
        numeroT +=1
        print(numeroT, '- ', pok.nome, '- HP', pok.hp_max)
        time.sleep(0.5)

def escolha_D_pokemon(escolha, time):  ####logica
    if escolha < 1 or escolha >len(time):
        return None
    return time[escolha - 1]

def escalacao():  ####interface
    time.sleep(1)
    while True:
        try:
            escolhendo = int(input('escolha um dos seus pokemon pelo número: '))
            escolhido = escolha_D_pokemon(escolhendo, meutime)
            time.sleep(0.5)
            if escolhido is None:
                print('esse número não corresponde à nenhum pokemon')
                continue
            escolhido = meutime[(escolhendo) - 1]
            time.sleep(1)
            return escolhido
        
        except ValueError:
            print('Digite um NÚMERO!!')
            time.sleep(1)

def escolha_a_bolaI(pokemon):  ####interface ##tbm tem a logica nele, mas é q a logica aqui n é quase nada
    time.sleep(0.5)
    print(f"\n--- Turno de {pokemon.nome} ---")
    for num, move in pokemon.movimentos.items():
        print(f"{num}: {move.nome} (Dano Base: {move.dano})")
        time.sleep(0.5)

    while True:
        try:
            escolha = int(input('Escolha o número do ataque: '))
            if escolha in pokemon.movimentos:
                return pokemon.movimentos[escolha]
            time.sleep(0.5)
            print("Número inválido! Escolha entre 1 e 4.")
        except ValueError:
            print("Por favor, digite apenas números.")
            time.sleep(0.5)
            
def inimizades(inimigos):  ####logica
    picina = []

    for mdf in inimigos:
        raro = mdf.raridade
        quantidade = valor_de_raridades[raro]
        picina += [mdf] * quantidade

    return random.choice(picina)

def bola_inimga(inimigos):  ####logica
    ataqe = list(inimigos.movimentos.values())
    return random.choice(ataqe)

def derrota_completa(time):  ####logica
    for poke in time:
        if poke.hp > 0:
            return False
    return True


perdeu = derrota_completa
inimizmo = inimizades(inimigo)
bolinha = bola_inimga

if inimizmo is not poke_Bidoof:
    print(f'um {inimizmo.nome} selvagem apareceu...')
else:
    print(f'aparentemente você rezou pouco na sua vida... {inimizmo.nome} resolveu brincar com você')
time.sleep(1)

listagem(meutime)
pokemon_escolhido = escalacao()
time.sleep(0.5)
if random.randint(1, 100) % 2 == 0:
    turno = 'player'
else:
    turno = 'inimigo'

while pokemon_escolhido.hp > 0:
    efeito_feito(pokemon_escolhido)
    if pokemon_escolhido.hp <= 0:
        print(f'\n{pokemon_escolhido.nome} não suportou {pokemon_escolhido.efeitos}')
        break
    if turno == 'player':
        sair = input('Vai lutar ou correr? ')
        time.sleep(1)
        if sair == 'correr' and (inimizmo is not poke_Bidoof):
            print('usted correo')
            break
        if inimizmo is poke_Bidoof:
            print('\nBIDOOF ri de sua mediocridade')
        ataqueE = escolha_a_bolaI(pokemon_escolhido)
        time.sleep(1)
        mostrar = atacamento(ataqueE, inimizmo)
        atacamentoI(pokemon_escolhido, inimizmo, mostrar, mostrar['ataque_nome'])
        if inimizmo.hp <= 0:
            print('meus FUCKING parabens paizão, cê ganhô')
            break
        time.sleep(1)
        turno = 'inimigo'
        
    efeito_feito(inimizmo)
    if inimizmo.hp <= 0:
        print(f'\n{inimizmo.nome} não suportou {inimizmo.efeito}')
        break
    if turno == 'inimigo':
        print(f'\nvez de {inimizmo.nome} (HP: {inimizmo.hp}/{inimizmo.hp_max})')
        time.sleep(1)
        mostrar = atacamento(bolinha(inimizmo), pokemon_escolhido)
        atacamentoI(inimizmo, pokemon_escolhido, mostrar, mostrar['ataque_nome'])

        if perdeu(meutime):
            time.sleep(3)
            ('\ntodo seu time se foi...')
            break
        if mostrar.get("fim_batalha") == "pokebroke":
            print('\nVocê nunca mais vai poder batalhar...')
            break
        turno = 'player'