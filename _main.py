#!/usr/bin/env python3
import _servicos as check_service_status
import _backup as backup_files
import _recursos as monitor_resources
from logging_config import setup_logging

import platform

def setup_custom_logging(log_dir, log_name):
    return setup_logging(log_name, log_dir=log_dir)

def main(backup_dir, log_dir):
    #Ajustar os diretórios para o sistema operacional atual
    if platform.system() != 'Windows':
        backup_dir = backup_dir.replace("\\", "/").replace("C:", "/mnt/c")
        log_dir = log_dir.replace("\\", "/").replace("C:", "/mnt/c")

    #Configura o logger para o backup
    backup_logger = setup_custom_logging(log_dir, 'Backup_arquivos')
    
    #Verifica o status dos serviços
    services = ['w3svc', 'MSSQLSERVER']
    service_statuses = {service: check_service_status.check_service_status(service, log_dir) for service in services}
    
    #Realiza o backup dos arquivos
    source_paths = [r'C:\inetpub\wwwroot', r'C:\Program Files\Microsoft SQL Server']
    if platform.system() != 'Windows':
        source_paths = [path.replace("\\", "/").replace("C:", "/mnt/c") for path in source_paths]
    backup_file = backup_files.backup_files(source_paths, backup_dir, backup_logger)
    
    #Monitora os recursos do sistema
    resource_usage = monitor_resources.monitor_resources(log_dir)


if __name__ == "__main__":
    #Diretórios
    backup_dir = "C:\\Users\\Bl4ck0ut\\Pictures\\Teste 3\\Windows e Linux\\Backup"
    log_dir = "C:\\Users\\Bl4ck0ut\\Pictures\\Teste 3\\Windows e Linux\\log"
    
    main(backup_dir, log_dir)
