#### BEM-VINDO AO FORTUNA DESSOFT - BY SAMUEL JABES E VINICIUS RODRIGUES ####

from random import randint
from random import choice
from os import system

def transforma_base(lista_questoes):
    questoes_por_nivel = {}
    for questao in lista_questoes:
        if questao['nivel'] not in questoes_por_nivel:
            questoes_por_nivel[questao['nivel']] = [questao]
        else:
            questoes_por_nivel[questao['nivel']].append(questao)
    return questoes_por_nivel

def valida_questao(questao):
    problemas = {}

    # Checando se as chaves exigidas estão na questão
    chaves_necessarias = ['titulo', 'nivel', 'opcoes', 'correta']
    for chave in chaves_necessarias:
        if chave not in questao:
            problemas[chave] = 'nao_encontrado'

    # Checando se o número de chaves está correto
    if len(questao.keys()) != 4:
        problemas['outro'] = 'numero_chaves_invalido'

    # Checa se o título existe e não está vazio ou em branco
    if 'titulo' in questao.keys() and questao['titulo'].strip() == '':
        problemas['titulo'] = 'vazio'

    # Checa se há a chave 'nível' e se ela contém um nível válido
    niveis_possiveis = set(['facil', 'medio', 'dificil'])
    if ('nivel' in questao.keys()) and (questao['nivel'] not in niveis_possiveis):
        problemas['nivel'] = 'valor_errado'

    letras_opcoes = ['A', 'B', 'C', 'D']
    if 'opcoes' in questao.keys():
        if len(questao['opcoes'].keys()) != 4:
            # Checa se há a chave 'opcoes' e se seu valor contém quatro chaves
            problemas['opcoes'] = 'tamanho_invalido'
        else:
            letras_estao = True
            for letra in letras_opcoes:
                if letra not in questao['opcoes']: letras_estao = False

            if letras_estao:
                for letra in letras_opcoes:
                    if questao['opcoes'][letra].strip() == '':
                        if 'opcoes' not in problemas:
                            problemas['opcoes'] = {f'{letra}':'vazia'}
                        else:
                            problemas['opcoes'][letra] = 'vazia'
            else:
                problemas['opcoes'] = 'chave_invalida_ou_nao_encontrada'

    # Checa se há a chave 'correta' e se existe uma opção válida nela
    if ('correta' in questao.keys()) and (questao['correta'] not in letras_opcoes):
        problemas['correta'] = 'valor_errado'

    return problemas

def valida_questoes(lista_questoes):
    lista_problemas = []
    for questao in lista_questoes:
        problemas = valida_questao(questao)
        lista_problemas.append(problemas)
    return lista_problemas

def sorteia_questao(questoes_por_nivel, nivel):
    numero_questao = randint(0, len(questoes_por_nivel[nivel])-1)
    questao_sorteada = questoes_por_nivel[nivel][numero_questao]
    return questao_sorteada

def sorteia_questao_inedita(questoes_por_nivel, nivel, questoes_sorteadas):
    questao_inedita = sorteia_questao(questoes_por_nivel, nivel)
    while questao_inedita in questoes_sorteadas:
        questao_inedita = sorteia_questao(questoes_por_nivel, nivel)
    questoes_sorteadas.append(questao_inedita)
    return questao_inedita

def questao_para_texto(questao, numero):
    cabecalho = f'----------------------------------------\nQUESTAO {numero}\n\n{questao["titulo"]}\n\nRESPOSTAS:\n'

    opcoes = ''
    for letra in questao['opcoes'].keys():
        opcoes += f'{letra}: {questao["opcoes"][letra]}\n'
    questao_formatada = cabecalho+opcoes
    
    return questao_formatada

