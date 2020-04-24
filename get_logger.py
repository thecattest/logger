import logging


def get_logger(fn, logger_name="converter"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(fn)
    formatter = logging.Formatter('%(asctime)s - %(name)s.%(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


if __name__ == '__main__':
    logger = get_logger("log1.log", "bot")
    logger.info("Hell o world")
    logger.error("You")

    logger2 = get_logger("log2.log", "logger2")
    logger2.info("WORKS")

    logger2 = get_logger("log1.log", "logger2")
    logger2.info("IT WORKS TOO")
