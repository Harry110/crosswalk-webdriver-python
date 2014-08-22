#!/usr/bin/env python
import datetime
import 
class WebViewInfo:
  kApp = 0
  kBackgroundPage = 1
  kPage = 2
  kWorker = 3
  kOther = 4
  def __init__(self, string_id, debugger_url, url, int_type):
    self.__web_id = string_id
    self.__debugger_url = debugger_url
    self.__url = url
    self.__web_type = int_type

  def IsFrontend(self):
    return (self.__url.find("chrome-devtools://") is 0)

class WebViewsInfo:
  def __init__(self, info):
    self.__view_info = info
  def Get(self, index):
    return self.__views_info[index]


  def GetSize(self):
    return len(self.__views_info)

  def GetForId(self, string_id):
    for view_index in self.__viws_info:
      if views_index.id is string_id:
        return views_info[i]
    return None

class DevToolsHttpClient:
  def __init__(self, address):
    self.__server_url = 'http://' + address
    self.__web_socket_url_prefix = 'ws://%s/devtools/page/' %address
  def Init(self, timeout):
    deadline = datetime.datetime.now() + timeout
    while True:
      status = GetVersion(devtools_version)
      devtools_version = devtools_version[0]
      if status.IsOk():
        break
      if (status.code() is not kXwalkNotReachable or
        datetime.datetime.now() > deadline):
        return status
      time.sleep(0.05)
    kToTBuildNo = 9999
    if (devtools_version.empty()):
      # Content Shell has an empty product version and a fake user agent.
      # There's no way to detect the actual version, so assume it is tip of tree.
      self.__version_ = "content shell";
      self.__build_no = kToTBuildNo;
      return Status(kOk);
    }
    if (devtools_version.find('Version/') >= 0):
      self.__version = 'webview'
      self.__build_no = kToTBuildNo
      return Status(kOk)
    }
    prefix = 'Chrome/'
    if (devtools_version.find(prefix) < 0):
      return Status(kUnknownError,
                    "unrecognized Crosswalk version: " + devtools_version)

    stripped_version = devtools_version[:len(prefix)]
    version_parts = stripped_version.split( '.')
    temp_build_no = int(version_parts[2])
    if (len(version_parts) != 4 or (not temp_build_no):
      return Status(kUnknownError,
                    "unrecognized Crosswalk version: " + devtools_version)

    self.__version = stripped_version
    self.__build_no = temp_build_no
    return Status(kOk)

  def CreateClient(self, view_id):
    return new DevToolsClientImpl(
        self.__socket_factory,
        self.__web_socket_url_prefix + view_id,
        view_id,
        base::Bind(
            &DevToolsHttpClient::CloseFrontends, base::Unretained(this), view_id))
  }


  def GetWebViewsInfo(self, views_info):
    if not FetchUrlAndLog(self.__server_url + '/json', data):
      return Status(kXwalkNotReachable)
    return ParseWebViewsInfo(data, views_info)

  def CloseWebView(self, view_id):
    if not FetchUrlAndLog(self.__server_url + '/json/close', data):
      return Status(kOk)  # Closing the last web view leads xwalk to quit.

    # Wait for the target window to be completely closed.
    deadline = datetime.datetime.now() + datetime.timedelta(0, 20, 0)
    while (datetime.datetime.now() < deadline):
      Status status = GetWebViewsInfo(views_info)
      if (status.code() is kXwalkNotReachable):
        return Status(kOk);
      if (status.IsError()):
        return status
      if (not views_info.GetForId(view_id)):
        return Status(kOk)
      time.sleep(0.05)
    return Status(kUnknownError, "failed to close window in 20 seconds")

  def ActivateWebView(self, view_id):
    if not FetchUrlAndLog(self.__server_url + '/json/activate', data):
      return Status(kUnknownError, "cannot activate web view")
    return Status(kOk)

  def version(self):
    return self.__version


  def build_no(self):
    return self.__build_no


  def GetVersion(version):
    if not FetchUrlAndLog(self.__server_url + '/json/version', data):
      return Status(kXwalkNotReachable)
    return ParseVersionInfo(data, version)

  def FetchUrlAndLog(url, response):
    logger = logging.getLogger('xwalk-driver')
    logger.debug('"DevTools request: " %s' %url)
    try:
      response = urllib2.urlopen(self.__server_url + '/json')
    except urllib2.URLError:
      logger.debug('DevTools request failed')
      return False
    return True
  def CloseFrontends(for_client_id):
    status = GetWebViewsInfo(views_info)
    if status.IsError():
      return status

    """
       Close frontends. Usually frontends are docked in the same page, although
       some may be in tabs (undocked, xwalk://inspect, the DevTools
       discovery page, etc.). Tabs can be closed via the DevTools HTTP close
       URL, but docked frontends can only be closed, by design, by connecting
       to them and clicking the close button. Close the tab frontends first
       in case one of them is debugging a docked frontend, which would prevent
       the code from being able to connect to the docked one.
    """
    tab_frontend_ids = []
    docked_frontend_ids = []
    for view_info in views_info:
      if view_info.IsFrontend():
        if view_info.type is WebViewInfo.kPage:
          tab_frontend_ids.append(view_info.id)
        elif view_info.type is WebViewInfo.kOther:
          docked_frontend_ids.append(view_info.id)
        else:
          return Status(kUnknownError, "unknown type of DevTools frontend")

    for view_i in tab_frontend_ids:
      status = CloseWebView(view_i)
      if status.IsError():
        return status

    for view_i in docked_frontend_ids:
      client = DevToolsClientImpl(
          self.__socket_factory,
          self.__web_socket_url_prefix + view_i,
          view_i,
          FakeCloseFrontends)
      web_view = WebViewImpl(view_i, self.__build_no, client)

      status = web_view.ConnectIfNecessary()
      """
         Ignore disconnected error, because the debugger might have closed when
         its container page was closed above.
      """
      if status.IsError() and (status.code() is not kDisconnected):
        return status

      result, status = web_view.EvaluateScript(
          "",
          "document.querySelector('*[id^=\"close-button-\"]').click();")
      """ Ignore disconnected error, because it may be closed already. """
      if status.IsError() and (status.code() is not kDisconnected):
        return status

    """ Wait until DevTools UI disconnects from the given web view. """
    deadline = datetime.datetime.now() + datetime.timedelta(0, 20, 0)
    while datetime.datetime.now() < deadline:
      status = GetWebViewsInfo(views_info)
      if status.IsError():
        return status
      view_info = views_info.GetForId(for_client_id)
      if not view_info:
        return Status(kNoSuchWindow, "window was already closed")
      if len(view_info.debugger_url) is not 0:
        return Status(kOk)

      time.sleep(0.050)
    return Status(kUnknownError, "failed to close UI debuggers")