def gera_ajuda(questao):
    opcoes = ['A', 'B', 'C', 'D']
    dicas_sorteadas = []
    numero_dicas = randint(1, 2)
    while numero_dicas != 0:
        opcao_sorteada = opcoes[randint(0, len(opcoes)-1)]
        if opcao_sorteada != questao['correta'] and opcao_sorteada not in dicas_sorteadas:
            dicas_sorteadas.append(questao['opcoes'][opcao_sorteada])
            numero_dicas -= 1
    
    if len(dicas_sorteadas) == 1:
        return f"DICA:\nOpções certamente erradas: {dicas_sorteadas[0]}"
    elif len(dicas_sorteadas) == 2:
        return f"DICA:\nOpções certamente erradas: {dicas_sorteadas[0]} | {dicas_sorteadas[1]}"

# Aqui começam funções auxiliares

def manual_do_jogo(nome):
    print(f'''
========================= BEM-VINDO AO FORTUNA DESSOFT!!! =========================
\n
{nome}, você receberá uma pergunta a cada rodada e deverá responder qual o item correto.
A cada resposta correta, seu prêmio aumenta, mas se errar, você perde tudo!\n

Você poderá solicitar ajuda dos universitários até 2 vezes digitando "ajuda".
Você poderá pular até 3 questões digitando "pula".
Se você achar que não sabe a resposta, pode escolher sair com o que conseguiu digitando "parar".\n
===================================================================================\n
Prepara o coração que o desafio vai começar!
''')
    input('Aperte ENTER para começar o jogo...')
    pass

def print_green(texto):
    print("\033[92m" + texto + "\033[00m")
    pass

def print_red(texto):
    print("\033[91m" + texto + "\033[00m")
    pass

#### AQUI COMEÇA NOSSO JOGO ####

system("cls")
nome = input("Informe o seu nome: ")
manual_do_jogo(nome)

lista_premios = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
ajudas_disponiveis = 2
pulos_disponiveis = 3
numero_questao = 0
questoes_acertadas = 0
fim_do_jogo = False

