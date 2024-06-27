#	Verificar o status dos serviços principais (por exemplo, Apache, MySQL, IIS, etc.).
from logging_config import setup_logging
import platform
import subprocess

def check_service_status(service_name, log_dir):
    logger = setup_logging('Status_serviços', log_dir=log_dir)
    try:
        if platform.system() == 'Windows':
            import win32serviceutil
            status = win32serviceutil.QueryServiceStatus(service_name)[1]
            result = 'Running' if status == 4 else 'Stopped'
        else:
            result = subprocess.run(['systemctl', 'is-active', service_name], capture_output=True, text=True).stdout.strip()
        
        logger.info(f'Serviço {service_name} Status: {result}')
        return result
    except Exception as e:
        logger.error(f'Erro ao verificar servico {service_name}: {str(e)}')
        return f'Erro: {str(e)}'
