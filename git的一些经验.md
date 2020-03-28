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
删除一个本地分支git branch -d xxx
从分支切回主分支并合并的方式：
git checkout master
git merge [分支名]
删除远程分支git push origin --delete 分支名
查看远程和本地的所有分支git branch -a
查看远程仓库origin 的信息git remote show origin 
通过git remote prune origin 移除那些远程仓库不存在的分支 这是参照远程移除本地

如果远程主机删除了某个分支，默认情况下，git pull 在拉取远程分支的时候，不会删除对应的本地分支。以防其他人操作了远程主机，导致git pull不知不觉删除了本地分支。但是，我们可以改变这个行为，加上参数 -p 就会在本地删除远程已经删除的分支
git pull -p