import inspect
import logging
import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        loggerName=inspect.stack()[1][3]
        logger= logging.getLogger(loggerName)
        filehandler = logging.FileHandler('//utilities/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger