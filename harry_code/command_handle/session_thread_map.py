import Queue
import time
import threading

class SessionThread(threading.Thread):
  def __init__(self, SessionId):
    threading.Thread.__init__(self)
    self.__quit = False;
    self.__queue = Queue.Queue()
    self.session_id = SessionId

  def run(self):
    while not self.__quit:
      try:
        msg = self.__queue.get()
        function = msg.get('function')
        args = msg.get('args')
        kwargs = msg.get('kwargs')
        function_args = args[:-1]
        fater_event = args[-1]
        a = function(*function_args, **kwargs)
      except Exception:
        pass
      finally:
        self.__queue.task_done()
        fathter.set()

  def quit(self):
    self.__quit = True

  def postTask(self, function, *args, **kwargs):
    self.__queue.put({       
        'function': function,
        'args': args,
        'kwargs': kwargs
    })




SessionThreadMap = {}
def pp(aa):
  print aa
ss = SessionThread(2235)
ss.postTask(pp, 2, 3)
ss.start()
time.sleep(5)
ss.postTask(ss.quit())
print 'zz'

