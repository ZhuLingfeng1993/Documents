备份的前提是文件组织合理

### 运行脚本出现一些奇怪的问题

是因为有些文件是我在windows下，创建的（-rw-r--r--），发现和在linux下创建的（-rw-rw-r--)权限不一样

一个命令中间不能有注释

### 系统备份和还原参考资料

<https://blog.csdn.net/qq_35523593/article/details/78545530>

<https://blog.csdn.net/sinat_27554409/article/details/78227496>

### tar

```
参数：
-c： 新建一个备份文档
-v： 显示详细信息
-p： 保存权限，并应用到所有文件
-z： 用gzip压缩备份文档，减小空间
-f： 指定备份文件的路径
--exclude： 排除指定目录，不进行备份
```

```
/proc：一个虚拟文件系统，系统运行的每一个进程都会自动在这个目录下面创建一个进程目录。既然是系统自动创建，也就没必要备份的必要了。
/tmp：一个临时文件夹，系统的一些临时文件会放在这里。
/lost+found：系统发生错误时（比如非法关机），可以在这里找回一些丢失文件。
/media：多媒体挂载点，像u盘、移动硬盘、windons分区等都会自动挂载到这个目录下。
/mnt：临时挂载点，你可以自己挂载一些文件系统到这里。
/run：系统从启动以来产生的一些信息文件。
/home：用户家目录，存放用户个人文件和应用程序。
/boot：和系统启动相关的文件，像grub相关文件都放在这里，这个目录很重要！
```

### 多线程压缩

```
sudo apt install pigz
```

```shell
tar -cvp fileName | pigz -p 8 > fileName.tar.gz
```

### home文件备份

1. 小文件备份

small_file_backup.sh

笔记，README，脚本程序

2. 大文件备份

备份到移动硬盘，手动备份

model_log_backup.sh

- 训练日志：train日志的清理，然后程序备份
- 训练好的caffemodel：清除旧的模型后程序备份
- 训练/测试 数据：整个数据文件夹备份（去除lmdb文件，包含脚本），手动备份
- 软件安装包(tools,ssd相关,caffe环境配置软件、驱动） ：组织好（目前在Downloads和tools_zlf下）

### 系统备份

主要是为了发生意外的时候能很快恢复系统环境，需要剔除大文件备份以及不需要的文件

- 备份~/.bashrc
- od_ubuntuSystem_backup.sh

### 文件的分解和合并

#### split

```shell
split -b 2048m -d -a 1 od_ubuntuSystem_backup@2018-08+01.tar.gz od_ubuntuSystem_backup@2018-08+01.tar.gz --verbose
```

#### cat

```shell
cat od_ubuntuSystem_backup@2018-08+01.tar.gz* > cat_od_ubuntuSystem_back
up@2018-08+01.tar.gz
```





