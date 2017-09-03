[TOC]

# markdown格式化学习笔记
## 列表
1. 无序列表
  - 第一种方式'-'
    - 以'-'开头
    - 后面加一个空格，然后在写内容
  - 第二种方式'*'
    * 以'*'开头
    * 后面加一个空格，然后在写内容
2. 有序列表
  - 以'1.'开头
  - 后面加一个空格，然后在学内容

>当然写完上面 嵌套就是回车后按table

****


## 代码块的实现
```javascript
# 声明一个变量
var aa = 'haha'
function demo (){
  console.log(aa)
}
```
```python
import os
print 'haha'
```
***
## 插入图片
![](http://img0.bdstatic.com/static/searchresult/img/logo-2X_b99594a.png)

***
## 插入链接
[百度](http://www.baidu.com)
***

## 引用
> 引用测试的引用测试的引用测试的引用测试的引用测试的引用测试的引用测试的引用测试的引用测试的引用测试的引用测试的引用测试的
***
## 粗体 和 斜体
### 粗体
>**我是粗体**

### 斜体
> *我是斜体*

***

## 表格 还可以写html 真厉害
<table style="text-align:center">
  <tr>
    <td>哈哈</td>
    <td>哈哈</td>
    <td>哈哈</td>
    <td>哈哈</td>
  </tr>
  <tr>
    <td>哈哈</td>
    <td>哈哈</td>
    <td colspan="2">哈哈</td>
  </tr>
    <tr>
    <td>哈哈</td>
    <td>哈哈</td>
    <td>哈哈</td>
    <td>哈哈</td>
  </tr>
</table>

***

## 分割线

>测试测试测测试
>> 测试测时候测试测测试
>>> 测试IC额 测试IC额 测试IC额 测试IC额

***
##  列表和引用混用
* 我是一个列表
  > 其实我是一个引用

***

## 列表里面嵌套code

* 我是一个列表
    <h1>我是一段代码</h1>
    &book;&time;


****
    我是一个缩进了4个空格的代码块

****
## 支持字体标签
[字体网址](http://fontawesome.io/3.2.1/icons/)
<i class="icon-book">
<i class="icon-clock">
<i class="icon-bug">
<i class="icon-rocket">
