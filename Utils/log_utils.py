# encoding:utf-8

# 日志
import logging
from logging.handlers import RotatingFileHandler


class Log():
    '''

    '''

    def __init__(self, file_path, level=logging.ERROR,name=__name__):
        logger = logging.getLogger(name)
        logger.setLevel(level=level)
        # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
        rHandler = RotatingFileHandler(file_path, maxBytes=1 * 1024 * 1024, backupCount=3, encoding='utf-8')
        # rHandler = logging.FileHandler(file_path, encoding='utf-8')
        rHandler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        rHandler.setFormatter(formatter)
        logger.addHandler(rHandler)

        console = logging.StreamHandler()
        console.setLevel(level)
        console.setFormatter(formatter)
        logger.addHandler(console)
        self.logger = logger

    #     self.queue = queue.Queue()
    #     self.queue.get()
    #     t = threading.Thread(target=self.worker)
    #     t.start()
    #
    # def worker(self):
    #     while True:
    #         message = self.queue.get()
    #         getattr(self._logger,message[0])(message[1])
    #
    # @property
    # def debug(self):
    #     return
    #
    # @debug.setter
    # def debug(self,value):
    #     self.queue.put(('debug',value))
    #
    # @property
    # def info(self):
    #     return
    #
    # @info.setter
    # def info(self,value):
    #     self.queue.put(('info',value))
    #
    # @property
    # def warning(self):
    #     return
    #
    # @warning.setter
    # def warning(self,value):
    #     self.queue.put(('warning',value))
    #
    # @property
    # def error(self):
    #     return
    #
    # @error.setter
    # def error(self,value):
    #     self.queue.put(('error',value))
