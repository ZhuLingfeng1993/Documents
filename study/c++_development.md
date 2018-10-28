[在linux环境下编译C++ 程序](https://www.cnblogs.com/ucas/p/5778664.html)

[简单的makeFile文件](https://www.cnblogs.com/Bw98blogs/p/7297007.html)

[Linux 开发 | 学习 Makefile](https://www.jianshu.com/p/5982ccb87af0)

### Cmake

[CMake简要教程](https://www.jianshu.com/p/bbf68f9ddffa)

[【C/C++】从零开始的cmake教程](https://blog.csdn.net/gg_18826075157/article/details/72780431)

参考文献：

入门首先：<http://www.hahack.com/codes/cmake/#>

官方教程：<https://cmake.org/cmake-tutorial/>

官方教程译文：<https://juejin.im/post/5a72775d6fb9a01cac187e96>

简单操作语法：<https://learnxinyminutes.com/docs/cmake/>

官方cmake、ctest、cpack介绍：<https://cmake.org/cmake/help/v3.11/>

源码例程：<https://gitee.com/qccz123456/learn_cmake>，通过git log可查看具体每一步的步骤。

书籍：<http://sewm.pku.edu.cn/src/paradise/reference/CMake%20Practice.pdf>



#### [cmake:用add_subdirectory()添加外部项目文件夹](https://blog.csdn.net/10km/article/details/51889385)

```
add_subdirectory(project_dir project_name.out)
```





[Using OpenCV with gcc and CMake](https://docs.opencv.org/master/db/df5/tutorial_linux_gcc_cmake.html)

#### to_string

要使用to_string()这个函数，必须让编译器支持C++11的标准，这个函数是C++11提出的

要在CMake中使用C++11，只要在CMakeLists.txt中添加一行：

```c++
add_definitions(-std=c++11)
```

[Linux 中C/C++ search path（头文件搜索路径）](https://www.cnblogs.com/jhj117/p/8671459.html)

在Linux终端执行了这条指令：

> `cpp -v /dev/null -o /dev/null`



[Linux中C/C++编译添加头文件和库路径方式](https://blog.csdn.net/yusiguyuan/article/details/16950547)

[linux系统编译C++程序时头文件和库文件搜索路径](https://blog.csdn.net/dodo_check/article/details/8393407)



[新手必看：C++跨linux与windows编程的差异之处](http://qiusuoge.com/12485.html) 第12点

[C/C++，windows 和 linux 获取目录下文件列表的方法](https://blog.csdn.net/ernest68028/article/details/78475739)