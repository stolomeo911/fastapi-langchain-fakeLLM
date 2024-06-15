import logging
import os
from datetime import datetime

session_id = datetime.today().strftime('%Y%m%d')


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not getattr(logger, 'is_logger_setup', False):
        # Create subfolder with the session ID
        session_folder = os.path.join('logs', session_id)
        if not os.path.exists(session_folder):
            os.makedirs(session_folder)

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add formatter to handlers
        ch.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(ch)

        # Mark logger as setup
        logger.is_logger_setup = True

    return logger
