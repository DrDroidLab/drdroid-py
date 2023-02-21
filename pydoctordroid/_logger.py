import logging
import sys


def setup_logger(name: str = 'drdroid.sdk.global', debug: bool = False) -> logging.Logger:
    logger = logging.getLogger(name)

    log_level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(log_level)

    formatter = logging.Formatter(fmt='[drdroid] %(asctime)s %(levelname)s %(message)s')
    handler = logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
