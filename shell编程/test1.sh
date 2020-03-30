#!/bin/bash
your_name='run'
str="Hello, I know you are \"$your_name\"!\n"
echo $str
greeting="hello, "${your_name}" !"
echo $greeting
string="abcd"
echo ${#string} #获取字符串长度
echo $#string
string="runoob is a great site"
echo ${string:1:4} #提取字符串 从字符串第2个字符开始截取4个单位长度的字符
echo `expr index "$string" io` #查找字符i/o的位置 哪个先出现就计算哪个
#执行语句里面的字符串好像一定要写在""" 其他好像都会报错
array=(1 2 3 "4" "5") 
echo ${array[@]}
echo ${#array[@]}
echo ${array[2]}
:<<EOF
sdsdsd
sdsds
多行注释 
EOF也可以替换成别的符号  ' ! 但是在EOF后面多一个空格也会报错
EOF