```
sudo dpkg -i teamviewer_12.0.76279_i386.deb
```

会有denpends的问题

（下面这个命令是修复依赖关系（depends）的命令，就是假如你的系统上有某个package不满足依赖条件，这个命令就会自动修复，安装那个package依赖的package）

　　这个时候需要执行命令：

```
sudo apt-get install -f
```

再运行

```
sudo dpkg -i teamviewer_12.0.76279_i386.deb
```

## Teamviewer note

Teamviewer账户:与某台计算机无关，通过邮箱注册，有帐户名和密码
某台计算机：
独一无二的ID（teamviewer ID）
使用teamviwer时的名称
随机密码：在该机随机生成，用于临时访问
个人密码（用于无人值守访问）：可以远程输入teamviwer ID 和个人密码访问
授权轻松访问？：似乎没什么用
账户分配：将该计算机分配至某个Teamviewer账户，可以无需密码（只要该机开启teamviewer）对该机进行远程控制，注意，只能是一个账户
个人密码可由进入本台计算机的任意一个人通过任意一个teamviewer修改——所以如果出于安全，进入计算机应该有密码（也就是计算机账户登陆密码）

现在的问题是我们需要多个人能够对一台计算机的某个账户进行远程控制
所以首先，这几个人要知道计算机的该账户登陆密码
其次，要对该机进行远程访问，这几人需要知道该机的teamviewer ID(或者添加到某个teamViewer账户后取一个名字)和个人密码，
然后，这几个人用各自的teamViewer 账户，分别访问该机。