import os

from loguru import logger


def create_logger(client_name, response_log):

    try:
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        log_folder = f"../logs/{client_name}"

        # Create the log folder if it doesn't exist
        os.makedirs(log_folder, exist_ok=True)

        log_file = f"{log_folder}/{client_name}{response_log}_app.log"

        logger.add(log_file, rotation="1 day", retention="10 days", compression="zip", level="INFO",
                   format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function}:{line} | {message}")
        # logger.add(sys.stdout, level="INFO", format="{time} - {level} - {message}")
    except Exception as e:
        print(str(e))
    return logger