lista_questoes = [
    {'titulo': 'Qual o resultado da operação 57 + 32?',
    'nivel': 'facil',
    'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
    'correta': 'C'},

    {'titulo': 'Termo econômico usado para designar o aumento generalizado de preços de bens e serviços',
    'nivel': 'facil',
    'opcoes': {'A': 'Lei da oferta e demanda', 'B': 'Inflação', 'C': 'Taxa de juros', 'D': 'PIB'},
    'correta': 'B'},

    {'titulo': 'Qual o planeta do sistema solar mais distante da Terra?',
    'nivel': 'facil',
    'opcoes': {'A': 'Urano', 'B': 'Planeta X', 'C': 'Plutão', 'D': 'Netuno'},
    'correta': 'D'},

    {'titulo': 'Qual a capital do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
    'correta': 'A'},

    {'titulo': 'Quando é o feriado da Independência do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
    'correta': 'C'},

    {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
    'nivel': 'facil',
    'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
    'correta': 'B'},

    {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
    'nivel': 'facil',
    'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
    'correta': 'D'},

    {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
    'nivel': 'facil',
    'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
    'correta': 'A'},

    {'titulo': 'Qual destas não é uma fruta?',
    'nivel': 'facil',
    'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
    'correta': 'B'},

    {'titulo': 'Como se move o Rei no tabuleiro de xadrez?',
    'nivel': 'facil',
    'opcoes': {'A': 'Apenas uma casa mas para qualquer direção', 'B': 'Apenas uma casa e sempre para frente', 'C': 'Apenas uma casa mas nas diagonais', 'D': 'Qualquer número de casas em qualquer direção'},
    'correta': 'A'},

    {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
    'nivel': 'facil',
    'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
    'correta': 'B'},
    
    {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
    'nivel': 'facil',
    'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
    'correta': 'C'},

    {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
    'nivel': 'facil',
    'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
    'correta': 'D'},

    {'titulo': 'Qual destas não é uma linguagem de programação?',
    'nivel': 'facil',
    'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
    'correta': 'A'},

    {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
    'correta': 'C'},

    {'titulo': 'Quantos estados o Brasil possui?',
    'nivel': 'facil',
    'opcoes': {'A': '13', 'B': '22', 'C': '26', 'D': '27'},
    'correta': 'C'},
    
    {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
    'nivel': 'medio',
    'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
    'correta': 'B'},

    {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
    'nivel': 'medio',
    'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
    'correta': 'C'},

    {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
    'nivel': 'medio',
    'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
    'correta': 'D'},

    {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
    'nivel': 'medio',
    'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
    'correta': 'A'},

    {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
    'nivel': 'medio',
    'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
    'correta': 'C'},

    {'titulo': 'Qual destes números é primo?',
    'nivel': 'medio',
    'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
    'correta': 'D'},

    {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
    'nivel': 'medio',
    'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
    'correta': 'A'},

    {'titulo': 'Como faço para chamar o SAMU?',
    'nivel': 'medio',
    'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
    'correta': 'B'},

    {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
    'nivel': 'medio',
    'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
    'correta': 'D'},

    {'titulo': 'Qual a pessoa mais seguida no Instagram?',
    'nivel': 'medio',
    'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
    'correta': 'A'},

    {'titulo': 'Qual a combinação mais poderosa no poker?',
    'nivel': 'medio',
    'opcoes': {'A': 'Quadra', 'B': 'Full House', 'C': 'Royal Straight Flush', 'D': 'Bingo'},
    'correta': 'C'},

    {'titulo': 'Qual o mascote da seleção brasileira de futebol masculino?',
    'nivel': 'medio',
    'opcoes': {'A': 'Fuleco', 'B': 'Tatu-bola', 'C': 'Zizito', 'D': 'Canarinho'},
    'correta': 'D'},

    {'titulo': 'Qual dessas NÃO é uma linguagem de programação de alto nível?',
    'nivel': 'medio',
    'opcoes': {'A': 'Python', 'B': 'Assembly', 'C': 'Kotlin', 'D': 'C++'},
    'correta': 'B'},

    {'titulo': 'O que é um número racional?',
    'nivel': 'medio',
    'opcoes': {'A': 'Um número que é divisível somente por um e por ele mesmo', 'B': 'É o quadrado de um número irracional', 'C': 'É um número da forma p/q onde p e q são números naturais', 'D': 'É um número da forma a + b*i em que i é raiz de -1'},
    'correta': 'C'},

    {'titulo': 'Em que ano ocorreu a queda do muro de Berlim?',
    'nivel': 'medio',
    'opcoes': {'A': '1989', 'B': '1991', 'C': '1964', 'D': '1984'},
    'correta': 'A'},

    {'titulo': 'Qual desses países não possui uma bandeira quadrada?',
    'nivel': 'medio',
    'opcoes': {'A': 'Togo', 'B': 'Nepal', 'C': 'Vietnã', 'D': 'Guam'},
    'correta': 'B'},

    {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
    'correta': 'A'},

    {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
    'nivel': 'dificil',
    'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
    'correta': 'D'},

    {'titulo': 'Quem é Oxóssi?!',
    'nivel': 'dificil',
    'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
    'correta': 'C'},

    {'titulo': 'Qual a altura do Cristo Redentor?',
    'nivel': 'dificil',
    'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
    'correta': 'B'},

    {'titulo': 'Em que ano faleceu Charles Babbage?',
    'nivel': 'dificil',
    'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
    'correta': 'A'},

    {'titulo': 'Einstein foi Nobel de física em qual ano?',
    'nivel': 'dificil',
    'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
    'correta': 'D'},

    {'titulo': 'Qual o número atômico do nitrogênio?',
    'nivel': 'dificil',
    'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
    'correta': 'B'},

    {'titulo': 'Qual o ponto de fusão do nitrogênio?',
    'nivel': 'dificil',
    'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
    'correta': 'C'},
    
    {'titulo': 'Quantos gols Pelé fez oficialmente?',
    'nivel': 'dificil',
    'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
    'correta': 'B'},

    {'titulo': 'O que é Necrose?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
    'correta': 'D'},

    {'titulo': 'Qual o nome da lei que estabelece a relação entre a velocidade de afastamento de uma galáxia e sua distância?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Lei de Eddington', 'B': 'Lei de Hubble', 'C': 'Lei de Hawking', 'D': 'Lei de Swan Leavitt'},
    'correta': 'B'},

    {'titulo': 'Quem era o treinador da seleção brasileira na conquista do tetra da Copa do Mundo da FIFA?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Carlos Alberto Parreira', 'B': 'Luiz Felipe Scolari, o Felipão', 'C': 'Mario Jorge Lobo Zagallo', 'D': 'Carlos Caetano Bledorn Verri, o Dunga'},
    'correta': 'A'},

    {'titulo': '__________ é o nome dado a quando o jogador de xadrez é forçado a uma situação de desvantagem por sua obrigação de fazer um movimento',
    'nivel': 'dificil',
    'opcoes': {'A': 'En Passant', 'B': 'Zwischenzug', 'C': 'Xeque-Mate', 'D': 'Zugzwang'},
    'correta': 'D'}
]
questoes_por_nivel = transforma_base(lista_questoes)

