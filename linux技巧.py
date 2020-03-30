ctrl z 将当前程序放到后台运行 恢复当前运行 fg
ctrl s 暂停当前程序 按任意键继续
ctrl c 中断当前程序
alt+backspace 向前删除一个单词
touch xxx.txt yyy.txt 创建文件
touch love_{1..10}_shiyanlou.txt 一次创建多个文件
mkdir -p one/two/three 一次创建多级目录
tree [XXX]  显示某文件夹的树形图
rm -r xxx 删除文件夹下所有内容
cp -r xxx 复制文件夹下所有内容
mv xxx yyy 可以把一个文件移到另一个文件夹下 也可以给他重命名（如果移动目的地的文件名不存在就会重命名） 移动文件夹也可以 不需要-r 
cat -n xxx  可以带行号的打印文件内容
man [命令名] 可以显示命令的详细信息 有些命令也可以--help