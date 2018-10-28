### change theme(比如如改变书写区域的宽度)

主要通过CSS(Cascade Style Sheets) 实现

refer to  `Help->Change Themes`

[Change Width of Writing Area](https://support.typora.io/Width-of-Writing-Area/)

Example CSS:

```css
#write {
  max-width: 1800px; /*adjust writing area position*/
}
```

### Install

#### deb安装:最佳方案

<https://aur.archlinux.org/packages/typora/>  下面有deb的链接，可以直接下载

[https://typora.io/./linux/typora_0.9.53_amd64.deb](https://typora.io/linux/typora_0.9.53_amd64.deb)

再sudo dpkg -l 安装就行

#### 官网安装方案:

<https://www.typora.io/#linux>

```shell
# optional, but recommended
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
# add Typora's repository
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update
# install typora
sudo apt-get install typora
```

公司下载不成功,用手机网络也不行，连网站都上不去。

在寝室,按照上述步骤安装成功。

#### 官网 binary file

翻墙在官网下载了binary file，可以运行

the binary file vesion can exectue in commond line after adding it's directory to PATH,but cant find in open with list

### USE
- apt-get version can execute in comonde line,and can be find in open with list

  

