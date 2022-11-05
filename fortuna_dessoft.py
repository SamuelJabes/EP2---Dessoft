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

def valida_questao(questao):
    erros_na_questao = {}

    # Checando se as chaves exigidas estão na questão
    chaves_necessarias = ['titulo', 'nivel', 'opcoes', 'correta']
    for chave in chaves_necessarias:
        if chave not in questao:
            erros_na_questao[chave] = 'nao_encontrado'

    # Checando se o número de chaves está correto
    if len(questao.keys()) != 4:
        erros_na_questao['outro'] = 'numero_chaves_invalido'

    # Checa se o título existe e não está vazio ou em branco
    if 'titulo' in questao.keys() and questao['titulo'].strip() == '':
        erros_na_questao['titulo'] = 'vazio'

    # Checa se há a chave 'nível' e se ela contém um nível válido
    niveis_possiveis = set(['facil', 'medio', 'dificil'])
    if ('nivel' in questao.keys()) and (questao['nivel'] not in niveis_possiveis):
        erros_na_questao['nivel'] = 'valor_errado'

    letras_opcoes = ['A', 'B', 'C', 'D']
    if 'opcoes' in questao.keys():
        if len(questao['opcoes'].keys()) != 4:
            # Checa se há a chave 'opcoes' e se seu valor contém quatro chaves
            erros_na_questao['opcoes'] = 'tamanho_invalido'
        else:
            letras_estao = True
            for letra in letras_opcoes:
                if letra not in questao['opcoes']: letras_estao = False

            if letras_estao:
                for letra in letras_opcoes:
                    if questao['opcoes'][letra].strip() == '':
                        if 'opcoes' not in erros_na_questao:
                            erros_na_questao['opcoes'] = {f'{letra}':'vazia'}
                        else:
                            erros_na_questao['opcoes'][letra] = 'vazia'
            else:
                erros_na_questao['opcoes'] = 'chave_invalida_ou_nao_encontrada'

    # Checa se há a chave 'correta' e se existe uma opção válida nela
    if ('correta' in questao.keys()) and (questao['correta'] not in letras_opcoes):
        erros_na_questao['correta'] = 'valor_errado'

    return erros_na_questao

def valida_questoes(lista_questoes):
    lista_problemas = []
    for questao in lista_questoes:
        problemas = valida_questao(questao)
        lista_problemas.append(problemas)
    return lista_problemas

def sorteia_questao(lista_questoes, nivel):
    numero_questao = randint(0, len(lista_questoes[nivel])-1)
    questao_sorteada = lista_questoes[nivel][numero_questao]
    return questao_sorteada