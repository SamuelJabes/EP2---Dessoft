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


#### AQUI COMEÇA NOSSO JOGO ####

nome = input("Informe o seu nome: ")
print(f'''
========================= BEM-VINDO AO FORTUNA DESSOFT!!! =========================
\n
{nome}, você receberá uma pergunta a cada rodada e deverá responder qual o item correto.\n
A cada resposta correta, seu prêmio aumenta, mas se errar, você perde tudo!\n\n

Você poderá solicitar ajuda dos universitários até 2 vezes digitando "ajuda".\n
Você poderá pular até 3 questões digitando "pular".\n
Se você achar que não sabe a resposta, pode escolher sair com o que conseguiu digitando "parar".\n
===================================================================================
''')