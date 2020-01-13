import os
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logfile = os.path.join(os.path.dirname(os.path.relpath(__file__)),"test_log.log")
handler =logging.FileHandler(logfile)
handler.setLevel(logging.INFO)

def error():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

