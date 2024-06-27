from logging_config import setup_logging
import psutil

def status(percentual):
    if percentual < 50:
        return "Baixo"
    elif percentual < 80:
        return "Moderado"
    else:
        return "Alto"

def monitor_resources(log_dir):
    logger = setup_logging('Status_recursos', log_dir=log_dir)
    try:
        cpu = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        
        cpu_status = status(cpu)
        memory_status = status(memory_info.percent)
        disk_status = status(disk_usage.percent)
        
        logger.info(f'CPU: {cpu}% ({cpu_status}), Memoria: {memory_info.percent}% ({memory_status}), Disco: {disk_usage.percent}% ({disk_status})')
        
        return {
            'CPU': cpu,
            'CPU Status': cpu_status,
            'Memoria': memory_info.percent,
            'Memoria Status': memory_status,
            'Disco': disk_usage.percent,
            'Disk Status': disk_status
        }
    except Exception as e:
        logger.error(f'Erro no monitoramento dos recursos: {str(e)}')
        return None
