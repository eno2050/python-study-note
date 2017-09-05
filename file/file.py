# _*_ coding:utf-8 _*_


def testFileFunc():
    '''
    用来测试文件打开的模式不同带来的结果
    '''
    # keywords = raw_input("请输入您要测试的模式:")
    # if keywords.lower() == 'r':
    #     print '我是只读文件'
    # elif keywords.lower() == 'w':
    #     print '我是可写文件'
    # else:
    #     print '您的输入不正常'
    fp = open('hello.txt','a+')
    print fp.read()
    fp.close()
    fp = open('hello.txt','a+')
    fp.write('hello world')
    fp.close()

if __name__ == '__main__':
    testFileFunc()
