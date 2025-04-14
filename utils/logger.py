# utils/logger.py

import logging
import sys

def setup_logger(name=__name__, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Cria um console handler com o mesmo nível
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    
    # Define o formato das mensagens de log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Adiciona o handler somente se não existir nenhum
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger
