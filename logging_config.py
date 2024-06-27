import logging
import os

from logging.handlers import RotatingFileHandler

def setup_logging(log_name, log_dir):
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{log_name}.log")
    
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    return logger
