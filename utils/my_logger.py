import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler

from core.settings import Setting


def init_logging(logname:str=Setting.LOG_ROOT,level:int=logging.DEBUG,filepath:str=None):

    logger = logging.getLogger(logname)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if filepath is not None:
        file_dir = os.path.split(filepath)[0]
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)
        fhandler=TimedRotatingFileHandler(filename=filepath,encoding='utf-8',when='d',interval=1,backupCount=90)
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
    return logger

def set_logger_level(logname:str=Setting.LOG_ROOT,level:int=logging.DEBUG):
    logging.getLogger(logname).setLevel(level)

def get_logger(name:str=Setting.LOG_ROOT):
    #获取当前时间
    logger = init_logging(filepath=os.path.join(os.getcwd(),"logs",time.strftime("%Y%m%d", time.localtime())+'.log'))
    return logger