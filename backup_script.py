import os
import zipfile

def fazer_backup(pasta_origem, arquivo_destino):
    if not os.path.exists(pasta_origem):
        print(f'A pasta de origem "{pasta_origem}" não existe.')
        return


    with zipfile.ZipFile(arquivo_destino, 'w') as zipf:
        for pasta_raiz, _, arquivos in os.walk(pasta_origem):
            for arquivo in arquivos:
                caminho_completo = os.path.join(pasta_raiz, arquivo)
                zipf.write(caminho_completo, os.path.relpath(caminho_completo, pasta_origem))

    print(f'Backup concluído! Arquivo criado em "{arquivo_destino}".')

# Pasta a ser backupeada
pasta_origem = r'C:\Users\eliza\OneDrive\Documentos\Estudos_Devosp-mao-na-massa\projetos-estudos\project-jenkins-github' 
arquivo_destino = 'backup.zip'  

fazer_backup(pasta_origem, arquivo_destino)
