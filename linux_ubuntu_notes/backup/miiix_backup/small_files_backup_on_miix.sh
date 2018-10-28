#save_dir=~/backup/small_files_backup@`date +%Y-%m-%d`.tar.gz 
save_dir=/media/zhulingfeng/LENOVO/zlf_ubuntu_backup/small_files_backup@`date +%Y-%m-%d`.tar.gz 
#exclude_file_list=~/software/caffe-ssd-zlf/examples/ssd/ssd_detect/video_first.h264
cd ~
tar -cvpzf $save_dir \
~/Documents \
$CAFFE_ROOT/{src,include} \
$CAFFE_ROOT/examples/{ssd,mobileNet_ssd,mobileNet_ssdLite,fssd} \
$CAFFE_ROOT/python/caffe \
$CAFFE_ROOT/{Makefile,Makefile.config} \
$CAFFE_ROOT/tools/extra/{plot_log.py,parse_time_log.py} \
$CAFFE_ROOT/tools/zlf_caffe.cpp \
~/software/RefineDet/examples/refinedet/SSRD_pascal.py \
~/software/RefineDet/python/caffe/model_libs.py \
~/software/RefineDet/tools/extra/plot_log.py \
#--exclude=$exclude_file_list \
