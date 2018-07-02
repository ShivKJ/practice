from datetime import datetime
from logging import Formatter, INFO, StreamHandler, getLogger
from logging.handlers import RotatingFileHandler
from os import makedirs
from os.path import dirname, exists, join
from sys import stdout

from dateutil.tz import gettz

__TOP_LEVEL_DIR = join(dirname(__file__), 'log')

if not exists(__TOP_LEVEL_DIR):
    makedirs(__TOP_LEVEL_DIR)

LOGGER_NAME = 'PRACTICE'


def initialize_logger(logger_name):
    logger = getLogger(logger_name)
    logger.setLevel(INFO)

    # --------------------------Creating Formatter----------------------------------
    fmt = Formatter('%(asctime)s %(name)s %(levelname)s '
                    '%(pathname)s [%(filename)s] '
                    '[%(lineno)d] %(message)s')

    INDIA = gettz('Asia/Kolkata')
    UTC = gettz('UTC')

    fmt.converter = lambda x: (datetime
                               .utcfromtimestamp(x)
                               .replace(tzinfo=UTC)
                               .astimezone(INDIA)
                               .timetuple())

    # ---------------Adding File Handler--------------------

    LOG_FILE = join(__TOP_LEVEL_DIR, str(datetime.utcnow()
                                         .replace(tzinfo=UTC)
                                         .astimezone(INDIA)
                                         .date()) + '.log')

    fh = RotatingFileHandler(LOG_FILE,
                             maxBytes=1024 * 1024 * 8,
                             backupCount=5)
    fh.setLevel(INFO)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    # -----------------Adding Stream Handler-----------------
    sh = StreamHandler(stdout)
    sh.setFormatter(fmt)
    sh.setLevel(INFO)
    logger.addHandler(sh)
    logger.info('Logger %s initialized', logger_name)
    
    return logger


initialize_logger(LOGGER_NAME)
