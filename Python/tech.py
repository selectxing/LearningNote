# python之禅
import this

# import、from import、import as区别
'''
import：引入整个包，调用包中某个类时需要写包名
from import：引入包中某个类，调用该类时无需再写包名
import as：引用并设置别名
'''
import datetime
print(datetime.datetime.now())

from datetime import datetime
print(datetime.now())

import datetime as dt
print(dt.datetime.now())

from datetime import datetime as dt
print(dt.now())

# 如何简单地理解Python中的if __name__ == '__main__'
'''
https://blog.csdn.net/yjk13703623757/article/details/77918633/
'''