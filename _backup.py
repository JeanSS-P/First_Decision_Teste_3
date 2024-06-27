from logging_config import setup_logging
import os
import platform
import subprocess
from datetime import datetime

def get_backup_dir(backup_dir):
    os.makedirs(backup_dir, exist_ok=True)
    return backup_dir

def backup_files(source_paths, backup_dir, logger):
    try:
        #Obter o diretório de backup
        backup_dir = get_backup_dir(backup_dir)

        #Cria um nome de arquivo de backup com um timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(backup_dir, f'backup_{timestamp}.tar.gz')
        
        #Verifica o sistema operacional
        for path in source_paths:
            parent_dir, folder_name = os.path.split(path)
            if platform.system() == 'Windows':
                subprocess.run(['tar', '-czf', backup_file, '-C', parent_dir, folder_name], shell=True)
            else:
                subprocess.run(['tar', '-czf', backup_file, '-C', parent_dir, folder_name])
        
        #Registra a criação do backup no log
        logger.info(f'Backup criado em {backup_file}')
        return backup_file
    except Exception as e:
        #Em caso de erro, registra a mensagem de erro no log
        logger.error(f'Erro na criacao do backup: {str(e)}')
        return None
