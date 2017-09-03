# Python学习笔记
>Class内置属性
1. __dict__:类的属性(包含一个字典，由类的数据类型组成)
2. __doc__:类的文档字符串
3. __name__:类名
4. __module__:类定义的模块
  - 类的全名是: '__main__.className'
  - 如果类在一个导航模块Mymod中，那么className.__moudle__ 等于 Mymod
5. __bases__:类的所有父类元素组成的集合
