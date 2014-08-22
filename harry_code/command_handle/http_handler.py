#!/usr/bin/python

# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import random
import sys
import BaseHTTPServer
import urlparse
import re
import json
import SocketServer
# xwalkdriver package
from commands_internal import *
from global_instance import webdriver_global
from http_error_code import *
from http_request_regx_table import HttpRequestRegx
from command_mapping import CommandMapping
from status import StatusCode
from status import Status


# command is one of CommandMap
def MatchCommand(request_method, request_path, command, session_id, out_params):
  if(request_method != command[0]):
    return False
  path_all = command[1]
  path_parts = path_all.split('/')
  request_parts = request_path.split('/')

  if len(path_parts) != len(request_parts):
    return False
  for i in range(len(request_parts))
    if(path_parts[i][0] == '$'):
      name = path_parts[i]
      if name[1:] == "sessionId":
        session_id[0] = request_parts[i]
      else:
        params[name[1:], request_parts[i]]
    elif request_parts[i] != path_parts[i]:
      return False
  out_params.update(params)
  return True
   
  


class XwalkHttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  global webdriver_global

  kLocalStorage = "localStorage"
  kSessionStorage = "sessionStorage"
  kShutdownPath = "shutdown"

  kNewSessionPathPattern = "session"

  def quitFunction():
    self.server_close()

  def PrepareResponseHelper(self, trimmed_path, status, value, session_id):
    if status.code() == StatusCode.kUnknownCommand:
      response = {"code": HTTP_NOT_IMPLEMENTED, 
                  "headers": [["", ""],]
                  "body": "unimplemented command: " + trimmed_path}
      return response

    if trimmed_path == XwalkHttpHandler.kNewSessionPathPattern and status.IsOk():
      """
      Creating a session involves a HTTP request to /session, which is
      supposed to redirect to /session/:sessionId, which returns the
      session info.
      """
      response = {"code": HTTP_SEE_OTHER,
                  "headers":[["Location", webdriver_global.url_base_ + "session/" + session_id],], 
                  "body": "unimplemented command: " + trimmed_path}
      return response
    elif status.IsError():
      Status full_status = status
      full_status.addDetails(
        "Driver info: xwalkdriver=" + kXwalkDriverVersion +
        " ,platform=" + os.uname()[0] + "," + os.umane()[2] + 
        "," + os.uname()[-1])
      value = {"message": full_status.message()}

    if not value:
      value = {}
  
    body_params = {}
    body_params["status"] = status.code()
    body_params['value'] = value
    body_params["sessionId"] = session_id

    response = {"code": HTTP_OK,
                "headers": [["Content-Type", "application/json; charset=utf-8"],], 
                "body": body_params}
    return response


  def PrepareResponse(self, trimmed_path, send_response_func, status, value, session_id):
    response = {}
    response =
      PrepareResponseHelper(trimmed_path, status, value, session_id)

    send_response_func(response)
    if trimmed_path == XwalkHttpHandler.kShutdownPath:
      self.quitFunction()

  """ parser JSON wire Http protocol url from selenium, aka, it 
  parse the detailed data format relative with json request. 
  for example if xwalkdriver receives a post request(apply for create new session) from selenium, 
  "POST" + "/session" + "...{"sessionId":null,"desiredCapbilities":{'xwalkOptions': {'androidPackage': 'org.xwalk.simple',
  'androidActivity': '.simpleActivity',}}}..." it parse the second part, and then extract the last part
  """
  """ return "STATUS" "REQUEST" "CONTENT" "REQUEST PARAMS" """
  def ParseRequestFromSelenium(self):
    flag = 0
    for name, command_map in HttpRequestRegx.PatternTable.items():
      session_id = []
      params = {}
      if (MatchCommand(self.command, self.path, command_map, session_id, params)):
        flag = 1
        break
    if !flag:
      return(Status(StatusCode.kError), name, None, None, None)
    varLen = int(self.headers['Content-Length'])
    if varLen:
      # if content exists
      content = self.rfile.read(varLen)
      params.update(content)
    return (Status(StatusCode.kOk), name, v[2], session_id[0], params)


  def sendResponse(self, response):
    self.send_response(response["code"])
    for header in response["headers"]:
      self.send_header(header[0], header[1])          
    self.end_headers()
    self.wfile.write(json.dumps(response['body'])

    
  """ reference on PatternTable to trigger specific request to devtool s and collect 
  right response from devtool, finally pack the right parameters and pack them into  
  "HttpServerResponseInfo" in format of Dictionary.
  For detailed, pls reference on "http_ser_response.py" """
  def RequestHandler(self):
    HttpServerResponseInfo = {}
    response_task = Task(PrepareResponse, [trimmed_path, self.sendResponse])
    (status, name, command, session_id, params) = self.ParseRequestFromSelenium()
    # check if parse request status
    if status.IsError():
      print "Failed to Parse Request From Selenium" 
      return False
    command.SetSessionId([session_id])
    command.SetParams(params)
    command.SetCommandName(name)
    # set a event then switch to the child thread
    command.run()
    session_id = command.session_id[0]
    response = command.value
    status = command.status
    Response()
      # only 2 type: "status" and "newSession"
      HttpServerResponseInfo = CommandMapping.WrapCommand[request](content, params[0], response_task)
    return

  def do_POST(self):
    self.RequestHandler()
    return 
   
  def do_GET(self):
    self.RequestHandler()
    return 



class ThreadedHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
  """Handle requests in a seperate thread."""









