pyretry
====

```python
import requests
from pyretimetout import *

@retry(5,timeout_duration=2,all_limit=True) # all task timeout in 2s
def go(*args):
    time.sleep(4)
    return aa

go()
Retry count: 0
task is timeout
Retry count: 1
task is timeout
Retry count: 2
task is timeout
Retry count: 3
task is timeout
Retry count: 4
task is timeout

@retry(10,5) # Retry function upto 10 times, each task timeout in 5s
def fetch():
	r = requests.get('http://xiaorui.cc')
	return r.text

fetch()
```
## Installation
#####nima! pyretry 已经让人给抢先占用了,只能改名为 pyretimeout
pyretimeout can be installed using Pypi, `pip install pyretimeout`

