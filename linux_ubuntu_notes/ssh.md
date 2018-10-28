## 不同局域网下ssh使用

[不同局域网ubuntu如何进行ssh穿透登录](https://blog.csdn.net/MONKEY3233/article/details/80240673): 需要能设置**被连接电脑**所在网络的路由器



其它:要用一个独立服务器, 可以免费申请?

## 同一局域网下ssh使用

### 参考:

[linux下使用ssh连接另一台linux服务器](https://jingyan.baidu.com/article/59703552abe8b88fc1074051.html)

[TLCL:网络系统](http://www.ciku6.com/chap17.html)

`man ssh`

### 步骤

安装ssh

查看服务器ip

登录: `ssh user@remote_ip`

图形界面: 登录时`ssh -X user@remote_ip`

当网络状况不好时, 压缩数据会明显提速: 登录时`ssh -X user@remote_ip`

[ssh 登录报错 packet_write_wait: Connection to x.x.x.x port 22: Broken pipe](https://blog.csdn.net/u013511989/article/details/79972435)

### 文件拷贝

[Linux下常用的文件传输方式介绍与比较](https://www.cnblogs.com/wfwenchao/p/6008959.html)

#### scp

参考: [每天一个linux命令：scp命令](https://www.cnblogs.com/webnote/p/5877920.html)

只能在local端操作

不好用, 无法对远端路径进行自动补全

### sftp 

建议先看文档: `man sftp`

参考:[linux下如何使用sftp命令【转】](https://www.cnblogs.com/the-tops/p/5956163.html)

首先:在local运行 `sftp user@remote-ip`, 进入sftp交互界面 (加上-C 可以压缩数据)

在remote执行命令: 就像一般在本地操作的命令一样, 但不支持环境变量

在local执行命令: 一般在本地操作的命令前面加`l`

从remote下载: `get [-afPpr] remote-path [local-path]`

上传到remote: `put [-afPpr] local-path [remote-path]`