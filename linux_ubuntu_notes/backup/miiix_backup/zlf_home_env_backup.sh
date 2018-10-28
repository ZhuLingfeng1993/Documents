#save_dir=~/backup/zlf_home_env_backup@`date +%Y-%m-%d`.tar.gz
save_dir=/media/zhulingfeng/LENOVO/zlf_ubuntu_backup/zlf_home_env_backup@`date +%Y-%m-%d`.tar.gz
#.config?
tar -cvpzf $save_dir ~/{.bashrc,.pip,.profile,.config,bin} 
