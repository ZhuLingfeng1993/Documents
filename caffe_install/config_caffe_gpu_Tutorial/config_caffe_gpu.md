### 参考

[Ubuntu16.04 Caffe 安装步骤记录（超详尽）](https://blog.csdn.net/yhaolpz/article/details/71375762)

[GTX1070+CUDA8.0+Ubuntu16.04+Caffe+SSD 深度学习框架搭建 细节一步到位版](https://blog.csdn.net/sinat_31802439/article/details/52958791)

### 安装nVidia驱动和CUDA

#### 禁用 nouveau

安装好依赖包后需要禁用 nouveau，只有在禁用掉 nouveau 后才能顺利安装 NVIDIA 显卡驱动，禁用方法就是在 /etc/modprobe.d/blacklist-nouveau.conf 文件中添加一条禁用命令，首先需要打开该文件，通过以下命令打开：

`sudo gedit /etc/modprobe.d/blacklist-nouveau.conf`
打开后发现该文件中没有任何内容，写入：

`blacklist nouveau option nouveau modeset=0 `
保存时命令窗口可能会出现以下提示：

`** (gedit:4243): WARNING **: Set document metadata failed: 不支持设置属性 metadata::gedit-position`

无视此提示～，保存后关闭文件，注意此时还需执行以下命令使禁用 nouveau 真正生效：

`sudo update-initramfs -u`

#### 下载 CUDA 8.0

进入 <https://developer.nvidia.com/cuda-downloads> ，依次选择 CUDA 类型然后下载即可。 

`sudo chmod a+x NVIDIA-Linux-x86_64-375.20.run `

#### 删除旧的Nvidia驱动：

卸载驱动 以我安装的nvidia-331-updates为例

如果你安装的其它版本，请自行更改命令

sudo apt-get remove --purge nvidia-331-updates 

如果安装的是官网下载的驱动

则重新运行run文件来卸载

sh ./nvidia.run --uninstall

也有的说: 

sudo apt-get --purge remove nvidia-*(需要清除干净)

sudo apt-get --purge remove xserver-xorg-video-nouveau



重启电脑(!!)

#### 安装 CUDA 8.0

下载的1.4G的 CUDA中包含有 nvidia 显卡驱动，故此步骤 CUDA 的安装包括了 nvidia 显卡驱动的安装，此时注意你是否已经安装过 nvidia 显卡驱动，若无法保证已安装的 nvidia 显卡驱动一定正确，那就卸载掉之前安装的 nvidia 显卡驱动（卸载方法链接)，然后开始安装 CUDA 8.0；若可以保证已安装正确的 nvidia 显卡驱动，则直接开始安装 CUDA 8.0，在安装过程中选择不再安装 nvidia 显卡驱动。

为了方便开始安装过程的路径查找，把下载的 CUDA 安装文件移动到 HOME 路径下，然后通过 Ctrl + Alt + F1 进入文本模式，输入帐号密码登录，通过 Ctrl + Alt + F7 可返回图形化模式，在文本模式登录后首先关闭桌面服务：`sudo service lightdm stop`

然后通过 Ctrl + Alt + F7 发现已无法成功返回图形化模式，说明桌面服务已成功关闭，注意此步对接下来的 nvidia 驱动安装尤为重要，必需确保桌面服务已关闭。

Ctrl + Alt + F1 进入文本模式，然后运行 CUDA 安装文件进行安装，之前我们已经把 CUDA 安装文件移动至 HOME，直接通过 sh 命令运行安装文件即可：

```shell
sudo ./NVIDIA-Linux-x86_64-375.20.run --no-x-check --no-nouveau-check --no-opengl-files
          #--no-x-check 安装驱动时关闭X服务
--no-nouveau-check 安装驱动时禁用nouveau
         # --no-opengl-files 只安装驱动文件，不安装OpenGL文件
#中间有一步询问与xconfig有关的选项，选择默认的no
```

其中 cuda_8.0.61_375.26_linux.run 是我的 CUDA 安装文件名，而你需替换为自己的 CUDA 安装文件名，若此时忘记可直接通过 ls 文件查看文件名，这也是我建议把 CUDA 安装文件移动到 HOME 下的另一个原因。

执行此命令约1分钟后会出现 0%信息，此时长按回车键让此百分比增长，直到100%，然后按照提示操作即可，先输入 accept ，然后让选择是否安装 nvidia 驱动，这里的选择对应第5步开头，若未安装则输入 “y”，若确保已安装正确驱动则输入“n”。

剩下的选择则都输入“y”确认安装或确认默认路径安装，开始安装，此时若出现安装失败提示则可能为未关闭桌面服务或在已安装 nvidia 驱动的情况下重复再次安装 nvidia 驱动，

sudo service lightdm start
重启x-window的服务，并不会出现循环登录的问题

这里似乎不重启也没有关系!!!!

安装完成后输入重启命令重启：`reboot`

重启后登录进入系统，配置 CUDA 环境变量，与第3步相同，使用 gedit 命令打开配置文件：`sudo gedit ~/.bashrc`

在该文件最后加入以下两行并保存：

```shell
export PATH=/usr/local/cuda-8.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

使该配置生效：`source ~/.bashrc`

#### 验证 CUDA 8.0 是否安装成功

sudo nvidia-smi以及sudo nvidia-settings检查驱动是否安装成功

使用 nvcc --version测试是否安装成功

或者分别执行以下命令：

```sehll
cd /usr/local/cuda-8.0/samples/1_Utilities/deviceQuery
sudo make
./deviceQuery
```

若看到类似以下信息则说明 cuda 已安装成功：

```
./deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "GeForce GT 740M"
  CUDA Driver Version / Runtime Version          8.0 / 8.0
  CUDA Capability Major/Minor version number:    3.5
  Total amount of global memory:                 2004 MBytes (2100953088 bytes)
  ( 2) Multiprocessors, (192) CUDA Cores/MP:     384 CUDA Cores
  GPU Max Clock rate:                            1032 MHz (1.03 GHz)
  Memory Clock rate:                             800 Mhz
  Memory Bus Width:                              64-bit
  L2 Cache Size:                                 524288 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(65536), 2D=(65536, 65536), 3D=(4096, 4096, 4096)
  Maximum Layered 1D Texture Size, (num) layers  1D=(16384), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(16384, 16384), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 1 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 1 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 8.0, CUDA Runtime Version = 8.0, NumDevs = 1, Device0 = GeForce GT 740M
Result = PASS
```

### 安装 cudnn

登录官网：https://developer.nvidia.com/rdp/cudnn-download ，下载对应 cuda 版本且 linux 系统的 cudnn 压缩包，注意官网下载 cudnn 需要注册帐号并登录，不想注册的可从我的网盘下载：https://pan.baidu.com/s/1c2xPVzy

下载完成后解压，得到一个 cudn 文件夹，该文件夹下include 和 lib64 两个文件夹，命令行进入 cudn/include 路径下，然后进行以下操作：

1、下载cuDNN后解压

```shell
sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64/
sudo chmod a+r /usr/local/cuda/include/cudnn.h
sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
```

2、cd /usr/local/cuda/lib64/

```shell
sudo rm -rf libcudnn.so libcudnn.so.5    #删除原动态文件
sudo ln -s libcudnn.so.5.1.5 libcudnn.so.5  #生成软链接 ,使用locate libcudnn.so命令查看libcudnn.so.5.x.x的值!
sudo ln -s libcudnn.so.5 libcudnn.so      #生成软链接
#若需要更换cudnn版本，则替换原来的libcudnn*，并重新软链接。
```

这里需要注意第三行命令，网上有人的第三行命令为：

`sudo ln -s libcudnn.so.5.1.5 libcudnn.so.5 #生成软衔接`
起初我执行的也是上条链接 libcudnn.so.5.1.5 的命令，但是后面编译caffe时出错，报错内容为 /usr/bin/ld: 找不到 -lcudnn，所以这里需要先查看一下自己应该链接的是 libcudnn.so.5.1.10 还是 libcudnn.so.5.1.5 ，查看方法为下：

`locate libcudnn.so`
我执行完后显示如下：

```
yhao@yhao-X550VB:~$ locate libcudnn.so
/home/yhao/.local/share/Trash/files/libcudnn.so
/home/yhao/.local/share/Trash/files/libcudnn.so.5
/home/yhao/.local/share/Trash/files/libcudnn.so.5.1.10
/home/yhao/.local/share/Trash/files/cuda/lib64/libcudnn.so
/home/yhao/.local/share/Trash/files/cuda/lib64/libcudnn.so.5
/home/yhao/.local/share/Trash/files/cuda/lib64/libcudnn.so.5.1.10
/home/yhao/.local/share/Trash/info/libcudnn.so.5.1.10.trashinfo
/home/yhao/.local/share/Trash/info/libcudnn.so.5.trashinfo
/home/yhao/.local/share/Trash/info/libcudnn.so.trashinfo
/home/yhao/cuda/lib64/libcudnn.so
/home/yhao/cuda/lib64/libcudnn.so.5
/home/yhao/cuda/lib64/libcudnn.so.5.1.10
/usr/local/lib/libcudnn.so
/usr/local/lib/libcudnn.so.5
```

可以看到我的文件是 libcudnn.so.5.1.10 ，并没有 libcudnn.so.5.1.5，所以第三行命令我链接的是 libcudnn.so.5.1.10 ，这里第三行链接命令视你的查看结果而定。

安装完成后可用 nvcc -V 命令验证是否安装成功，若出现以下信息则表示安装成功：

```shell
yhao@yhao-X550VB:~$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2016 NVIDIA Corporation
Built on Tue_Jan_10_13:22:03_CST_2017
Cuda compilation tools, release 8.0, V8.0.61
```

### 安装opencv

参考cpu安装

### 安装caffe

参考cpu安装

#### 配置Makefile.config

参考cpu安装

不同之处:

将`#USE_CUDNN := 1`

修改成：
`USE_CUDNN := 1`

#### 配置Makefile

将：
`NVCCFLAGS +=-ccbin=$(CXX) -Xcompiler-fPIC $(COMMON_FLAGS)`
替换为：
`NVCCFLAGS += -D_FORCE_INLINES -ccbin=$(CXX) -Xcompiler -fPIC $(COMMON_FLAGS)`

将：
`LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5`
改为：
`LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_serial_hl hdf5_serial`

#### make all -j28

#### make test -j28

#### sudo make runtest -j28

报错：
`Check failed: error == cudaSuccess (8 vs. 0) invalid device function`
这种错误的情况是由于显卡计算能力的不同而又没配置好导致的。要将上面的CUDA_ARCH参数改为与你显卡相匹配的数值。
解决：
查找显卡对应的计算能力（https://developer.nvidia.com/cuda-gpus），修改Makefile.config,添加上对应的一行，
如：

```
CUDA_ARCH := -gencode arch=compute_60,code=sm_60 \
	     #-gencode arch=compute_20,code=sm_20 \
             #-gencode arch=compute_20,code=sm_21 \
             -gencode arch=compute_30,code=sm_30 \
             -gencode arch=compute_35,code=sm_35 \
             -gencode arch=compute_50,code=sm_50 \
             -gencode arch=compute_52,code=sm_52 \
	     -gencode arch=compute_60,code=sm_60 \
             -gencode arch=compute_61,code=sm_61
```

然后重新编译，make all -j28，再sudo make runtest -j28


