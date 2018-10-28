#!/bin/bash
# 执行脚本前先 sudo su ,无法识别 ~,所以要自己打home/xx	
save_dir=/media/zhulingfeng/LENOVO/zlf_ubuntu_backup/zlf_ubuntuSystem_backup@`date +%Y-%m-%d`.tar.gz
# 一个命令中间不能有注释
tar -cp  \
/ \
--exclude=/home \
--exclude=/proc \
--exclude=/tmp \
--exclude=/lost+found \
--exclude=/mnt \
--exclude=/media \
--exclude=/run \
--exclude=/sys \
| pigz -p 8 >$save_dir 
# --exclude=/run \
# --exclude=/sys \
# --exckude=/snap \


