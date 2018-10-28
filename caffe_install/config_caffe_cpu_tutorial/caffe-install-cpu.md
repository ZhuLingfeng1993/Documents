### 参考资料

[Ubuntu16.04 Caffe 安装步骤记录（超详尽）](https://blog.csdn.net/yhaolpz/article/details/71375762	) 

### 安装依赖项

```shell
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler

sudo apt-get install --no-install-recommends libboost-all-dev libopenblas-dev liblapack-dev libatlas-base-dev libgflags-dev libgoogle-glog-dev liblmdb-dev git cmake build-essential
```

### 配置环境变量

 同样使用 gedit 命令打开配置文件：

```shell
 sudo gedit ~/.bashrc
```

 打开后在文件最后加入以下两行内容：

```shell
 export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH

 export LD_LIBRARY_PATH=/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH  
```

```shell
source ~/.bashrc
```

### 安装opencv3.4

 进入官网 : <http://opencv.org/releases.html> , 选择 3.4.0 版本的 source , 下载 opencv-3.4.0.zip 

 解压到你要安装的位置，命令行进入已解压的文件夹 opencv-3.4.0 目录下，执行：

```shell
 mkdir build # 创建编译的文件目录
 cd build	
 cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
 make -j8  #编译
```

 编译成功后安装：

 `sudo make install #安装 `

 安装完成后通过查看 opencv 版本验证是否安装成功：

 `pkg-config --modversion opencv   `



#### pytohn import cv2报错: 

```ImportError: No module named cv2.```

解决:

```
sudo apt-get install python-opencv （python2.7.12版本）
sudo pip3 install opencv-python（python3.5.2版本）
```

### 安装caffe

#### 下载

首先在你要安装的路径下 clone ：

```
git clone https://github.com/BVLC/caffe.git
```

#### makefile.config

进入 caffe ，将 Makefile.config.example 文件复制一份并更名为 Makefile.config ，也可以在 caffe 目录下直接调用以下命令完成复制操作 ：

```shell
 cp Makefile.config.example Makefile.config
```

 复制一份的原因是编译 caffe 时需要的是 Makefile.config 文件，而Makefile.config.example 只是caffe 给出的配置文件例子，不能用来编译 caffe。

然后修改 Makefile.config 文件，在 caffe 目录下打开该文件：

 ```shell
gedit Makefile.config
 ```

 修改 Makefile.config 文件内容：

**1.应用 cpu**

```
#CPU_ONLY := 1
修改为： 
CPU_ONLY := 1
```

**2.应用 opencv 版本**

```
将
#OPENCV_VERSION := 3 
修改为： 
OPENCV_VERSION := 3
```

**3.使用 python 接口**

```
将
#WITH_PYTHON_LAYER := 1 
修改为 
WITH_PYTHON_LAYER := 1
```

4. **修改 python 路径**

```
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib 
修改为： 
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu 
```

####  Makefile 

```
 将：
 LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5
 改为：
LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_serial_hl hdf5_serial

LIBRARIES += boost_thread stdc++  修改为
LIBRARIES += boost_thread stdc++  boost_regex
```

#### ldconfig

`sudo ldconfig`

> ldconfig是一个动态链接库管理命令，其目的为了让动态链接库为系统所共享。
>
> ldconfig的主要用途：
>
> 默认搜寻/lilb和/usr/lib，以及配置文件/etc/ld.so.conf内所列的目录下的库文件。
>
> 搜索出可共享的动态链接库，库文件的格式为：lib***.so.**，进而创建出动态装入程序(ld.so)所需的连接和缓存文件。
>
> 缓存文件默认为/etc/ld.so.cache，该文件保存已排好序的动态链接库名字列表。
>
> ldconfig通常在系统启动时运行，而当用户安装了一个新的动态链接库时，就需要手工运行这个命令。

#### make

OK ，可以开始编译了，在 caffe 目录下执行 ：

`make all -j8`

 这是如果之前的配置或安装出错，那么编译就会出现各种各样的问题，所以前面的步骤一定要细心。

报错:

```
.build_release/lib/libcaffe.so: undefined reference to `boost::re_detail::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
```

解决:
在Makefile文件中，
`LIBRARIES += boost_thread stdc++ ` 修改为
`LIBRARIES += boost_thread stdc++  boost_regex`

#### runtest

编译成功后可运行测试：

`make runtest -j8`

- make runtest失败 

```shell
错误：
.build_release/tools/caffe: error while loading shared libraries:  libopencv.so.3.2: cannot open shared object file: No such file or  directory 
```

解决：

 ```shell
cd caffe-master
sudo ldconfig
 ```

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

### 安装pycaffe

#### 安装依赖包

```
sudo apt-get install python-numpy
```

```shell
sudo echo export PYTHONPATH="$CAFFE_EROOT/python" >> ~/.bashrc
source ~/.bashrc
```

```
pip install -U scikit-image #若没有安装pip: sudo apt install python-pip
```

- 问题

```shell
ImportError: No module named google.protobuf.internal
solution:
sudo pip install protobuf
```

- 问题

解决import caffe :RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility问题

解决方法：

numpy版本不合适：

```
sudo pip uninstall numpy
sudo pip install numpy==1.14.5
```

#### make

```
make pycaffe -j8
```

#### 验证

验证一下是否可以在 python 中导入 caffe 包，首先进入 python 环境：

```
python
```

然后导入 caffe :

```
>>> import caffe
```

### 配置notebook环境

首先要安装python接口依赖库，在caffe根目录的python文件夹下，有一个requirements.txt的清单文件，上面列出了需要的依赖库，按照这个清单安装就可以了。

在安装scipy库的时候，需要fortran编译器（gfortran)，如果没有这个编译器就会报错，因此，我们可以先安装一下。

**首先进入 caffe/python 目录下**，执行安装代码：

```
sudo apt-get install gfortran
for req in $(cat requirements.txt); do sudo pip install $req; done
```

**安装过程中

安装完成以后执行：

```
sudo pip install -r requirements.txt
```

就会看到，安装成功的，都会显示Requirement already satisfied, 没有安装成功的，会继续安装。

然后安装 jupyter ：

```
sudo pip install jupyter
```

安装完成后运行 notebook :

```
jupyter notebook
或
ipython notebook
```