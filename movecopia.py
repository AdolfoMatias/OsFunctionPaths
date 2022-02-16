#bibliotecas do sistema e que interagem no diretorio
import os
import shutil

#função que procura arquivo pasta
def procura():

    """Retorna uma pasta procurada"""

    pasta_procura = input('Digite a pasta: ')
    return pasta_procura

#função de criar pasta
def cria_pasta():

    """Cria uma pasta indicada, casso já exista ela retorna a existência"""

    try:
        nova_pasta = input('Digite nova pasta: ')
        os.mkdir(nova_pasta)
    except FileExistsError:
        print('Pasta já existe.')
        return
    return nova_pasta

#função pra arquivos mover arquivos entre pasta
def move():

    """Procura um caminho antigo, caminho novo e um arquivo, se encontrado
    o arquivo ela  move o arquivo pra nova pasta, caso não encontrado ela retorna mensagem de inexistência do arquivo."""

    print('-----PROCURAR EM-----')
    caminho_velho = procura()
    print('-----MOVER PARA-----')
    caminho_novo = procura()
    print('-----COPIAR PARA-----')
    arquivo_mov = input('Qual arquivo: ')
    for raiz, diretorios, arquivos in os.walk(caminho_velho):
        for arquivo in arquivos:
            if arquivo_mov in arquivo:
                pasta_velha = os.path.join(raiz, arquivo)
                pasta_nova = os.path.join(caminho_novo, arquivo)
                info  = print(f'''Arquivo: {arquivo_mov} movido com sucesso para:
                {pasta_nova} ''')
                shutil.move(pasta_velha, pasta_nova)
                return info
            else:
                print(f'Arquivo: {arquivo_mov} não encontrado.')
                return
    

#função pra arquivos copiar arquivos entre pasta
def copia():

    """Procura um caminho antigo, caminho novo e um arquivo, se encontrado
    o arquivo ela  copia o arquivo pra nova pasta, caso não encontrado ela retorna mensagem de inexistência do arquivo."""

    print('-----PROCURAR EM-----')
    caminho_velho = procura()
    print('-----COPIAR PARA-----')
    caminho_novo = procura()
    print('-----COPIAR PARA-----')
    arquivo_cop = input('Qual arquivo: ')
    for raiz, diretorios, arquivos in os.walk(caminho_velho):
        for arquivo in arquivos:
            if arquivo_cop in arquivo:
                pasta_velha = os.path.join(raiz, arquivo)
                pasta_nova = os.path.join(caminho_novo, arquivo)
                info = print(f'''Arquivo: {arquivo_cop} copiado com sucesso para:
                {pasta_nova} ''')
                shutil.copy(pasta_velha, pasta_nova)
                return info
            else:
                print(f'Arquivo: {arquivo_cop} não encontrado.')
                return
    

#função que  deleta arquivos entre pastas
def deletar():
    """Procura um caminho e um arquivo, se encontrado
    o arquivo ela  deleta o arquivo da pasta, caso não encontrado ela retorna mensagem de inexistência do arquivo."""

    print('-----DELETAR EM-----')
    caminho_procura = procura()
    arquivo_del = input('Qual arquivo: ')
    for raiz, diretorios, arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            if arquivo_del in arquivo:
                pasta_arquivo = os.path.join(raiz, arquivo)
                info = print(f'Arquivo: {arquivo_del} deletado com sucesso.')
                os.remove(pasta_arquivo)
                return  info

            else:
                print(f'Arquivo: {arquivo_del} não encontrado.')
                return
    



if __name__ == '__main__':
    copia()

