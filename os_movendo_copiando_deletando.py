import os
import shutil


#funçãoq que cria pasta e percorre por ela
    
def cria():
    v1 = input('Digite a pasta: ')
    v2 = input('Digite a nova: ')

    try:
        os.mkdir(v2)
    except FileExistsError as e:
        print(f'Já existe {v2}')
    
    for raiz, diretorios, arquivos in os.walk(v1):
        for arquivo in arquivos:
            pasta_velha = os.path.join(raiz, arquivo)
            pasta_nova = os.path.join(v2,arquivo )
            nome_ar, ext_ar = os.path.splitext(arquivo)

#função que move itens
def mover():
    v1 = input('Digite a pasta: ')
    v2 = input('Digite a nova: ')

    try:
        os.mkdir(v2)
    except FileExistsError as e:
        print(f'Já existe {v2}')

    for raiz, diretorios, arquivos in os.walk(v1):
        for arquivo in arquivos:
            pasta_velha = os.path.join(raiz, arquivo)
            pasta_nova = os.path.join(v2,arquivo)
            
            shutil.move(pasta_velha, pasta_nova)

            print(f'Arquivo movido {arquivo}')


#função que copia itens de uma pasta
def copiar():
    v1 = input('Digite a pasta: ')
    v2 = input('Digite a nova: ')

    try:
        os.mkdir(v2)
    except FileExistsError as e:
        print(f'Já existe {v2}')

    for raiz, diretorios, arquivos in os.walk(v1):
        for arquivo in arquivos:
            pasta_velha = os.path.join(raiz, arquivo)
            pasta_nova = os.path.join(v2,arquivo)
            
            shutil.copy(pasta_velha, pasta_nova)
            print(f'Arquivo copiado {arquivo}')


#Função que deleta itens de uma pasta

def deletar():
    v1 = input('Digite a pasta: ')
    
   
    for raiz, diretorios, arquivos in os.walk(v1):
        for arquivo in arquivos:
            pasta_velha = os.path.join(raiz, arquivo)
            
            print(f'Arquivo deletado {arquivo}')
            os.remove(pasta_velha)

if __name__ =='__main__':
    #mover()
    deletar()
    



