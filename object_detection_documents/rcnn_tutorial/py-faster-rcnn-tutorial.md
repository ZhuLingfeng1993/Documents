# 结构

Fast RCNN) + py-faster-rcnn

前者为caffe实现, 需要编译, 

后者为python实现 faster rcnn部分, 不需编译

# 安装

主要参考官网README

build caffe这一步时报错:

```shell
In file included from ./include/caffe/util/device_alternate.hpp:40:0,
                 from ./include/caffe/common.hpp:19,
                 from ./include/caffe/blob.hpp:8,
                 from ./include/caffe/layers/hinge_loss_layer.hpp:6,
                 from src/caffe/layers/hinge_loss_layer.cpp:4:
./include/caffe/util/cudnn.hpp: In function ‘void caffe::cudnn::setConvolutionDesc(cudnnConvolutionStruct**, cudnnTensorDescriptor_t, cudnnFilterDescriptor_t, int, int, int, int)’:
./include/caffe/util/cudnn.hpp:107:3: error: too few arguments to function ‘cudnnStatus_t cudnnSetConvolution2dDescriptor(cudnnConvolutionDescriptor_t, int, int, int, int, int, int, cudnnConvolutionMode_t, cudnnDataType_t)’
   CUDNN_CHECK(cudnnSetConvolution2dDescriptor(*conv,
   ^
In file included from ./include/caffe/util/cudnn.hpp:5:0,
                 from ./include/caffe/util/device_alternate.hpp:40,
                 from ./include/caffe/common.hpp:19,
                 from ./include/caffe/blob.hpp:8,
                 from ./include/caffe/layers/hinge_loss_layer.hpp:6,
                 from src/caffe/layers/hinge_loss_layer.cpp:4:
/usr/local/cuda/include/cudnn.h:539:27: note: declared here
 cudnnStatus_t CUDNNWINAPI cudnnSetConvolution2dDescriptor( cudnnConvolutionDescriptor_t convDesc,
                           ^
In file included from ./include/caffe/util/device_alternate.hpp:40:0,
                 from ./include/caffe/common.hpp:19,
                 from ./include/caffe/blob.hpp:8,
                 from ./include/caffe/layers/hinge_loss_layer.hpp:6,
                 from src/caffe/layers/hinge_loss_layer.cpp:4:
./include/caffe/util/cudnn.hpp: In function ‘void caffe::cudnn::createPoolingDesc(cudnnPoolingStruct**, caffe::PoolingParameter_PoolMethod, cudnnPoolingMode_t*, int, int, int, int, int, int)’:
./include/caffe/util/cudnn.hpp:126:3: error: too few arguments to function ‘cudnnStatus_t cudnnSetPooling2dDescriptor(cudnnPoolingDescriptor_t, cudnnPoolingMode_t, cudnnNanPropagation_t, int, int, int, int, int, int)’
   CUDNN_CHECK(cudnnSetPooling2dDescriptor(*pool_desc, *mode, h, w,
   ^
In file included from ./include/caffe/util/cudnn.hpp:5:0,
                 from ./include/caffe/util/device_alternate.hpp:40,
                 from ./include/caffe/common.hpp:19,
                 from ./include/caffe/blob.hpp:8,
                 from ./include/caffe/layers/hinge_loss_layer.hpp:6,
                 from src/caffe/layers/hinge_loss_layer.cpp:4:
/usr/local/cuda/include/cudnn.h:1033:27: note: declared here
 cudnnStatus_t CUDNNWINAPI cudnnSetPooling2dDescriptor(

```

百度错误: 

> caffe编译成功，但在编译caffe-fast-rcnn时报错，也就是说我的电脑新装的caffe和cuda，cndnn的版本是对应的。并且，在注释掉cudnn时，caffe-fast-rcnn的编译不出错。因此考虑作者发布的源码中caffe的版本较低，于我的7.0cudnn版本不匹配，因此需要对caffe-fast-rcnn中涉及cudnn的文件全部替换为原先可以成功编译的caffe文件。
>
> 作者：yes蒋淼淼 
> 来源：CSDN 
> 原文：https://blog.csdn.net/jmt330/article/details/78568876 
> 版权声明：本文为博主原创文章，转载请附上博文链接！

另外官网README中:

> **NOTE** If you are having issues compiling and you are using a recent version of CUDA/cuDNN, please consult [this issue](https://github.com/rbgirshick/py-faster-rcnn/issues/509?_pjax=%23js-repo-pjax-container#issuecomment-284133868) for a workaround

‘this issue’ :

```shell
To enable supports of CUDNNv5:
1).
cd caffe-fast-rcnn
git remote add caffe https://github.com/BVLC/caffe.git
git fetch caffe
git merge -X theirs caffe/master

2).
remove self_.attr("phase") = static_cast<int>(this->phase_); from include/caffe/layers/python_layer.hpp after merging.

3). (in caffe-fast-rcnn)
- mkdir build && cd build
- cmake ..
- make all -j8
- make pycaffe -j8
```

报错的根本原因是faster-rcnn的caffe代码与我使用的CUDA/cuDNN版本不兼容, 前者更旧, 所以要更新代码, 参照这个issue可以解决(修改了Makefile.config, 没有修改Makefile)

另外, caffe可以用make或cmake编译(http://caffe.berkeleyvision.org/installation.html)