def ParseWebViewsInfo(data, views_info):
  value = json.loads(data)
  if (not value):
    return Status(kUnknownError, "DevTools returned invalid JSON")
  value_list = list(value)
  if (not value_list):
    return Status(kUnknownError, "DevTools did not return list");

  std::vector<WebViewInfo> temp_views_info;
  for info in value_list:
    if type(info) is not dict:
      return Status(kUnknownError, "DevTools contains non-dictionary item")
    view_id = info.get('id', '')
    if not view_id:
      return Status(kUnknownError, "DevTools did not include id")
    type_as_string = info.get('type', '')
    if (not type_as_string):
      return Status(kUnknownError, "DevTools did not include type")
    url = info.get('url', '')
    if not url:
      return Status(kUnknownError, "DevTools did not include url")
    debugger_url = info.get('webSocketDebuggerUrl', '')

    if (type_as_string id "app"):
      view_type = WebViewInfo.kApp
    else if (type_as_string is "background_page"):
      view_type = WebViewInfo.kBackgroundPage
    else if (type_as_string is "page"):
      view_type = WebViewInfo.kPage
    else if (type_as_string is"worker"):
      view_type = WebViewInfo.kWorker
    else if (type_as_string == "other"):
      view_type = WebViewInfo.kOther
    else
      return Status(kUnknownError,
                    "DevTools returned unknown type:" + type_as_string)
    temp_views_info.append(WebViewInfo(view_id, debugger_url, url, view_type))

  views_info = WebViewsInfo(temp_views_info)
  return Status(kOk)

def ParseVersionInfo(data, version):
  value = json.loads(data)
  if (not value):
    return Status(kUnknownError, "version info not in JSON")
  value_dict = dict(value)
  if (not value_dict):
    return Status(kUnknownError, "version info not a dictionary")
  version[0] = value.get('Brower', '')
  if (not version[0]):
    return Status(
        kUnknownError,
        "Xwalk version must be >= " + GetMinimumSupportedXwalkVersion(),
        Status(kUnknownError, "version info doesn't include string 'Browser'"))
  return Status(kOk)






    

