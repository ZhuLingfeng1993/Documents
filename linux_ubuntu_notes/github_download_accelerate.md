https://www.jianshu.com/p/c96dc32eca35
https://blog.csdn.net/it_xiao_bai/article/details/80692152
https://github.com/googlehosts/hosts

IPv6 连接测试：test-ipv6.com

Hosts是一个没有扩展名的系统文件，可以用记事本等工具打开，其作用就是将一些常用的网址域名与其对应的IP地址建立一个关联“数据库”，当用户在浏览器中输入一个需要登录的网址时，系统会首先自动从Hosts文件中寻找对应的IP地址，一旦找到，系统会立即打开对应网页，如果没有找到，则系统会再将网址提交DNS域名解析服务器进行IP地址的解析。
需要注意的是，Hosts文件配置的映射是静态的，如果网络上的计算机更改了请及时更新IP地址，否则将不能访问。



## 具体解决过程

在本地host文件中添加映射，关于hosts的作用这里就不做声明了。

- windows系统的hosts文件的位置如下：

  > C:\Windows\System32\drivers\etc\hosts

- mac/linux系统的hosts文件的位置如下：

  > /etc/hosts

具体步骤如下：

> 1. 用文本编辑器打开hosts文件
>
> 2. 访问ipaddress网站<https://www.ipaddress.com/>，查看网站对应的IP地址，输入网址则可查阅到对应的IP地址，这是一个查询域名映射关系的工具
>
> 3. 查询 github.global.ssl.fastly.net 和 github.com 两个地址
>
> 4. 多查几次，选择一个稳定，延迟较低的 ip 按如下方式添加到host文件的最后面
>
>    151.101.185.194  github.global.ssl.fastly.net
>    192.30.253.112  github.com
>
> 5. 保存hosts文件
>
> 6. 重启浏览器，或刷新DNS缓存，告诉电脑hosts文件已经修改，linux/mac执行sudo /etc/init.d/networking restart命令；windows在cmd中输入ipconfig /flushdns命令即可。
>
> 7. 起飞！！！