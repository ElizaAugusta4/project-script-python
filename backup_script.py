import os
import zipfile

def fazer_backup(pasta_origem, arquivo_destino):
    # Verifica se a pasta de origem existe
    if not os.path.exists(pasta_origem):
        print(f'A pasta de origem "{pasta_origem}" não existe.')
        return

    # Cria um arquivo ZIP para o backup
    with zipfile.ZipFile(arquivo_destino, 'w') as zipf:
        # Percorre todos os arquivos e subpastas na pasta de origem
        for pasta_raiz, _, arquivos in os.walk(pasta_origem):
            for arquivo in arquivos:
                caminho_completo = os.path.join(pasta_raiz, arquivo)
                # Adiciona cada arquivo ao arquivo ZIP mantendo a estrutura de pastas
                zipf.write(caminho_completo, os.path.relpath(caminho_completo, pasta_origem))

    print(f'Backup concluído! Arquivo criado em "{arquivo_destino}".')

# Pasta a ser backupeada
pasta_origem = r'C:\Users\eliza\OneDrive\Documentos\Estudos_Devosp-mao-na-massa\projetos-estudos\project-jenkins-github'  # Substitua pelo caminho da pasta que você quer backupear
arquivo_destino = 'backup.zip'  # Nome do arquivo ZIP de destino

fazer_backup(pasta_origem, arquivo_destino)



fazer_backup(pasta_origem, arquivo_destino)
