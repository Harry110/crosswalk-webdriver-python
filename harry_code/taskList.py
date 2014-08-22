#!/usr/bin/env python

 
import logging
import Queue
import threading

def async_call(function, callback, *args, **kwargs):
    _task_queue.put({
        'function': function,
        'args': args,
        'kwargs': kwargs
    })

def _task_queue_run():
    while True:
        try:
            task = _task_queue.get()
            function = task.get('function')
            args = task.get('args')
            kwargs = task.get('kwargs')
            try:
                if callback:
                    callback(function(*args, **kwargs))
            except Exception as ex:
                if callback:
                    callback(ex)
            finally:
                _task_queue.task_done()
        except Exception as ex:
            print 'good'
            logging.warning(ex)
