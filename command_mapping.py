
from commands_internal import *
from command import Command
from http_server_response import HttpServerResponse
  

class CommandMapping():
  ''' After parse the Json Http wired protocol from selenium, Wrap the specific request to specific function in this table '''

  WrapCommand = {
    Command.STATUS: HttpServerResponse.status,
    Command.NEW_SESSION: ExecuteCreateSession,      
    Command.GET_SESSION: HttpServerResponse.getSession,
    Command.GET: HttpServerResponse.get,
  }
        


def test():
  for k,v in CommandMapping.WrapCommand.items():
    print k
    print v
         
if __name__ == "__main__":
  test()
