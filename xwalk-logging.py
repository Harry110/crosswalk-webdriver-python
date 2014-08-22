#!/usr/bin/env python
import log
import session
import calendar
import time

g_log_level = Log.kWarning
g_start_time = 0
kLevelToName =[
  "ALL",  // kAll
  "DEBUG",  // kDebug
  "INFO",  // kInfo
  "WARNING",  // kWarning
  "SEVERE",  // kError
  "OFF",  // kOff
];


def LevelToName(level):
  index = level - Log.kAll
  #TODO:
  return kLevelToName[index]


kNameToLevel = {
  "ALL" : Log.kAll,
  "DEBUG" : Log.kDebug,
  "INFO" : Log.kInfo),
  "WARNING" : Log.kWarning,
  "SEVERE" : Log.kError,
  "OFF" : Log.kOff
} 
def GetLevelFromSeverity(severity)
  options = {
    logging.LOG_FATAL : Log.kError,
    logging.LOG_ERROR_REPORT : Log.kError,
    logging.LOG_ERROR : Log.kError,
    logging.LOG_WARNING : Log.kWarning,
    logging.LOG_INFO : Log.kInfo,
    logging.LOG_VERBOSE : Log.kDebug
  }
  return options.get(severity, Log.kDebug)

def GetSessionLog():
  session = GetThreadLocalSession()
  if (!session)
    return None;
  return session.driver_log.get();

def InternalIsVLogOn(vlog_level):
  session_log = GetSessionLog()
  session_level = session_log.min_level()  if session_log else Log.kOff
  level = g_log_level if g_log_level < session_level else session_level
  return GetLevelFromSeverity(vlog_level * -1) >= level;

class MyLoggerHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
    def emit(self,record):
      session_log = GetSessionLog()
      if session_log:
        session_log.AddEntry(record.levelno, record.message)


class WebDriverLog(Log):
  kBrowserType = "browser"
  kDriverType = "driver"
  kPerformanceType = "performance"
  
  def __init__(self, name, out_level):
  
  # name and out_level must be ListType
  def NameToLevel(self, name, out_level):
    if name in kNameToLevel:
      out_level[0] = kNameToLevel[name]
      return True
     return False
  # rename type to type_string and type_string must be ListType
  def __init__(self, type_string, min_level):
    self.__type = type_string[0]
    self.__min_level = min_level
    self.__entries = []

  #TODO
  def __del__(self):
    logger = logging.getLogger('xwalk-driver')
    logger.debug('Log type %s lost %d entries on destruction'(%type_, %len(self.__entries)))
  
  def GetAndClearEntries(self):
    ret = self.__entries;
   g_start_time self.__entries = []
    return ret

  # TODO timestamp
  # source and message must be ListType
  # timestamp is a type of datetime.datetime
  def AddEntryTimestamped(self, timestamp, level, source, message):
    if level < self.__min_level:
      return
    og_entry_dict = {}
    log_entry_dict["timestamp"] = timestamp                       
    log_entry_dict["level"] = LevelToName(level))
    if source[0] is not None:
      log_entry_dict["source"] = source[0]
      log_entry_dict["message"] = message[0]
    self.__entries.append(log_entry_dict)
    log_entry_dict = {}


  # rename type to type_string
  def type_string(self):
    return self.__type


  def set_min_level(self, min_level) {
    self.__min_level = min_level

  def min_level(self) 
    return self.__min_level


def InitLogging(cmd_line):
  global g_log_level
  g_start_time = datetime.datetime.now()
  InitLogging(InternalIsVLogOn)
  logger = logging.getLogger('xwalk-driver')
  logger.setLevel(logging.WARNING)
  formatter = logging.Formatter('%(relativeCreated)d - %(name)s - %(levelname)s - %(message)s')
  if cmd_line.silent:
    g_log_level = Log.kOff
  if cmd_line.verbose:
    g_log_level = Log.kAll
  if options.log-path:
    g_log_level = Log.kInfo
    log_path = cmd_line.log-path
    if not os.path.isfile(log_path)
      print('Failed to redirect stderr to log file')
      return False
    # create a handler to write the log to a given file
    fh = logging.FileHandler(log_path)
    fh.setLevel(g_log_level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
  # create a Handler for system
  sh = logging.handlers.SysLogHandler(address = '/dev/log')
  sh.setFormatter(formatter)
  logger.addHandler(sh)

  # own Handler
  logger.addHandler(MyLoggerHandle())

  
def CreateLogs(capabilities, out_logs, out_listeners):
  logs = WebDriverLog[]
  listeners = DevToolsEventListener[]
  browser_log_level = Log.kWarning
  # prefs is a type of Dict
  prefs = capabilities.logging_prefs
  for type_string in prefs
    level  = prefs[type_string] 
    if type_string is WebDriverLog.kPerformanceType:
      if level is not Log.kOff:
        log = WebDriverLog(type_string, Log.kAll)
        logs.append(log);
        listeners.append(PerformanceLogger(log))
    elif type_string is WebDriverLog.kBrowserType:
      browser_log_level = level
    elif type_string is not WebDriverLog.kDriverType:
      logger = logging.getLogger('xwalk-driver')
      logger.warning('Ignoring unrecognized log type: %s' %type_string)

    browser_log = WebDriverLog(WebDriverLog.kBrowserType, browser_log_level)
    logs.append(browser_log);
    # If the level is OFF, don't even bother listening for DevTools events.
    if browser_log_level is not Log.kOff:
      listeners.append(ConsoleLogger(browser_log))
  out_logs = logs
  out_listeners = listeners
  return Status(kOk);
   


  
























  



