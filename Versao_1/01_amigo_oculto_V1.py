
# =============================================================================================== #

# VERSÃO 1 (A VERSÃO MAIS SIMPLES)

# Depois colocar de forma mais completa, por exemplo:
# . Colocar algo para podermos inserir os nomes das pessoas, seja pelo terminal, ou por uma interfacie grafica.
# . Colocar para enviar para o e-mail das pessoas por exemplo os resultados.
# . Quando for rodar o programa (no começo, antes de tudo) apargar todos os arquivos que não sejam os necessarios.
# . ...

# OBS.: com esse código temos que só terá um circulo
# (por exemplo, tendo 5 pessoas teriamos 1->2->3->4->5->1 e nunca 1->2->1 e 3->5->4->3),
# e, ninguém tira a si mesmo.

# Luigi Spreafico

# =============================================================================================== #

# Comandos que eu uso.

# cd Documents/GitHub/Amigo_oculto/Versao_1

# python3.9 01_amigo_oculto_V1.py

# =============================================================================================== #

# Modulos que eu uso.

import numpy as np

# =============================================================================================== #

# O programa em si.

# Abrindo o arquivo com os nomes das pessoas e armazendo cada nome como um elemento de uma lista.
with open('01_nome_das_pessoas_V1.txt') as f:
    file_string = f.readlines()

# A proxima linha é para checar se o código está funcionando direitinho, 
# deixar ela comentada quando for usar para não saber quem tirou quem.
# print(file_string)

# Colocando em ordem alfabetica a lista dos nomes. 
# (OBS.: Isso não era preciso.)
file_string.sort()

# A proxima linha é para checar se o código está funcionando direitinho, 
# deixar ela comentada quando for usar para não saber quem tirou quem.
# print(file_string)

# Aqui criamos um vetor com o mesmo número de elementos que o número de participantes. 
# Onde este vetor é feito com números aleatórios de 0 até 1 (não incluindo o 1). 
# Dessa forma, cada vez que rodarmos o programa iremos obter um vetor com elementos diferentes. 
# Depois vamos e obtemos um vetor que nos diz a ordem dos indices de forma que esse nosso vetor fique em ordem correta.
idx = np.argsort(np.random.random(len(file_string)))

# Criamos uma lista com o mesmo número de elementos que o número de participantes.
new_new_file_string = [0] * len(file_string)

# Utilizamos a lista original com os nomes e o vetor com os indices para embaralhar a ordem dos nomes.
for i1 in range(len(new_new_file_string)):
    new_new_file_string[i1] = file_string[idx[i1]]

# A proxima linha é para checar se o código está funcionando direitinho, 
# deixar ela comentada quando for usar para não saber quem tirou quem.
# print(new_new_file_string)

# Agora pegamos e tiramos do final de cada nome o caracter \n.
# Isso é importante para podermos gerar o nome dos arquivos.
for i1 in range(len(new_new_file_string)):
    new_new_file_string[i1] = new_new_file_string[i1].replace('\n', '')

# A proxima linha é para checar se o código está funcionando direitinho, 
# deixar ela comentada quando for usar para não saber quem tirou quem.
# print(new_new_file_string)

# Aqui criar um arquivo .txt para cada pessoa, e depois colocar dentro dele quem essa pessoa tirou.
# Obs.: a forma que vai ser criado o nome do .txt será para ser um amigo oculto de natal, 
# para ser por exemplo de ano novo so mudar "_natal_AAAA" para "_AnoNovo_AAAA". 
# E substituir AAAA pelo ano do amigo oculto (ou data completa: DD_MM_AAAA).
for i1 in range(len(new_new_file_string)):
    file_name = 'amigo_oculto_' + new_new_file_string[i1] + '_natal_2022' + '.txt'
    if ( i1 == ( len(new_new_file_string) - 1 ) ):
        the_length = len(new_new_file_string[0])
        with open(file_name, 'w') as f:
            f.write('O seu amigo oculto é: / A sua amiga oculta é:')
            f.write('\n')
            f.write('---> ')
            f.write(new_new_file_string[0])
            f.write('!'*(20-the_length))
            f.write('\n')
    else:
        with open(file_name, 'w') as f:
            the_length = len(new_new_file_string[i1+1])
            f.write('O seu amigo oculto é: / A sua amiga oculta é:')
            f.write('\n')
            f.write('---> ')
            f.write(new_new_file_string[i1+1])
            f.write('!'*(20-the_length))
            f.write('\n')

# =============================================================================================== #
