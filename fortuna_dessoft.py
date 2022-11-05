#### BEM-VINDO AO FORTUNA DESSOFT - BY SAMUEL JABES E VINICIUS RODRIGUES ####

from random import randint

def transforma_base(lista_questoes):
    questoes_por_nivel = {}
    for questao in lista_questoes:
        if questao['nivel'] not in questoes_por_nivel:
            questoes_por_nivel[questao['nivel']] = [questao]
        else:
            questoes_por_nivel[questao['nivel']].append(questao)
    return questoes_por_nivel

def sorteia_questao(lista_questoes, nivel):
    numero_questao = randint(0, len(lista_questoes[nivel])-1)
    questao_sorteada = lista_questoes[nivel][numero_questao]
    return questao_sorteada