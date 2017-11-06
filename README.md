# pyretimeout

给任务加入超时控制.

```python
import requests
from pyretimetout import *

@retry(5, timeout_duration=2, all_limit=True) # all task timeout in 2s
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


@retry(10, 5) # Retry function to 10 times, each task timeout in 5s
def fetch():
	r = requests.get('http://xiaorui.cc')
	return r.text


fetch()
```

## Install

install

```
python setup.py install
```

OR

```
# pip install pyretimeout
```

## More

To Do List:

* 现在的all_limit时间有误差，因为signal信号不能秒级别
* 一些层次的逻辑还可以优化
* 用多线程的去做尝试,测试通过

