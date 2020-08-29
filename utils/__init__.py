import os

from utils.my_logger import init_logging
from core.settings import Setting

COREBASEDIR = os.path.abspath(os.path.dirname(__file__))

# init_logging()

def init_core_log():
    return init_logging(logname=__name__,level=Setting.LOG_LEVEL,filepath=os.path.join(Setting.LOG_FILE_ROOT_PATH,__name__,'log.log'))