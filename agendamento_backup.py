import schedule
import time
import zipfile
import os

def fazer_backup(pasta_origem, arquivo_destino):
    if not os.path.exists(pasta_origem):
        print(f'A pasta de origem "{pasta_origem}" não existe.')
        return

    arquivos = os.listdir(pasta_origem)

    with zipfile.ZipFile(arquivo_destino, 'w') as zipf:
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_origem, arquivo)
            zipf.write(caminho_completo, os.path.basename(caminho_completo))

    print(f'Backup concluído! Arquivo criado em "{arquivo_destino}".')

def executar_backup_agendado():
    pasta_origem = 'C:/Users/eliza/OneDrive/Documentos/Estudos_Devosp-mao-na-massa/projetos-estudos/project-jenkins-github' 
    arquivo_destino = 'backup.zip'  # Nome do arquivo ZIP de destino
    fazer_backup(pasta_origem, arquivo_destino)


schedule.every().day.at("14:29").do(executar_backup_agendado)

while True:
    schedule.run_pending()
    time.sleep(60)  # Verificar a cada minuto se há tarefas agendadas para executar
