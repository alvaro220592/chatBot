# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ===================================================== #
# ---------------------CHATBOT------------------------- #
# ===================================================== #
#                                                       #
# Projeto de chat entre o usuário e a máquina, cuja     #
# função é construir interações simples e inteligentes  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #


print(
    
    '=====================================================\n'
    '---------------------CHATBOT-------------------------\n'
    '=====================================================\n'
)


# O nome virá do usuário e será armazenado em letra minúscula para prevenir nomes repetidos com caixa diferente.
nome = input('Oi, qual o seu nome?\n').lower()

# aqui é iniciada a criação de um arquivo de texto(caso este ainda não exista) para escrita dos nomes.
fileW = open('nomes.txt', 'a', encoding='utf8')

# atribuindo o mesmo arquivo, desta vez para leitura, à variável fileR
fileR = open('nomes.txt') 

# se o nome digitado já estiver no arquivo(a verificação é feita com o método .read()):
if nome in fileR.read():
    print(f'Oi, {nome}! Legal te ver novamente...') # O programa 'reconhece' o usuário
    fileR.close() # e fecha a conexão com o arquivo

# se o nome não estiver no arquivo:
else:
    fileW.write(nome + '\n') # o sistema escreverá o nome inserido pelo usuário no arquivo(a inserção é feita pelo método .write())
    print(f'Oi, {nome}! Prazer em te conhecer...') # se comporta como se estivesse conhecendo o usuário agora.

# A conexão com o arquivo é fechada fora da condição acima para que seu comando seja feito apenas 1 vez.
fileW.close()