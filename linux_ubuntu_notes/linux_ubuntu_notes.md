# linux/ubuntu notes 

### 修改pip源

**pip国内的一些镜像**

  阿里云 <http://mirrors.aliyun.com/pypi/simple/> 
   中国科技大学 <https://pypi.mirrors.ustc.edu.cn/simple/> 
   豆瓣(douban) <http://pypi.douban.com/simple/> 
   清华大学 <https://pypi.tuna.tsinghua.edu.cn/simple/> 
   中国科学技术大学 <http://pypi.mirrors.ustc.edu.cn/simple/>

**修改源方法：**

**临时使用：** 
 可以在使用pip的时候在后面加上-i参数，指定pip源 
 eg: pip install scrapy -i <https://pypi.tuna.tsinghua.edu.cn/simple>

**永久修改：** 
 **linux:** 
 修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：

```
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```

**windows:** 
 直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### 

### 设置PATH变量

#### 命令

`export PATH=$PATH:some_path`: 将some_path 添加到PATH末尾

`export PATH=some_path:$PATH`: 将some_path添加到PATH最前面

#### 始终有效

在`~/.bashrc`中添加上述命令, 并且在终端执行`source ~/.bashrc`使其立即生效(有可能当前终端不生效而其它终端生效)

#### 临时有效

在终端直接执行命令, 只在该终端有效

### 查看硬盘分区信息：

`$sudo fdisk -l`

`df`

### Ubuntu下移动硬盘报错、无法挂载问题的解决

使用指令进行修复： 

` sudo ntfsfix /dev/sdaX(无法挂载的硬盘分区) `

### 打包和压缩

打包应该只是作为一个文件存储,并尽可能连续存储

压缩对某些文件能减小体积, 但也会更费时

