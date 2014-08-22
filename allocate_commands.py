
#for the session command that has session id
class RequestCommand():
  def __init__(self, request_fun):
    self.command = request_fun
    self.status = None
  def SetParams(self, params):
        self.params = params
    def SetSessionId(self, session_id):
        self.session_id = [session_id]
    def run(self):
        # self.status, self.session_id, self.params
        self.status = self.command(self.session_id, self.params, self.value)


class ExecuteSessionCommand():
  def __init__(self, session_command):
    self.command = session_command
    self.params = None
    self.session = []
    self.value = None
    self.status = None
  def SetParams(self, params):
    self.params = params
  def SetSessionId(self, session_id):
    self.session_id[0] = session_id
    self.session = session_map[session_id]
    self.thread = session_thread_map[session_id]
  def SetCommandName(self, name):
    self.name = name
  def run(self):
    sinal = threading.Event()
    threading.currentThread().threadEvent = sinal
    self.thread.postTask(self.command, self.session, self.params, self.value, sinal)
    sinal.wait()
    self.status = sinal.status


def PrepareWindowCommand(command, session, web_view, params, value):
  status = session.GetTargetWindow(web_view)
  if (status.IsError()):
    return status
  status = web_view.ConnectIfNecessary()
  if (status.IsError()):
    return status
  status = web_view.HandleReceivedEvents()
  if (status.IsError()):
    return status
  if (web_view.GetJavaScriptDialogManager().IsDialogOpen()):
    status = Status(kUnexpectedAlertOpen)
    return status
  nav_status = Status(kOk)
  for attemp in range(2):
    if (attempt == 1):
      if (status.code() == kNoSuchExecutionContext):
        # Switch to main frame and retry command if subframe no longer exists.
        session.SwitchToTopFrame()
      else:
        break
    nav_status = web_view.WaitForPendingNavigations(
        session.GetCurrentFrameId(), session.page_load_timeout, True)
    if (nav_status.IsError()):
      status = nav_status
      return status

def DealWindowCommand(command, session, web_view, params, value):
  nav_status = web_view.WaitForPendingNavigations(session.GetCurrentFrameId(), 
    session.page_load_timeout, True)
  if (status.IsOk() and nav_status.IsError() and nav_status.code() != kUnexpectedAlertOpen):
    status = nav_status
    return status
  if (status.code() == kUnexpectedAlertOpen):
    status = Status(kOk)
    return status
  
class ExecuteWindowCommand():
  def __init__(self, window_command):
    self.command = window_command
    self.params = None
    self.session = []
    self.value = None
    self.status = None
    self.web_view = None
  def SetParams(self, params):
    self.params = params
  def SetSessionId(self, session_id):
    self.session_id[0] = session_id
    self.session = session_map[session_id]
    self.thread = session_thread_map[session_id]
  def SetCommandName(self, name):
    self.name = name
  def run(self):
    sinal = threading.Event()
    threading.currentThread().threadEvent = sinal
    self.thread.postTask(PrepareWindowCommand, 
      self.session, self.web_view, self.params, self.value, sinal)
    sinalthreadEvent.wait()
    self.status = sinal.status
    if self.status.IsOk():
      self.thread.postTask(self.command, 
        self.session, self.web_view, self.params, self.value, sinal)
      sinal.wait()
      self.status = sinal.status
      if self.status.IsOk():
        self.thread.postTask(DealWindowCommand, 
          self.session, self.web_view, self.params, self.value, sinal)
        sinal.wait()
        self.status = sinal.status
        
  
class ExcuteElementCommand():
  def __init__(self, window_command):
    self.command = window_command
    self.params = None
    self.session = None
    self.session_id = []
    self.value = None
    self.status = None
    self.web_view = None
  def SetParams(self, params):
    self.params = params
  def SetSessionId(self, session_id):
    self.session_id[0] = session_id
    self.session = session_map[session_id]
    self.thread = session_thread_map[session_id]
  def SetCommandName(self, name):
    self.name = name
  def run(self):
    sinal = threading.Event()
    threading.currentThread().threadEvent = sinal
    self.thread.postTask(PrepareWindowCommand, self.status, 
      self.session, self.web_view, self.params, self.value, sinal)
    sinal.wait()
    if self.status.IsOk():
      self.element = self.params.get('id', '')
      self.element = self.params.get('element', '')
      if self.element:
        self.thread.postTask(self.command, self.status, 
          self.session, self.web_view, self.element, self.params, self.value, sinal)
        sinal.wait()
      else:
        self.status = Status(kUnknownError, "element identifier must be a string")
      if self.status.IsOk():
        self.thread.postTask(DealWindowCommand, self.status, 
          self.session, self.web_view, self.params, self.value, sinal)
        sinal.wait()




