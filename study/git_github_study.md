# 教程或参考资料

## [廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

## 远程仓库: github

[github help](https://help.github.com/):

[Set up git](https://help.github.com/articles/set-up-git)

[Create a repo](https://help.github.com/articles/create-a-repo)

## study_material ——git——cheatsheet

# 笔记

#### 先有本地库，后有远程库

创建本地仓库

`git init`, 会生成.git文件夹

###### 本地上传到远端

在github上 新建repo

关联: `git remote add name xxx.git`, name 为本地给远端取的名字, 一般用origin

push: `git push -u origin master`

把本地库的内容推送到远程，用`git push`命令，实际上是把当前分支`master`推送到远程。

由于远程库是空的，我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送的远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来，在以后的推送或者拉取时就可以简化命令。

从现在起，只要本地作了提交，就可以通过命令：

```
$ git push origin master
```

把本地`master`分支的最新修改推送至GitHub

###### 从远端上更新本地

`git pull origin master `

#### 先创建远程库，然后，从远程库克隆

现在，假设我们从零开发，那么最好的方式是先创建远程库，然后，从远程库克隆。

```
git clone xxx.git
```

注意这和直接download是不同的

查看remote: `git remote -v`

查看branch: `git branch -av`

切换到已经存在的branch dev : `git checkout dev`

本地的代码管理, 可视化(暂时不需要, 还没有那么复杂)

#### 笔记本与服务器的代码一致

1. miix上初始化一个代码文件(meld miix od上同名文件), add, commit ,push
2. od上删除同名文件
3. od上pull

#### cheatsheet

每条log显示一行: 

```
git log --pretty=oneline
```

#### 流程                    

0. 操作-撤回操作

1. 添加文件
2. 修改文件-`git checkout -- <file> `
3. add-`git reset HEAD <file>`
4. commit-`git reset --hard HEAD^  `(版本回退)
5. push-无法撤销

#### 忽略文件: gitignore

可以在github网站上找到常用的忽略文件

#### git原理分析

git的结构是树状结构(merge 不是真正的建立连接)

HEAD是当前指针, 分支名是分支最末端的指针,git log中的结点名就是结点指针

`git merge branch_name`是将branch_name merge到当前HEAD(即当前branch)



