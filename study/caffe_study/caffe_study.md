### GPU编程

- 了解GPU原理

  CPU把数据全部读到内存?看看内存占用（当前的数据比较小，数据大的时侯(imageNet,COCO)可能会存在问题

  [GPU计算的原理](https://blog.csdn.net/horsefoot/article/details/71183880)

  CS231n lecutre 8

- 了解GPU编程

  [ CUDA编程入门极简教程](https://blog.csdn.net/l7H9JA4/article/details/79831042)

### 了解Caffe的GPU编程

要自己写一个层还是比较吃力的

[wiki:Developing new layers](https://github.com/BVLC/caffe/wiki/Development)

[解析：深度学习框架Caffe源码](https://www.leiphone.com/news/201612/oZUj5d437bpSl5wc.html)

[caffe的一些源码分析](https://blog.csdn.net/seven_first/article/category/5721883)

[梳理caffe代码](https://so.csdn.net/so/search/s.do?q=%E6%A2%B3%E7%90%86caffe%E4%BB%A3%E7%A0%81&t=blog&u=langb2014)

[caffe的各种使用](http://www.cnblogs.com/denny402/tag/caffe/)

###### 看看OPENCL实现

网上找到的OpenCL版的Caffe是最基本的caffe, 相对与我们当前的Caffe-SSD, 有很多层都没有OpenCL实现

另外, OpenCL实现与CUDA实现有些对应关系,有些只是函数替换或修改,有些则改动较大, 另外配置似乎比较麻烦

### caffe wiki 

https://github.com/BVLC/caffe/wiki

#### [Development](https://github.com/BVLC/caffe/wiki/Development)

### caffe的python接口

相关文件都在`$CAFFE_ROOT/python`下，但基本没有什么实质性的代码，只是对caffe c++代码的封装，所以帮助文档也帮助不了什么

> - `caffe.Net` is the central interface for loading, configuring, and running models. `caffe.Classifier` and `caffe.Detector` provide convenience interfaces for common tasks.
> - `caffe.SGDSolver` exposes the solving interface.
> - `caffe.io` handles input / output with preprocessing and protocol buffers.
> - `caffe.draw` visualizes network architectures.
> - Caffe blobs are exposed as numpy ndarrays for ease-of-use and efficiency.



具体使用，参照examples 

###### Net

```python
import caffe 
from caffe import layers as L
from caffe import params as P

n=caffe.NetSpec()

n.output_layer_name = L.SomeNameLayer(n.input_layer_name,             numeric_param_name = numeric_param_value, dict_param_name = dict_param_value, enum_param_name = P.SomeName.enum_param_value)

proto = n.to_proto()

with open('mnist/lenet_auto_train.prototxt', 'w') as f:
    f.write(str(proto))
```

其中，SomeNameLayer是caffe.proto中定义的层，各种param_name也根据caffe.proto中定义

ReLU(n.input_layer_name, in_place=True)

dict_param_value = dict(key1=value1, ...)

两个output_layer: 

`n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB, source=lmdb,transform_param=dict(scale=1./255), ntop=2)`

###### Solver

```python
solver_param = {
    key1:value1
    ...
}

# Create solver.
solver = caffe_pb2.SolverParameter(
        train_net=train_net_file,
        test_net=[test_net_file],
        snapshot_prefix=snapshot_prefix,
        **solver_param)
```

###### Train/Test



为什么卷基层没有bias?也许要集中通过BN的偏移实现？

### 权重初始化

https://www.cnblogs.com/tianshifu/p/6165809.html

在caffe/include/caffe中的 filler.hpp文件中有它的源文件

文件  filler.hpp提供了7种权值初始化的方法，分别为：常量初始化（constant）、高斯分布初始化（gaussian）、positive_unitball初始化、均匀分布初始化（uniform）、xavier初始化、msra初始化、双线性初始化（bilinear）。

在prototxt中用各种filler实现，weight_filler, bias_filler

```protobuf
message FillerParameter {
  // The filler type.
  optional string type = 1 [default = 'constant'];
  optional float value = 2 [default = 0]; // the value in constant filler
```

### bias

是否使用：bias_term 

```protobuf
message ConvolutionParameter {
  optional uint32 num_output = 1; // The number of outputs for the layer
  optional bool bias_term = 2 [default = true]; // whether to have bias terms
```

### solver param

正则化：weight_decay

周期epoch：display=num_train_img/batch_size

优化方法：type:ADAM

### 预处理

发现一些prob参数，按照一定概率进行处理，因为由于训练过程一张图片很可能处理许多次，所以达到了对图片的各种可能的随机预处理

###### 零均值中心化和归一化

需要对训练的数据计算mean_value(tools/compute_image_mean/cpp),然后都除以255

注意训练时减去了一个mean_value,验证、测试、以及最后使用时的inference之前的预处理都要用这个mean_value(scale参数也是一样)

### 如何写自己的caffe层

详见网页书签

有用C++和python写的

另外注意caffe的wiki部分，上面有很多资源

如果已经有C++层实现，可以直接写python层，不用自己实现

### caffe工具和可视化

$CAFFE_ROOT/tools/extra 下的文件

#### NetScope：prototxt可视化

http://ethereon.github.io/netscope/#/editor

###### NetScope脱机(localhost)使用

```shell
需要：
1.linux下
2.python2，或python3

方法：
step1：git clone https://github.com/ethereon/netscope
step2：cd netscope
step3:  python -m SimpleHTTPServer 8000 或者 python3 -m http.server 8000
step4:  打开浏览器，敲入本机地址: http://localhost: 8000或者0.0.0.0： 8000
注：step3中的8000可变。
```



#### summarize(prototxt)

```
AttributeError: 'module' object has no attribute 'text_format'
```

```
修改如下：
#from google import protobuf
from google.protobuf import text_format

        #protobuf.text_format.Parse(f.read(), net)
        text_format.Parse(f.read(), net)
```

summarize的结果有些细节看不懂

#### 训练日志可视化（曲线）

！！！！！

https://blog.csdn.net/u011607316/article/details/69223030！！！！！

###### 参考资料

https://blog.csdn.net/u011070171/article/details/52936205

https://blog.csdn.net/zziahgf/article/details/79215862

###### 使用方法

```shell
python parse_log.py 
./plot_training_log.py.example
```

具体用法参见帮助

###### 问题及解决

```shell
笔记本上运行
./plot_training_log.py.example  0 demo.py train_MobileNet_VOC0712_SSD_300x300_20180728133519.log
```

```shell
Traceback (most recent call last):
  File "./plot_training_log.py.example", line 6, in <module>
    import matplotlib.cm as cmx
  File "/usr/local/lib/python2.7/dist-packages/matplotlib/__init__.py", line 131, in <module>
    from matplotlib.rcsetup import defaultParams, validate_backend, cycler
  File "/usr/local/lib/python2.7/dist-packages/matplotlib/rcsetup.py", line 29, in <module>
    from matplotlib.fontconfig_pattern import parse_fontconfig_pattern
  File "/usr/local/lib/python2.7/dist-packages/matplotlib/fontconfig_pattern.py", line 28, in <module>
    from backports.functools_lru_cache import lru_cache
ImportError: No module named functools_lru_cache
```

  根本上来说是`import matplotlib.cm as cmx`的问题，发现`import matplotlib` ok

```python
import matplotlib.cm
ImportError: cannot import name cbook
```

百度搜索问题，结果https://www.cnblogs.com/go-better/p/7737551.html，https://blog.csdn.net/chris_pei/article/details/79047863

原来安装matplotlib用的命令是：

```
 sudo pip install matplotlib
```

这样就会有问题，不知道啥情况。卸掉matplotlib：

```
sudo pip uninstall matplotlib
```

换成

```
sudo apt-get install python-matplotlib
```

就没以上两个问题了。



### batchnorm

首先去看看batchnorm的原理

其次：

> caffe中实现批量归一化（batch-normalization）需要借助两个层：BatchNorm 和 Scale  
>
> BatchNorm实现的是归一化  Scale实现的是平移和缩放 
>
> 均值和方差采用的是滑动平均的更新方式。因此，BN层共存储了3个数值：均值滑动和、方差滑动和、滑动系数和。

BN层的三个参数是不需要学习的

> 由于Scale需要实现平移功能，所以要把bias_term项设为true  

同时Scale层的缩放和平移参数是要学习的，同时又与正则化无关

> 另外，实现BatchNorm的时候需要注意一下参数use_global_stats，在训练的时候设为false，在测试的时候设为true  use_global_stats = false 时采用滑动平均计算新的均值和方差  use_global_stats = true 时会强制使用模型中存储的BatchNorm层均值与方差参数 
>
> 其实也没必要这么麻烦，因为在BathNorm层的源码中设定了如果use_global_stats缺省，那么在训练时为false，测试时为true，源代码为（caffe/src/caffe/layers/batch_norm_layer.cpp）第14行：
>
> ```
> use_global_stats_ = this->phase_ == TEST;
> ```

另外，由于Scale层有偏移了，一般将Conv层的bias_term设置成False

综上，batchNorm实现通常如下：

```protobuf
layer {
  bottom: "conv1_1"
  top: "conv1_1"
  name: "bn_conv1_1"
  type: "BatchNorm"
  param {
    lr_mult: 0
    decay_mult: 0
  }
  param {
    lr_mult: 0
    decay_mult: 0
  }
  param {
    lr_mult: 0
    decay_mult: 0
  }
}

layer {
  bottom: "conv1_1"
  top: "conv1_1"
  name: "scale_conv1_1"
  type: "Scale"
  param {
    lr_mult: 0.1
    decay_mult: 0
  }
  param {
    lr_mult: 0.1
    decay_mult: 0
  }
  scale_param {
    bias_term: true
  }
}
```

```protobuf
message BatchNormParameter {
  // If false, normalization is performed over the current mini-batch
  // and global statistics are accumulated (but not yet used) by a moving
  // average.
  // If true, those accumulated mean and variance values are used for the
  // normalization.
  // By default, it is set to false when the network is in the training
  // phase and true when the network is in the testing phase.
  optional bool use_global_stats = 1;
  // What fraction of the moving average remains each iteration?
  // Smaller values make the moving average decay faster, giving more
  // weight to the recent values.
  // Each iteration updates the moving average @f$S_{t-1}@f$ with the
  // current mean @f$ Y_t @f$ by
  // @f$ S_t = (1-\beta)Y_t + \beta \cdot S_{t-1} @f$, where @f$ \beta @f$
  // is the moving_average_fraction parameter.
  optional float moving_average_fraction = 2 [default = .999];
  // Small value to add to the variance estimate so that we don't divide by
  // zero.
  optional float eps = 3 [default = 1e-5];
}
```

### merge_bn

Caffe的BatchNorm是通过BatchNorm Layer + Scale Layer实现的

merge bn的作用？

在DSSD论文的Inference Time中有说明实现原理和效果（有时间和空间提升效果数值，但没有具体分析）

根据merge bn的原理，在离线时将Conv Layer中运算与其对应的BatchNorm Layer + Scale Laye中运算结合到一起，然后在线推理时（deploy网络）在Conv Layer中一次计算的确能减少计算量

如果BatchNorm Layer + Scale Layer采用的是InPlace计算，那merge bn对于内存的减少就可能就微乎其微了。

##### deploy网络的Conv层参数设置

由于需要将Scale Layer的偏移merge到Conv，所以Conv的bias_term必须为True(caffe 默认为True)

当然，deploy网络不是用batchNorm

### why two param?
for weight and basis

### split
prototxt可视化时一个层的多个分枝线
### 用一个文件包含train&test phase进行训练和间隔测试的问题
caffe的教程中用到了这种方式，测试数据也会被用于计算梯度，不利于模型的泛化能力，最好
不要用

### google protocol buffers

https://developers.google.com/protocol-buffers/docs/overview
类似于XML的,用于序列化结构体数据的机制，但更简单更快

definition: .proto 
message:like struct in C/C++
text formoat：.prototxt
编译（c++ .h .cpp)
各种编程语言的API

### caffe.proto 

FillerParameter 的各种type没有具体定义,应该在caffe的src中有相应cpp定义(可直接百度)
.proto只是定义了结构体数据格式，数据的操作应该是由cpp完成

### caffe 中的 engine 

caffe.proto中：

```c++
// Note: certain layers may have more than one computational engine
  // for their implementation. These layers include an Engine type and
  // engine parameter for selecting the implementation.
  // The default for the engine is set by the ENGINE switch at compile-time.

  enum Engine {
    DEFAULT = 0;
    CAFFE = 1;
    CUDNN = 2;
  }
  optional Engine engine = 15 [default = DEFAULT];
```

  其实就两种引擎CAFFE vs. cuDNN。

**default其实是cuDNN(GPU版caffe)**，可能在make里可以设置,可能GPU和CPU的default分别是CUDNN和CAFFE

要讲清两者的区别，先要说一下什么是cuDNN.
CUDA是GPU编程的API。BLAS（as you know）是矩阵运算的高度优化的函数库。cuDNN就有点像BLAS，是GPU上深度学习计算时常用的一些计算操作/函数的实现库，如卷积，Pooling, softmax, sigmoid, tanh之类的。它是针对这些操作，像BLAS一样，做了超强的优化的，性能优，内存占用小，效率高。

用它的好处，自不必说，一个功能，就不用大家，即每个框架，都自己实现一遍了，直接统一调用cuDNN库里的实现就好了。当然，不是每个layer，cuDNN都支持，所以，你可以看到，engine这个参数，只有上述部分layer里才可以定义。

###### 不同engine的实际不同

应该跟特定的层及及其实现有关，已经实验过同一网络CAFFE和CUDNN显存一样但速度后者更快，也实验过同一网络CUDNN显存更大


