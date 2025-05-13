import logging

def setup_logger(log_path="logs/syntherra.log"):
    logger = logging.getLogger("syntherra")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

# Usage
# logger = setup_logger()
# logger.info("Bot started successfully.")
