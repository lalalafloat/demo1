git 如果配置好了config的话不用指定远程仓库
没配置可以执行下面这个命令（我没试过）
git remote add origin 远程仓库地址
建一个新分支 git branch xxx    注意这是在当前head的地方建立
git checkout xxx 切换到某分支
上面两个命令等于 git checkout -b xxx
如果是原来就提交过的代码 只是修改是M的话 可以用git commit -am "xx"
这等于：
git add .
git commit -m "some str"
git push
但是新建的就不能-am
push 到远程指定分支命令
git push -u origin xxxx
删除一个分支git branch -d xxx