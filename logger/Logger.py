import datetime
from abc import abstractmethod, ABCMeta
from sys import stdout

class Logger(object):
    __metaclass__ = ABCMeta

    def __init__(self, verbose=True):
        self._verbose = verbose

    @abstractmethod
    def log(self, message, includeTimestamp=False, onlyIfVerbose=False):pass

    def set_carriage_reset(self, carriage_reset=False): pass

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


class DummyLogger(Logger):
    def log(self, message, includeTimestamp=False, onlyIfVerbose=False): pass

    def getLog(self):
        return None

    def printLog(self):pass


class StdOutLogger(Logger):
    def __init__(self, verbose=True):
        super(StdOutLogger, self).__init__(verbose)
        self._newline = '\n'

    def set_carriage_reset(self, carriage_reset=False):
        if carriage_reset:
            self._newline = ''
        else:
            self._newline = '\n'

    def log(self, message, includeTimestamp=False, onlyIfVerbose=False):
        s = self._createLogMessage(message, includeTimestamp, onlyIfVerbose)
        if s is not None:
            stdout.write(s + self._newline)

    def getLog(self):
        return None

    def printLog(self):pass


class StringLogger(Logger):
    def __init__(self,  verbose=True):
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


class FileLogger(Logger):
    def __init__(self, logFileName, verbose=True):
        super(FileLogger, self).__init__(verbose)
        self._logFileName = logFileName

    def log(self, message, includeTimestamp=False, onlyIfVerbose=False):
        s = self._createLogMessage(message, includeTimestamp, onlyIfVerbose)
        if s is not None:
            f_obj = open(self._logFileName, "a")
            f_obj.write(s + '\n')
            f_obj.close()

    def getLog(self):
        f_obj = open(self._logFileName, "r")
        out = f_obj.readlines()
        f_obj.close()
        return out

    def printLog(self):
        lines = self.getLog()
        for line in lines:
            print line.rstrip()
