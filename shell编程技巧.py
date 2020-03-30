shell编程就是对一堆Linux命令的逻辑化处理
sudo chmod +x cleanlogs.sh 赋予文件可执行权限
cat /dev/null > xxx.txt 利用重定向功能删除某一文件/文件夹内容
echo 打印字符串/变量内容
行首以 # 开头(除#!之外)的是注释。#!是用于指定当前脚本的解释器
'''
#!/bin/bash

echo "The # here does not begin a comment."
echo 'The # here does not begin a comment.'
echo The \# here does not begin a comment.
echo The # 这里开始一个注释
echo $(( 2#101011 ))     # 数制转换（使用二进制表示），不是一个注释，双括号表示对于数字的处理

# 欢迎来到实验楼参观学习
'''
使用$符号加上变量名就行了。记住：定义变量不用$符号，使用变量要加$就行了
#!/bin/bash
path=$(pwd) 两种赋值给变量的方式 如果是不需要执行的量好像直接等于也行
files=`ls -al`
echo current path: $path
echo files: $files

在shell中，有两种方式能实现整数运算，一种是使用expr命令， 另外一种是通过方括号（$[]）来实现。下面分别来看看：