questoes_sorteadas = []
classifica_nivel = {
    0: 'facil', 1: 'facil', 2: 'facil',
    3: 'medio', 4: 'medio', 5: 'medio',
    6: choice(['medio', 'dificil']), 
    7: 'dificil', 8: 'dificil', 9: 'dificil'
}

while not fim_do_jogo:
    questao_atual = sorteia_questao_inedita(questoes_por_nivel, classifica_nivel[questoes_acertadas], questoes_sorteadas)
    numero_questao += 1
    fim_da_questao = False
    usou_ajuda = False

    while not fim_da_questao and not fim_do_jogo:
        print(questao_para_texto(questao_atual, numero_questao))
        resposta = input("Sua resposta: ")

        if resposta == questao_atual['correta']:
            questoes_acertadas += 1
            print_green(f"VOCÊ ACERTOU! O seu prêmio atual é R$ {lista_premios[questoes_acertadas]:05.2f}")
            fim_da_questao = True
        elif resposta == 'pula':
            if pulos_disponiveis == 0:
                print_red('Você não tem mais pulos disponíveis')
                input('Aperte ENTER para responder novamente...')
            else:
                pulos_disponiveis -= 1
                if pulos_disponiveis == 0:
                    print('Você pulou a questão e não tem mais pulos disponíveis')
                else:
                    print(f"Você pulou a questão e ainda tem {pulos_disponiveis} pulos disponíveis")
                    fim_da_questao = True
        elif resposta == 'ajuda':
            if ajudas_disponiveis == 0:
                print_red('Você não tem mais ajudas disponíveis')
                input('Aperte ENTER para responder novamente...')
            elif usou_ajuda:
                print_red('Você já usou ajuda nessa questão!')
                input('Aperte ENTER para responder novamente...')
            else:
                ajudas_disponiveis -= 1
                usou_ajuda = True
                print(gera_ajuda(questao_atual))
                print(f"Você usou uma ajuda e ainda tem {ajudas_disponiveis} ajudas disponíveis")
        elif resposta == 'parar':
            print(f"Você parou com R$ {lista_premios[questoes_acertadas]:05.2f}")
            fim_do_jogo = True
        elif resposta in ['A', 'B', 'C', 'D']:
            print_red(f"VOCÊ ERROU! Você perdeu tudo :(")
            fim_do_jogo = True
        else:
            print_red('OPÇÃO INVÁLIDA!')
            print("As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula' ou 'parar'")
            input('Aperte ENTER para responder novamente...')
    
    if questoes_acertadas == 9: fim_do_jogo = True
    
    if fim_do_jogo:
        replay = input("Gostaria de jogar novamente? [S/N] ")
        if replay.upper() == 'S':
            fim_do_jogo = False
            # Reinicia as variáveis
            ajudas_disponiveis = 2
            pulos_disponiveis = 3
            numero_questao = 0
            questoes_acertadas = 0
            questoes_sorteadas = []
            system("cls")
            manual_do_jogo(nome)