[pigz高效压缩解压命令](https://blog.csdn.net/luo617/article/details/81223428)

```shell
# pigz压缩：pigz：用法-9是压缩比率比较大，-p是指定cpu的核数。
tar cvf - mydir | pigz -9 -p 24 > file.tgz

# pigz解压: 只能夹解压,不能解包
pigz -d  file.tgz
pigz -dc  file.tgz  # cat的形式打印出来
unpigz file.gz

#.tar （注：tar是打包，不是压缩！） 
解包：tar xvf FileName.tar 
打包：tar cvf FileName.tar DirName #注意先tar, 后打包目录
———————————————

#.gz 
解压1：gunzip FileName.gz 
解压2：gzip d FileName.gz 
压缩：gzip FileName 
#.tar.gz 和 .tgz 
解压：tar zxvf FileName.tar.gz 
压缩：tar zcvf FileName.tar.gz DirName 
```

### ppa

#### ppa source

/etc/apt/sources.list.d

#### install ppa apt

ppa:personal package archive(非官方的package)
公司的网络下载不了，要用外网

### Problem:lock

unable to lock the administration directory (/var/lib/dpkg/) is another process using it
SOLUTION:
https://linux.cn/article-8040-1.html
1.找出并杀掉所有 apt-get 或者 apt 进程
ps -A | grep apt

sudo kill -9 processnumber
或者
$ sudo kill -SIGKILL processnumber

2、 删除锁定的文件

### boot空间不足

系统更新内核导致的boot空间不足，可以尝试删除旧的内核。

查看boot分区信息
`df -h /boot` 

输入命令，查看目前系统中安装的内核镜像
`dpkg --get-selections |grep linux-image`

键入命令，查看本机系统的内核版本：
uname -r

卸载旧的版本
sudo apt-get purge linux-image-(版本号)

### gedit 中文乱码

命令行运行：

```shell
gsettings set org.gnome.gedit.preferences.encodings auto-detected "['GB18030', 'UTF-8', 'CURRENT', 'ISO-8859-15', 'UTF-16']"
```

从网上找的解决方法，直接复制粘贴无效，将上述命令中的所有引号改成英文状态引号就可以

### 问题:从外部应用打开连接后,chrome只显示一个空的标签,不会自动跳转

平台:Ubuntu 16.04 Desktop

------

解决办法:https://askubuntu.com/questions/689449/external-links-are-opened-as-blank-tabs-in-new-browser-window-in-chrome 
The issue is with google-chrome.desktop, and it is missing the %U argument . 
Open file: $HOME/.local/share/applications/google-chrome.desktop 
Find the line: 
Exec=/opt/google/chrome/chrome 
Add a space and %U: 
Exec=/opt/google/chrome/chrome %U 
Then save the file.

翻译一下: 
出现这个问题跟 google-chrome.desktop 有关,它缺少一个参数 %U。 
打开文件:$HOME/.local/share/applications/google-chrome.desktop 
找到下面这行: 
Exec=/opt/google/chrome/chrome 
在末尾添加一个空格和%U: 
Exec=/opt/google/chrome/chrome %U 
然后保存文件即可。

### 远程访问

- teamviewer

  unbutu下使用即使网络较好也会卡

- ssh

### wifi

[联想拯救者 ](https://www.cnblogs.com/renqiangnwpu/p/8334689.html)[+ ubuntu16.04 + WIFI设置](https://www.cnblogs.com/renqiangnwpu/p/8334689.html)  

根本问题：当装入Ubuntu16.04双系统时，会出现无线网卡被hard blocked问题。

```
$ rfkill list all

0: ideapad_wlan: Wireless LAN
Soft blocked: no
Hard blocked: yes
1: ideapad_bluetooth: Bluetooth
	Soft blocked: yes
	Hard blocked: yes
2: ideapad_3g: Wireless WAN
	Soft blocked: no
	Hard blocked: yes
3: hci0: Bluetooth
	Soft blocked: yes
	Hard blocked: no
4: phy0: Wireless LAN
	Soft blocked: no
	Hard blocked: no
```

### 双系统查看windows的文件

[双系统下](https://blog.csdn.net/hustcw98/article/details/79323575)[Linux无法访问windows文件夹的问题](https://blog.csdn.net/hustcw98/article/details/79323575)

查看硬盘分区

```
sudo fdisk -l
```

 可以找到相应的windows的盘的代号

最后使用命令``ntfsfix``修复即可，这里是`/dev/sda1`

```
sudo ntfsfix /dev/sda1
```

###  Windows10 和 Ubuntu 16.04 双系统 系统时间不统一解决

https://blog.csdn.net/qinkang1993/article/details/54617867
https://blog.csdn.net/zyqblog/article/details/79318955

### Ubuntu中安装包出现的依赖问题

修改源，然后upgrade

### 修改Ubuntu 源

`$ sudo gedit /etc/apt/sources.list`

Uncommnet default source

添加TsingHua Source：

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
```

 修改完毕后，

```shell
sudo apt-get update  
sudo apt-get upgrade
```
### 无法输入中文
<https://www.cnblogs.com/darklights/p/7722861.html>
不必安装搜狗，按操作安装fcitx就行，然后选择pinyin
### 系统备份
<https://blog.csdn.net/qq_35523593/article/details/78545530>
<https://blog.csdn.net/sinat_27554409/article/details/78227496>
需要备份到移动硬盘或者其它分区上


### 设置默认分辨率
https://jingyan.baidu.com/article/d45ad148a269b969552b80e4.html
(1) `cvt 1920 1080 #查看需要的分辨率对应的modeline`
(2) `xrandr #可以看到当前显示器的名字（箭头所指）以及当前显示器正在使用的分辨率`
(3) `gedit ~/.profile`
#在fi之后回车换行并空出一行后输入：

```shell
cvt 1920 1080
xrandr --newmode 1920x1080 173.00 1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode 显示器名 1920x1080
```

保存并退出
(4) 注销后登陆

其它设置:

```shell
cvt 1920 1080
xrandr --newmode 1920x1080_60.00  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode VGA-1 1920x1080_60.00

cvt 1360 768
xrandr --newmode 1360x768_60.00   84.75  1360 1432 1568 1776  768 771 781 798 -hsync +vsync
xrandr --addmode VGA-1 1360x768_60.00

cvt 1600 900
xrandr --newmode 1600x900_60.00  118.25  1600 1696 1856 2112  900 903 908 934 -hsync +vsync
xrandr --addmode Virtual1 1600x900_60.00

```



