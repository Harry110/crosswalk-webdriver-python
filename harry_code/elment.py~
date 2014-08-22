#!/usr/bin/env python
import datetime


def SendKeysToElement(session, web_view, element_id, key_list):
  is_displayed = [False]
  is_forused = [False]
  start_time = datetime.datetime.now() 
  while True:
    status = IsElementDisplayed(
        session, web_view, element_id, true, is_displayed)
    if status.IsError():
        return status
    if is_dispplayed:
      break
    status = IsElementFocused(session, web_view, element_id, is_focused)
    if status.IsError():
        return status
    if is_dispplayed:
      break    
    if (datetime.datetime.now() - start_time) > session.implicit_wait:
      return Status(kElementNotVisible)
    time.sleep(1)
  is_enable = False
  status = IsElementEnabled(session, web_view, element_id, is_enabled)
  if status.IsError():
    return status
  if not is_enabled
    return Status(kInvalidElementState)

  if not is_focused: 
    args = []
    args.append(CreateElement(element_id))
    result = []
    status = web_view.CallFunction(
        session.GetCurrentFrameId(), kFocusScript, args, result);
    if status.IsError():
      return status
  return SendKeysOnWindow(web_view, key_list, true, session.sticky_modifiers)

def ExecuteTouchSingleTapAtom(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(session.GetCurrentFrameId(),
      #TODO
      webdriver::atoms::asString(webdriver::atoms::TOUCH_SINGLE_TAP),
      args,
      value)

# value is a ListType
def ExecuteElementCommand(command, session, web_view, params, value):
  if (params.has_key('id') or (params.has_key('element'):
    element_id = params.get('id','')
    element_id = params.get('element', element_id)
    return command(session, web_view, [element_id], params, value)
  return Status(kUnknownError, "element identifier must be a string")



def ExecuteFindChildElement(interval_ms, session, web_view, element_id, params, value):
  return FindElement(
      interval_ms, true, element_id, session, web_view, params, value)


def ExecuteHoverOverElement(session, web_view, element_id, params, value):
  location = WebPoint()
  status = GetElementClickableLocation( session, web_view, element_id, location)
  if status.IsError():
    return status
  move_event = MouseEvent(kMovedMouseEventType, kNoneMouseButton, location.x, location.y,
      session.sticky_modifiers, 0);
  events = []
  events.append(move_event)
  status = web_view.DispatchMouseEvents(events, session.GetCurrentFrameId())
  if status.IsOk():
    session.mouse_position = location
  return status


def ExecuteClickElement(session, web_view, element_id, params, value):
  tag_name = []
  status = GetElementTagName(session, web_view, element_id[0], tag_name);
  if status.IsError():
    return status
  if tag_name is "option":
    is_toggleable = []
    status = IsOptionElementTogglable(
        session, web_view, element_id, is_toggleable);
    if status.IsError():
      return status
    if is_toggleable:
      return ToggleOptionElement(session, web_view, element_id[0])
    else:
      return SetOptionElementSelected(session, web_view, element_id[0], true);
  else:
    location = WebPoint()
    status = GetElementClickableLocation(
        session, web_view, element_id, location);
    if status.IsError():
      return status

    events = [];
    events.append(
        MouseEvent(kMovedMouseEventType, kNoneMouseButton,
                   location.x, location.y, session.sticky_modifiers, 0))
    events.append(
        MouseEvent(kPressedMouseEventType, kLeftMouseButton,
                   location.x, location.y, session.sticky_modifiers, 1))
    events.append(
        MouseEvent(kReleasedMouseEventType, kLeftMouseButton,
                   location.x, location.y, session.sticky_modifiers, 1))
    status =
        web_view->DispatchMouseEvents(events, session.GetCurrentFrameId())
    if status.IsOk():
      session.mouse_position = location
    return status

def ExecuteTouchSingleTap(session, web_view, element_id, params, value):
  # Fall back to javascript atom for pre-m30 Xwalk.
  if (session.xwalk.GetBuildNo() < 1576)
    return ExecuteTouchSingleTapAtom(
        session, web_view, element_id, params, value);

  location = WebPoint()
  Status status = GetElementClickableLocation(
      session, web_view, element_id, location)
  if (status.IsError()):
    return status

  events = []
  events.append(
      TouchEvent(kTouchStart, location.x, location.y))
  events.append(
      TouchEvent(kTouchEnd, location.x, location.y))
  return web_view.DispatchTouchEvents(events)


def ExecuteClearElement(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id[0]))
  result = []
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      webdriver::atoms::asString(webdriver::atoms::CLEAR),
      args, result);

def ExecuteSendKeysToElement(session, web_view, element_id, params, value):
  key_list = param.get('value', '')
  
  if key_list is None
    return Status(kUnknownError, "'value' must be a list");

  # ListType
  is_input = [False];
  status = IsElementAttributeEqualToIgnoreCase(
      session, web_view, element_id, "tagName", "input", is_input)
  if (status.IsError()):
    return status
  is_file = [False]
  status = IsElementAttributeEqualToIgnoreCase(
      session, web_view, element_id, "type", "file", is_file);
  if (status.IsError()):
    return status
  if (is_input and is_file): 
    # Compress array into a single string.
    for path_part in key_list:
      if not path_part:
        return Status(kUnknownError, "'value' is invalid")
      paths_string.append(path_part)


    # Separate the string into separate paths, delimited by '\n'.
    paths = paths_string.split('\n')
    multiple = [False];
    status = IsElementAttributeEqualToIgnoreCase(
        session, web_view, element_id, "multiple", "true", multiple)
    if (status.IsError()):
      return status
    if (not multiple) and (len(paths) > 1):
      return Status(kUnknownError, "the element can not hold multiple files")
    # TODO
    element = CreateElement(element_id)
    return web_view.SetFileInputFiles(session.GetCurrentFrameId(), element, paths)
  else:
    return SendKeysToElement(session, web_view, element_id, key_list)

def ExecuteSubmitElement(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      webdriver::atoms::asString(webdriver::atoms::SUBMIT),
      args,
      value)


def ExecuteGetElementText(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      webdriver::atoms::asString(webdriver::atoms::GET_TEXT),
      args,
      value)

def ExecuteGetElementValue(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      "function(elem) { return elem['value'] }",
      args,
      value)


def ExecuteGetElementValue(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      "function(elem) { return elem.tagName.toLowerCase() }",
      args,
      value)

def ExecuteGetElementText(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      webdriver::atoms::asString(webdriver::atoms::GET_TEXT),
      args,
      value)

def ExecuteGetElementSelect(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      webdriver::atoms::asString(webdriver::atoms::IS_SELECT),
      args,
      value)

def ExecuteGetElementEnable(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      webdriver::atoms::asString(webdriver::atoms::IS_ENABLE),
      args,
      value)

def ExecuteGetElementDisplayed(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      webdriver::atoms::asString(webdriver::atoms::IS_DISPLAYED),
      args,
      value)

def ExecuteGetElementLocation(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      webdriver::atoms::asString(webdriver::atoms::GET_LOCATION),
      args,
      value)

def ExecuteGetElementLocationOnceScrolledIntoView(session, web_view, element_id, params, value):
  location = WebPoint()
  status = ScrollElementIntoView(
      session, web_view, element_id, location);
  if (status.IsError()):
    return status
  value[0] = location
  return Status(kOk)


def ExecuteGetElementSize(session, web_view, element_id, params, value):
  args = []
  args.append(CreateElement(element_id))
  return web_view.CallFunction(
      session.GetCurrentFrameId(),
      # TODO
      webdriver::atoms::asString(webdriver::atoms::GET_SIZE),
      args,
      value)

def ExecuteGetElementAttribute(session, web_view, element_id, params, value):
  name = params.get('name', '')
  if name is None:
    return Status(kUnknownError, "missing 'name'")
  return GetElementAttribute(session, web_view, element_id, name, value)


Status ExecuteGetElementValueOfCSSProperty(session, web_view, element_id, params, value):
  property_name = params.get('propertyName', '')
  if property_name is None:
    return Status(kUnknownError, "missing 'propertyName'")
  property_value = []
  Status status = GetElementEffectiveStyle(
      session, web_view, element_id, property_name, property_value);
  if (status.IsError()):
    return status;
  value[0] = property_value[0]
  return Status(kOk);
}

Status ExecuteElementEquals(session, web_view, element_id, params, value):
  std::string other_element_id;
  other_element_id = params.get('other', '')
  if other_element_id is None:
    return Status(kUnknownError, "'other' must be a string")
  value[0] = (element_id[0] == other_element_id)
  return Status(kOk)

                           







































