import datetime
from abc import abstractmethod, ABCMeta
from sys import stdout


class Logger(object):
    __metaclass__ = ABCMeta

    def __init__(self, verbose=True):
        self._verbose = verbose

    @abstractmethod
    def log(self, message, includeTimestamp=False, onlyIfVerbose=False):pass

    def _createLogMessage(self, message, includeTimestamp=False, onlyIfVerbose=False):
        out = ''
        if onlyIfVerbose:
            if not self._verbose: return None
        if includeTimestamp:
            out += str(datetime.datetime.now()) + ': '
        out += message
        return out


    @abstractmethod
    def getLog(self): pass

    @abstractmethod
    def printLog(self): pass

class StdOutLogger(Logger):
    def log(self, message, includeTimestamp=False, onlyIfVerbose=False):
        s = self._createLogMessage(message, includeTimestamp, onlyIfVerbose)
        if s is not None:
            stdout.write(s + '\n')

    def getLog(self):
        return None

    def printLog(self):pass


class StringLogger(Logger):
    def __init__(self,  verbose):
        super(StringLogger, self).__init__(verbose)
        self._log=''

    def log(self, message, includeTimestamp=False, onlyIfVerbose=False):
        s = self._createLogMessage(message, includeTimestamp, onlyIfVerbose)
        if s is not None:
            self._log += s + '\n'

    def getLog(self):
        return self._log

    def printLog(self):
        print (self._log)