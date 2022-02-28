#Imports
from random import randint

#Variaveis
acertos, erros, perguntas = 0, 0, 0
user = dict()

questoes = [ #essas perguntas são apenas para teste, futuramente pretendo usar um banco de dados 
    {'perg': 'Qual a cor do ceu?', 'resp': ( 'azul', 'roxo', 'Amarelo'), 'certa': 'azul'}, 
    {'perg': 'Quantas saias de filó tem a barata?', 'resp': ('7', '1', '12'), 'certa': '1'}, 
    {'perg': 'Qual o primeiro nome de einstein?', 'resp': ('Albert', 'Robert', 'Cleber'), 'certa': 'Albert'}
]

#avisos iniciais
print('Vamos dar inicio a sua prova')
user['nome'] = input('primeiro diga seu nome: ')
user['idade'] = input('sua idade: ')
print(f'certo {user["nome"]} vamos iniciar sua prova\nBoa sorte!')

#fase de prova
while True:

    # codigo responsável por montar a pergunta
    pergunta_escolhida = randint(0, len(questoes) -1)
    print()
    print(questoes[pergunta_escolhida]['perg'])
    escolha = 1
    for c in questoes[pergunta_escolhida]['resp']:
        print(f'{escolha}. {c}')
        escolha += 1

    #codigo q obtem a respota do usuário
    resposta = int(input('escolha uma resposta(apenas o numero): ')) -1
    if questoes[pergunta_escolhida]['resp'][resposta] == questoes[pergunta_escolhida]['certa']:
        acertos += 1
    else:
        erros += 1
    
    #codigo que finaliza a prova
    perguntas += 1
    if perguntas == 3:
        break

#Resultado
print()
print('---fim da prova---')
print(f'Você acertou {acertos}')
print(f'Você errou {erros}')
