#!/usr/bin/env python
import time
import json
class Log:
  kAll = 0
  kDebug = 10
  kInfo = 20
  kWarning = 30
  kError = 40
  kOff = 50
  def __init__(self):
    
  def AddEntry(level, message):
    AddEntry(level, "", message)
  def AddEntry(level, source, message):
    AddEntryTimestamped(time.asctime(), level, source, message);

g_is_vlog_on_func = None;

def TruncateString(data):
  kMaxLength = 200
  if len(data[0] > kMaxLength:
    data[0] = data[0][:kMaxLength-1]
    data[0][-3:] = '...'

def SmartDeepCopy(value):
  kMaxChildren = 20
  if type(value) is types.DictType:
    dict_copy = {}
    for key, child in value.items():
      if len(dict_copy) >= kMaxChildren - 1:
        dict_copy['~~~'] = '...'
        break
      dict_copy[key] = SmartDeepCopy(child)
    return dict_copy
  elif type(value) is types.ListType:
    list_copy = [];
    for child in value:
      if len(list_copy) >= kMaxChildren - 1:
        list_copy.append('...')
        break
      list_copy.append(SmartDeepCopy(child))
    return list_copy
  elif type(value) is types.StringType:
    return value
  return value

def InitLogging(is_vlog_on_func):
  global g_is_vlog_on_func
  g_is_vlog_on_func = is_vlog_on_func

def IsVLogOn(vlog_level):
  global g_is_vlog_on_func
  if (!g_is_vlog_on_func):
    return False
  return g_is_vlog_on_func(vlog_level);

def PrettyPrintValue(value):
  return json.dumps(value)

def FormatValueForDisplay(value):
  copy = SmartDeepCopy(value)
  return PrettyPrintValue(copy)

def FormatJsonForDisplay(json):
  return json.loads(json)






















     

    
