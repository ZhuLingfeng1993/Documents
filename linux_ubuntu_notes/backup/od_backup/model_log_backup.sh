#!/bin/bash
cd $CAFFE_ROOT
save_dir=~/backup/model_log_backup@`date +%Y-%m-%d`.tar.gz
tar -cvpzf $save_dir \
models \
jobs \
