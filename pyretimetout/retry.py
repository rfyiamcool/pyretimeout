#coding:utf-8
from functools import wraps
import signal
import time
import os

class Failing(Exception):
    pass

def Timeout(signum, frame):
    print 'task is timeout' 

def timeout(func, args=(), kwargs={}, timeout_duration=3, default=None):
    class TimeoutError(Exception):
        pass

    def handler(signum, frame):
        raise TimeoutError()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_duration)
    try:
        result = func(*args, **kwargs)
    except TimeoutError as exc:
        result = default
    finally:
        signal.alarm(0)

    return result

def retry(retries,timeout_duration=None,all_limit=False):
    def repl(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            i = 0
            start = int(time.time())
            #return timeout(f,timeout_duration=1)
            
            while i < retries:
                if timeout_duration and all_limit:
                    if i==0:
                        signal.signal(signal.SIGALRM, Timeout)
                        signal.alarm(timeout_duration)
                    if i>0:
                        signal.signal(signal.SIGALRM, Timeout)
                        left = timeout_duration - (end - start) 
                        print left
                        if left<1:
                            signal.alarm(1)
                        else:
                            signal.alarm(left)
                        
    

                if timeout_duration and not all_limit:
                    signal.signal(signal.SIGALRM, Timeout)
                    signal.alarm(timeout_duration)


                print 'Retry count:',i
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    i += 1
                    if retries == i:
                        raise Failing(e)
                finally:
                    end = int(time.time())
                    
        return wrapper
    return repl
