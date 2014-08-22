import json
import time
import DevToolsClient from devtools_client

class InspectorMessageType(object):
  kEventMessageType = 0
  kCommandResponseMessageType = 1

class InspectorEvent(object):
  def __init__(self):
    self.method = None
    self.params = None

class InspectorCommandResponse(object):
  def __init__(self):
    self.id = None
    self.error = None
    self.result = None

kInspectorContextError = "Execution context with given id not found."

def ParseInspectorError(error_json):
  error = json.loads(error_json)
  error_dict = dict(error)
  if(!error or !error_dict):
    return Status(kUnknownError, "inspector error with no error message")
  error_message = error_dict.get('message')
  if error_message is kInspectorContextError:
      return Status(kNoSuchExecutionContext)
  return Status(kUnknownError, "unhandled inspector error: " + error_json)


def ConditionIsMe(): 
  return (Status(kOk), true)

class DevToolsClientImpl(DevToolsClient):
  def ScopedIncrementer():
    self.__stack_count += 1

  def ScopedDecrementer():
    self.__stack_count -= 1

  def __init__(factory, url, id, frontend_closer_func, parser_func):
    self.__socket = factory.Run()
    self.__url = url
    self.__crashed = false
    self.__id = id
    self.__frontend_closer_func = frontend_closer_func
    if parser_func:
      self.__parser_func = parser_func
    else:
      self.__parser_func = ParseInspectorMessage
    self.__unnotified_event = NULL
    self.__next_id = 1
    self.__stack_count = 0

    self.__listeners = []
    self.__unnotified_connect_listeners = []
    self.__unnotified_event_listeners = []
    self.__unnotified_event = None
    self.__unnotified_cmd_response_listeners = []
    self.__unnotified_cmd_response_info = None
    self.__response_info_map = None

  class ResponseState:
    kWaiting = 0
    """ The client is waiting for the response. """
    kBlocked = 1
    """ The command response will not be received because it is blocked by an
        alert that the command triggered. """
    kIgnored = 2
    """ The client no longer cares about the response. """
    kReceived = 3
    """ The response has been received. """

  class ResponseInfo:
    def __init__(method):
      self.method = method

    state = None
    response = None

  def SetParserFuncForTesting(parser_func):
    self.__parser_func = parser_func

  """ Overridden from DevToolsClient: """
  def GetId():
    return self.__id

  def WasCrashed():
    return self.__crushed

  def ConnectIfNecessary():
    if self.__stack_count:
      return Status(kUnknownError, "cannot connect when nested")
    if self.__socket->IsConnected():
      return Status(kOk)
              
    if !self.__socket->Connect(self.__url):
      """ Try to close devtools frontend and then reconnect. """
      Status status = self.__frontend_closer_func()
      if status.IsError():
        return status
      if !self.__socket->Connect(url_):
        return Status(kDisconnected, "unable to connect to renderer")

                                                          
    self.__unnotified_connect_listeners = self.__listeners
    del self.__unnotified_event_listeners
    del.__response_info_map
    """TODO (wyh)                                                            
        Notify all listeners of the new connection. Do this now so that any errors
        that occur are reported now instead of later during some unrelated call.
        Also gives listeners a chance to send commands before other clients.
    """
    return EnsureListenersNotifiedOfConnect();
    
  def SendCommand(method, params):
    status, result = SendCommandInternal(method, params)
    return status

  def SendCommandAndGetResult(method, params:
    status, intermediate_result = SendCommandInternal(method, params)
    if status.IsError():
      return (status, intermediate_result)
    if !intermediate_result:
      return (Status(kUnknownError, "inspector response missing result"), None)
    return (status, intermediate_result)

  def AddListener(listener):
    self.__listeners.append(listener)

  def HandleEventsUntil(conditional_func, timeout):
    if !self.__socket->IsConnected():
      return Status(kDisconnected, "not connected to DevTools")

    deadline = time.clock() + timeout
    next_message_timeout = timeout
    while true: {
      if !self.__socket->HasNextMessage():
        bool is_condition_met = false
        status, is_condition_met = conditional_func()
        if status.IsError():
          return status
        if is_condition_met:
          return Status(kOk)

      Status status = ProcessNextMessage(-1, next_message_timeout)
      if status.IsError():
        return status
      next_message_timeout = deadline - time.clock()

  def  HandleReceivedEvents():
    return HandleEventsUntil(ConditionIsMet), 0);

  def SendCommandInternal(method, params):
    if !self.__socket->IsConnected():
      return (Status(kDisconnected, "not connected to DevTools"), result)
    int command_id = self.__next_id
    self.__next_id += 1;
    command = {'id': command_id, 'method': method, 'params': json.dump(params)}
    """ TODO (wyh)
    if (IsVLogOn(1)) {
      VLOG(1) << "DEVTOOLS COMMAND " << method << " (id=" << command_id << ") "
                                    << FormatValueForDisplay(params);
    }
    """
    if !self.__socket->Send(json.dump(message):
      return (Status(kDisconnected, "unable to send message to renderer"), result)

    response_info = ResponseInfo(method)
    self.__response_info_map[command_id] = response_info;
    while (response_info.state == kWaiting:
      status = ProcessNextMessage(command_id, 600)
      if status.IsError():
        if response_info->state == kReceived:
          del self.__response_info_map[command_id]
          return (status, None)
    if response_info.state == kBlocked:
      response_info.state = kIgnored
      return (Status(kUnexpectedAlertOpen), None)

    """ TODO(wyh) CHECK_EQ(response_info->state, kReceived); """
    
    response = response_info.response;
    if response.result == None:
      return (ParseInspectorError(response.error), None)
    return (Status(kOk), response.result)

  def ProcessNextMessage(expected_id, timeout):
    ScopedIncrementer()
    try:
      status = EnsureListenersNotifiedOfConnect()
      if status.IsError():
        return status
      status = EnsureListenersNotifiedOfEvent()
      if status.IsError():
        return status
      status = EnsureListenersNotifiedOfCommandResponse()
      if status.IsError():
        return status

      """ The command response may have already been received or blocked while
           notifying listeners. """
      if expected_id != -1 and self.__response_info_map[expected_id].state != kWaiting:
        return Status(kOk)

      if (crashed_)
        return Status(kTabCrashed)

      self.__socket.settimeout(timeout)
      message = self.__socket.recv()

      type = InspectorMessageType()
      event = InspectorEvent()
      response = InspectorCommandResponse()
      bool re;
      type, event, response, re = self.__parser_func(message, expected_id)
      if !re:
        """ TODO(wyh)
        LOG(ERROR) << "Bad inspector message: " << message;
        """
        return Status(kUnknownError, "bad inspector message: " + message)
                            
      if type == kEventMessageType:
        return ProcessEvent(event)
      """CHECK_EQ(type, internal::kCommandResponseMessageType);"""
      return ProcessCommandResponse(response) 

    except websocket.WebSocketException:
      """ LOG(ERROR) << err; """
      return Status(kDisconnected, websocket.WebSocketException)
    except:
      pass
    finally:
      ScopedDecrementer()

  def ProcessEvent(event):
    """ TODO(wyh)
    if (IsVLogOn(1)) {
      VLOG(1) << "DEVTOOLS EVENT " << event.method << " "
              << FormatValueForDisplay(*event.params);
    }
    """
    self.__unnotified_event_listeners = self.__listeners
    self.__unnotified_event = event
    status = EnsureListenersNotifiedOfEvent()
    self.__unnotified_event_ = NULL

    if status.IsError():
      return status
    if event.method == "Inspector.detached":
      return Status(kDisconnected, "received Inspector.detached event")
    if event.method == "Inspector.targetCrashed":
      self.__crashed = true
      return Status(kTabCrashed)
    if event.method == "Page.javascriptDialogOpening":
      """
      A command may have opened the dialog, which will block the response.
      To find out which one (if any), do a round trip with a simple command
      to the renderer and afterwards see if any of the commands still haven't
      received a response.
      This relies on the fact that DevTools commands are processed
      sequentially. This may break if any of the commands are asynchronous.
      If for some reason the round trip command fails, mark all the waiting
      commands as blocked and return the error. This is better than risking
      a hang.
      """
      max_id = self.__next_id
      enable_params = {"purpose": "detect if alert blocked any cmds"}
      Status enable_status = SendCommand("Inspector.enable", enable_params)
      for cur_id, response = self.__response_info_map:
	if cur_id > max_id:
	  continue;
	if response.state == kWaiting:
	  response.state = kBlocked
      if enable_status.IsError():
	return status
    return Status(kOk);

  def ProcessCommandResponse(response):
    response_info = self.__response_info_map[response.id]
    if !response_info:
      return Status(kUnknownError, "unexpected command response")

    """ TODO(why)
    if (IsVLogOn(1)) {
      std::string method, result;
      if (iter != response_info_map_.end())
	method = iter->second->method;
      if (response.result)
	result = FormatValueForDisplay(*response.result);
      else
	result = response.error;
      VLOG(1) << "DEVTOOLS RESPONSE " << method << " (id=" << response.id
	      << ") " << result;
    }
    """

    if response_info.state == kReceived:
      return Status(kUnknownError, "received multiple command responses")

    if response_info.state == kIgnored:
      del self.__response_info_map[response.id]
    else:
      response_info.state = kReceived
      response_info.response.id = response.id
      response_info.response.error = response.error
      if response.result:
	response_info.response.result = response.result

    if response.result:
      self.__unnotified_cmd_response_listeners = self.__listeners
      self.__unnotified_cmd_response_info = response_info
      status = EnsureListenersNotifiedOfCommandResponse()
      self.__unnotified_cmd_response_info = None
      if status.IsError():
	return status
    return Status(kOk)

  def EnsureListenersNotifiedOfCommandResponse():

  def EnsureListenersNotifiedOfConnect():
    index = 0
    for listener in self.__unnotified_connect_listeners:
      Status status = listener->OnConnected(self)
      if status.IsError():
        del self.__unnotified_connect_listeners[0:index]
        return status
      index = index + 1
    del self.__unnotified_connect_listeners[:]
    return Status(kOk)

  def EnsureListenersNotifiedOfEvent():
    index = 0
    for listener in self.__unnotified_event_listeners:
      status = listener.OnEvent(self, self.__unnotified_event.method,
                                self.__unnotified_event.params)
      if status.IsError():
        del self.__unnotified_event_listeners[0:index]
        return status
      index = index + 1

    del self.__unnotified_event_listeners[:]
    return Status(kOk);

  def EnsureListenersNotifiedOfCommandResponse():
    index = 0
    for listener in self.__unnotified_cmd_response_listeners:
      status = listener.OnCommandSuccess(self, self.__unnotified_cmd_response_info.method)
      if status.IsError():
        del self.__unnotified_cmd_response_listeners[0:index]
        return status
      index = index + 1
    return Status(kOk)


