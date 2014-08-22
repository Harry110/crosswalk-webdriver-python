# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from command import Command
import re
from allocate_commands import *
class RequestCommand()
class ExecuteSessionCommand():
class HttpRequestRegx():
class ExecuteWindowCommand():
  ''' HttpRequestRegx class is a regular expression table, used for xwalkdriver parsing 
    the Json wired http protocols request from selenium, for the regular expression
    table is not complished, if you find some rules are not in the following table,
    just achieve them yourself. Good luck! '''
  PatternTable = {
    "CreateSession" : ['POST', '/session', RequestCommand(ExecuteCreateSession)],
    "GetSessionCapabilities" : ['GET', "session/:sessionId", ExecuteSessionCommand(ExecuteGetSessionCapabilities)],
    "Quit" : ['DELET', 'session/:sessionId', ]
    Command.STATUS: ('GET', '/status', ),
    Command.NEW_SESSION: ('POST', '/session'),
    # Get Capabilities example
    Command.GET_SESSION: ['GET', 'session/$sessionId', ExecuteSessionCommand(ExecuteGetSessionCapabilities)],
    Command.GET_ALL_SESSIONS: ('GET', '/sessions'),
    Command.QUIT: ('DELETE', '/session/$sessionId'),
    Command.GET_CURRENT_WINDOW_HANDLE:
        ('GET', '/session/$sessionId/window_handle'),
    Command.GET_WINDOW_HANDLES:
        ('GET', '/session/$sessionId/window_handles'),
    Command.GET: ('POST', '/session/$sessionId/url'),
    Command.GO_FORWARD: ('POST', '/session/$sessionId/forward'),
    Command.GO_BACK: ('POST', '/session/$sessionId/back'),
    Command.REFRESH: ('POST', '/session/$sessionId/refresh'),
    Command.EXECUTE_SCRIPT: ('POST', '/session//,e/execute'),
    Command.GET_CURRENT_URL: ('GET', '/session/$sessionId/url'),
    Command.GET_TITLE: ('GET', '/session/$sessionId/title'),
    Command.GET_PAGE_SOURCE: ('GET', '/session/$sessionId/source'),
    Command.SCREENSHOT: ('GET', '/session/$sessionId/screenshot'),
    Command.FIND_ELEMENT: ('POST', '/session/$sessionId/element'),
    Command.FIND_ELEMENTS: ('POST', '/session/$sessionId/elements'),
    Command.GET_ACTIVE_ELEMENT:
    ('POST', '/session/$sessionId/element/active'),
    Command.FIND_CHILD_ELEMENT:
        ('POST', '/session/$sessionId/element/$id/element'),
    Command.FIND_CHILD_ELEMENTS:
        ('POST', '/session/$sessionId/element/$id/elements'),
    #example
    Command.CLICK_ELEMENT: ('POST', '/session/$sessionId/element/$id/click',  ExecuteSElementCommand(ExecuteClickElement)),
    Command.CLEAR_ELEMENT: ('POST', '/session/$sessionId/element/$id/clear'),
    Command.SUBMIT_ELEMENT: ('POST', '/session/$sessionId/element/$id/submit'),
    Command.GET_ELEMENT_TEXT: ('GET', '/session/$sessionId/element/$id/text'),
    Command.SEND_KEYS_TO_ELEMENT:
        ('POST', '/session/$sessionId/element/$id/value'),
    Command.SEND_KEYS_TO_ACTIVE_ELEMENT:
        ('POST', '/session/$sessionId/keys'),
    Command.UPLOAD_FILE: ('POST', "/session/$sessionId/file"),
    Command.GET_ELEMENT_VALUE:
        ('GET', '/session/$sessionId/element/$id/value'),
    Command.GET_ELEMENT_TAG_NAME:
        ('GET', '/session/$sessionId/element/$id/name'),
    Command.IS_ELEMENT_SELECTED:
        ('GET', '/session/$sessionId/element/$id/selected'),
    Command.SET_ELEMENT_SELECTED:
        ('POST', '/session/$sessionId/element/$id/selected'),
    Command.IS_ELEMENT_ENABLED:
        ('GET', '/session/$sessionId/element/$id/enabled'),
    Command.IS_ELEMENT_DISPLAYED:
        ('GET', '/session/$sessionId/element/$id/displayed'),
    Command.GET_ELEMENT_LOCATION:
        ('GET', '/session/$sessionId/element/$id/location'),
    Command.GET_ELEMENT_LOCATION_ONCE_SCROLLED_INTO_VIEW:
          ('GET', '/session/$sessionId/element/$id/location_in_view'),
    Command.GET_ELEMENT_SIZE:
        ('GET', '/session/$sessionId/element/$id/size'),
    Command.GET_ELEMENT_ATTRIBUTE:
        ('GET', '/session/$sessionId/element/$id/attribute/$name'),
    Command.ELEMENT_EQUALS:
        ('GET', '/session/$sessionId/element/$id/equals/$other'),
    Command.GET_ALL_COOKIES: ('GET', '/session/$sessionId/cookie'),
    Command.ADD_COOKIE: ('POST', '/session/$sessionId/cookie'),
    Command.DELETE_ALL_COOKIES:
        ('DELETE', '/session/$sessionId/cookie'),
    Command.DELETE_COOKIE:
        ('DELETE', '/session/$sessionId/cookie/$name'),
    Command.SWITCH_TO_FRAME: ('POST', '/session/$sessionId/frame'),
    Command.SWITCH_TO_PARENT_FRAME: ('POST', '/session/$sessionId/frame/parent'),
    Command.SWITCH_TO_WINDOW: ('POST', '/session/$sessionId/window'),
    Command.CLOSE: ('DELETE', '/session/$sessionId/window'),
    Command.GET_ELEMENT_VALUE_OF_CSS_PROPERTY:
        ('GET', '/session/$sessionId/element/$id/css/$propertyName'),
    Command.IMPLICIT_WAIT:
        ('POST', '/session/$sessionId/timeouts/implicit_wait'),
    Command.EXECUTE_ASYNC_SCRIPT: ('POST', '/session/$sessionId/execute_async'),
    Command.SET_SCRIPT_TIMEOUT:
        ('POST', '/session/$sessionId/timeouts/async_script'),
    Command.SET_TIMEOUTS:
        ('POST', '/session/$sessionId/timeouts'),
    Command.DISMISS_ALERT:
        ('POST', '/session/$sessionId/dismiss_alert'),
    Command.ACCEPT_ALERT:
        ('POST', '/session/$sessionId/accept_alert'),
    Command.SET_ALERT_VALUE:
        ('POST', '/session/$sessionId/alert_text'),
    Command.GET_ALERT_TEXT:
        ('GET', '/session/$sessionId/alert_text'),
    Command.CLICK:
        ('POST', '/session/$sessionId/click'),
    Command.DOUBLE_CLICK:
        ('POST', '/session/$sessionId/doubleclick'),
    Command.MOUSE_DOWN:
        ('POST', '/session/$sessionId/buttondown'),
    Command.MOUSE_UP:
          ('POST', '/session/$sessionId/buttonup'),
    Command.MOVE_TO:
        ('POST', '/session/$sessionId/moveto'),
    Command.GET_WINDOW_SIZE:
        ('GET', '/session/$sessionId/window/$windowHandle/size'),
    Command.SET_WINDOW_SIZE:
        ('POST', '/session/$sessionId/window/$windowHandle/size'),
    Command.GET_WINDOW_POSITION:
        ('GET', '/session/$sessionId/window/$windowHandle/position'),
    Command.SET_WINDOW_POSITION:
        ('POST', '/session/$sessionId/window/$windowHandle/position'),
    Command.MAXIMIZE_WINDOW:
        ('POST', '/session/$sessionId/window/$windowHandle/maximize'),
    Command.SET_SCREEN_ORIENTATION:
        ('POST', '/session/$sessionId/orientation'),
    Command.GET_SCREEN_ORIENTATION:
        ('GET', '/session/$sessionId/orientation'),
    Command.SINGLE_TAP:
        ('POST', '/session/$sessionId/touch/click'),
    Command.TOUCH_DOWN:
        ('POST', '/session/$sessionId/touch/down'),
    Command.TOUCH_UP:
        ('POST', '/session/$sessionId/touch/up'),
    Command.TOUCH_MOVE:
        ('POST', '/session/$sessionId/touch/move'),
    Command.TOUCH_SCROLL:
        ('POST', '/session/$sessionId/touch/scroll'),
    Command.DOUBLE_TAP:
        ('POST', '/session/$sessionId/touch/doubleclick'),
    Command.LONG_PRESS:
        ('POST', '/session/$sessionId/touch/longclick'),
    Command.FLICK:
        ('POST', '/session/$sessionId/touch/flick'),
    Command.EXECUTE_SQL:
        ('POST', '/session/$sessionId/execute_sql'),
    Command.GET_LOCATION:
        ('GET', '/session/$sessionId/location'),
    Command.SET_LOCATION:
        ('POST', '/session/$sessionId/location'),
    Command.GET_APP_CACHE:
        ('GET', '/session/$sessionId/application_cache'),
    Command.GET_APP_CACHE_STATUS:
        ('GET', '/session/$sessionId/application_cache/status'),
    Command.CLEAR_APP_CACHE:
        ('DELETE', '/session/$sessionId/application_cache/clear'),
    Command.GET_NETWORK_CONNECTION:
        ('GET', '/session/$sessionId/network_connection'),
    Command.SET_NETWORK_CONNECTION:
        ('POST', '/session/$sessionId/network_connection'),
    Command.GET_LOCAL_STORAGE_ITEM:
        ('GET', '/session/$sessionId/local_storage/key/$key'),
    Command.REMOVE_LOCAL_STORAGE_ITEM:
        ('DELETE', '/session/$sessionId/local_storage/key/$key'),
    Command.GET_LOCAL_STORAGE_KEYS:
        ('GET', '/session/$sessionId/local_storage'),
    Command.SET_LOCAL_STORAGE_ITEM:
        ('POST', '/session/$sessionId/local_storage'),
    Command.CLEAR_LOCAL_STORAGE:
        ('DELETE', '/session/$sessionId/local_storage'),
    Command.GET_LOCAL_STORAGE_SIZE:
        ('GET', '/session/$sessionId/local_storage/size'),
    Command.GET_SESSION_STORAGE_ITEM:
        ('GET', '/session/$sessionId/session_storage/key/$key'),
    Command.REMOVE_SESSION_STORAGE_ITEM:
        ('DELETE', '/session/$sessionId/session_storage/key/$key'),
    Command.GET_SESSION_STORAGE_KEYS:
        ('GET', '/session/$sessionId/session_storage'),
    Command.SET_SESSION_STORAGE_ITEM:
        ('POST', '/session/$sessionId/session_storage'),
    Command.CLEAR_SESSION_STORAGE:
        ('DELETE', '/session/$sessionId/session_storage'),
    Command.GET_SESSION_STORAGE_SIZE:
        ('GET', '/session/$sessionId/session_storage/size'),
    Command.GET_LOG:
        ('POST', '/session/$sessionId/log'),
    Command.GET_AVAILABLE_LOG_TYPES:
        ('GET', '/session/$sessionId/log/types'),
  }

if __name__ == "__main__":
  for k,v in HttpRequestRegx.PatternTable.items():
    print HttpRequestRegx.PatternTable[k][1]

