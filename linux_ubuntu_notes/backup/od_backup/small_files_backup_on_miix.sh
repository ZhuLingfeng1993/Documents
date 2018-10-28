save_dir=~/backup/small_files_backup@`date +%Y-%m-%d`.tar.gz 
#exclude_file_list=~/software/caffe-ssd-zlf/examples/ssd/ssd_detect/video_first.h264
cd ~
tar -cvpzf $save_dir \
~/Documents \
$CAFFE_ROOT/{src,include} \
$CAFFE_ROOT/examples \
$CAFFE_ROOT/{Makefile,Makefile.config} \
#--exclude=$exclude_file_list \
