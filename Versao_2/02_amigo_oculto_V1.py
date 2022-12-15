
# VERSAO 2 (A VERSAO DE ENTRADA DO TERMINAL)

# Depois colocar de forma mais completa, por exemplo:
# . Modificar para que os nomes das pessoas sejam inseridos por uma interfacie grafica.
# . Colocar para enviar para o e-mail das pessoas por exemplo os resultados.
# . ...

# =============================================================================================== #

# cd Documents/GitHub/Amigo_oculto/Versao_2

# python3.9 02_amigo_oculto_V1.py

# =============================================================================================== #

import os

import numpy as np

# =============================================================================================== #

important_files_1 = '02_amigo_oculto.py'

important_files_2 = '02_nome_das_pessoas.txt'

important_files_3 = '02_arquivos_criados_para_sorteio.txt'

cwd = os.getcwd()

print()
print('-'*5 + ' SORTEIO DE AMIGO OCULTO ' + '-'*5)
print()
print('Oi, os nomes que já estavam no arquivo txt já foram carregados.')
print()
print('A partir de agora você poderá adicionar novos nomes.')
print()
print('Caso queira fazer o sorteio poderá fazer a qualquer momento.')
print()
print('Caso queira só deixar salvo os nomes adicionados poderá também só sair do programa que já ficará salvos os nomes que você adicionou.')
print()

the_length_1 = len('-'*5 + ' SORTEIO DE AMIGO OCULTO ' + '-'*5)

print('-'*the_length_1)
print()

try:
    with open(important_files_2, 'r') as f:
        the_name_list = f.readlines()
except:
    with open(important_files_2, 'w') as f:
        f.write('')
    with open(important_files_2, 'r') as f:
        the_name_list = f.readlines()

try:
    with open(important_files_3, 'r') as f:
        the_list_of_files = f.readlines()
except:
    with open(important_files_3, 'w') as f:
        f.write('')
    with open(important_files_3, 'r') as f:
        the_list_of_files = f.readlines()

if (not not the_name_list):
    for i1 in range(len(the_name_list)):
        the_name_list[i1] = the_name_list[i1].replace('\n', '')

while True:

    if ( not not the_name_list ):
        the_name_list.sort()

    the_string_1 = 'Por favor digite:'
    the_string_2 = '\no nome de uma pessoa para adicionar uma pessoa,'
    the_string_3 = '\n\'sair\' para sair do programa,'
    the_string_4 = '\n\'sortiar\' para fazer o sorteio,'
    the_string_5 = '\n\'nomes\' para ver os nomes dos participantes,'
    the_string_6 = '\n\'apagar\' para poder apagar algum nome da lista.\n\n'
    the_string = the_string_1 + the_string_2 + the_string_3 + the_string_4 + the_string_5 + the_string_6
    the_new_name = input(the_string)
    the_new_name = the_new_name.lower()

    condition_1 = the_new_name == 'sair'

    condition_2 = the_new_name == 'sortiar'

    condition_3 = the_new_name == 'nomes'

    condition_4 = the_new_name == 'apagar'

    condition_5 = ( not condition_1 ) and ( not condition_2 ) and ( not condition_3 ) and ( not condition_4 )

    if condition_1:
        print()
        print('Tchau!')
        print()
        with open(important_files_2, 'w') as f:
            if (not not the_name_list):
                for i1 in range(len(the_name_list)):
                    if (i1!=(len(the_name_list)-1)):
                        f.write(the_name_list[i1])
                        f.write('\n')
                    else:
                        f.write(the_name_list[i1])
            else:
                f.write('')
        break

    if condition_2:
        # Deletando os arquivos gerados do ultimo sorteio:
        if (not not the_list_of_files):
            files_in_the_directory = os.listdir(cwd)
            for i1 in range(len(the_list_of_files)):
                if (the_list_of_files[i1] in files_in_the_directory):
                    the_path = os.path.join(cwd, the_list_of_files[i1])
                    os.remove(the_path)
        # -----
        the_list_of_files = []
        # -----
        idx = np.argsort(np.random.random(len(the_name_list)))
        new_name_list = [0] * len(the_name_list)
        for i1 in range(len(new_name_list)):
            new_name_list[i1] = the_name_list[idx[i1]]
        for i1 in range(len(new_name_list)):
            file_name = 'amigo_oculto_' + new_name_list[i1] + '.txt'
            the_list_of_files.append(file_name)
            if ( i1 == ( len(new_name_list) - 1 ) ):
                the_length = len(new_name_list[0])
                with open(file_name, 'w') as f:
                    f.write('O seu amigo oculto é: / A sua amiga oculta é:')
                    f.write('\n')
                    f.write('---> ')
                    f.write(new_name_list[0])
                    f.write('!'*(20-the_length))
                    f.write('\n')
            else:
                with open(file_name, 'w') as f:
                    the_length = len(new_name_list[i1+1])
                    f.write('O seu amigo oculto é: / A sua amiga oculta é:')
                    f.write('\n')
                    f.write('---> ')
                    f.write(new_name_list[i1+1])
                    f.write('!'*(20-the_length))
                    f.write('\n')
        with open(important_files_3, 'w') as f:
            if (not not the_list_of_files):
                for i1 in range(len(the_list_of_files)):
                    if (i1!=(len(the_list_of_files)-1)):
                        f.write(the_list_of_files[i1])
                        f.write('\n')
                    else:
                        f.write(the_list_of_files[i1])
            else:
                f.write('')


    if condition_3:
        if not the_name_list:
            print('Você não tem nomes na lista.')
        else:
            print('Sua lista:')
            for the_name in the_name_list:
                print('. ' + the_name)

    if condition_4:
        the_string = 'Digite o nome que você quer apagar:\n\n'
        the_delete_name = input(the_string)
        if (the_delete_name in the_name_list):
            the_name_list.remove(the_delete_name)
            print('Nome deletado.')
        else:
            print('Você não tem esse nome na sua lista.')

    if condition_5:
        the_name_list.append(the_new_name)

    print()
    print('-'*the_length_1)
    print()
