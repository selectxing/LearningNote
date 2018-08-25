# 错误调试
'''
import logging  #使用logging模块记录日志
try:
except Exception/ValueError as e:
    logging.exception(3)
finally:
raise
'''

# 异常BaseException说明：https://docs.python.org/3/library/exceptions.html#exception-hierarchy

def main():
    try:
        print(test(0))
    except Exception as e:
        print("异常：", e)
def test(s):
    return 10 / s
main()

#调试：断言assert方式、logging模块方式、pdb方式、IDE断点

#单元测试：unittest模块
#文档测试doctest