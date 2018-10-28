

# The Linux Command Line Note

## Shortcuts(summary by myself) 

| Action                                                       | Keyboard shortcut        |
| ------------------------------------------------------------ | ------------------------ |
| **Move**                                                     |                          |
| Move to the start of the line                                | Ctrl+A                   |
| Move to the end of the line                                  | Ctrl+E                   |
| Move back one character                                      | Ctrl+B                   |
| Move back one word                                           | Alt+B                    |
| Move forward one character                                   | Ctrl+F                   |
| Move forward one word                                        | Alt+F                    |
| **Delete or Cut **                                           |                          |
| Erase a line(tested same as ctrl+u)                     | Ctrl+U                   |
| Delete from the cursor to the beginning of the line.         | Ctrl+u                   |
| Delete from the cursor to the end of the line.               | Ctrl+K                   |
| Delete from the cursor to the start of the word.(a word means charaters seperated by space) | Ctrl+W                   |
| Delete previous word | Esc+Backspace |
|  **Others** 					||
| Pastes text from the clipboard. (only with content cut by shortcuts above)                             | Ctrl+Y                   |
| Clear the screen leaving the current line at the top of the screen. | Ctrl+L                   |
| Reverse incremental search of history (ctrl+j to copy to commond line)                       | Ctrl+R                   |
| Reverse non-incremental search of history                    | Alt+P                    |

## some skills

### 执行脚本

- 用./path，可能会出现permission denied
- 用bash path
- sudo bash path:会给生成文件加上权限，不建议这么做，可能会出各种问题（因为权限）

### Linux 在一个命令行上执行多个命令
1. [ ; ]执行时采用并行执行方式

如果被分号(;)所分隔的命令会连续的执行下去，就算是错误的命令也会继续执行后面的命令。

例如：mkdir ddir edir;cd fdir;mkdir fdir;

建立目录ddir edir两个目录，切换到fdir；没有目录不会成功，创建目录fdir，最总成功创建ddir edir fdir三个目录

2. [ && ]执行时采用串行执行方式

如果命令被 && 所分隔，那么命令也会一直执行下去，但是中间有错误的命令存在就不会执行后面的命令，没错就直行至完为止。

例如：mkdir ddir edir&&cd fdir&&mkdir fdir;

建立目录ddir edir两个目录，切换到fdir；没有目录不会成功，创建目录fdir不再执行，最总成功创建ddir edir 两个目录

3. [ || ]执行时采用until执行方式，一旦遇到正确的命令就停止执行命令

如果每个命令被双竖线 || 所分隔，那么一遇到可以执行成功的命令就会停止执行后面的命令，而不管后面的命令是否正确与否。如果执行到错误的命令就是继续执行后一个命令，一直执行到遇到正确的命令为止。

例如：cd edir || cd fdir|| mkdir gdir || cd gdir;

切换到edir目录不成功，执行换到fdir目录不成功，创建目录gdir就会执行，切换进gdir目录就不会执行，最总成功创建gdir 目录并不能切换进目录。

人就像是被蒙着眼推磨的驴子，生活就像一条鞭子；当鞭子抽到你背上时，你就只能一直往前走，虽然连你也不知道要走到什么时候为止，便一直这么坚持着。

## About Shell

shell :就是一个程序，它接受从键盘输入的命令， 然后把命令传递给操作系统去执行
bash :来自 GNU 项目的 shell 程序
terminal:当使用图形用户界面时，我们需要另一个和 shell 交互的叫做终端仿真器的程序
X 窗口系统 :（使 GUI 工作的底层引擎）

ls    		#列出当前目录中的文件
ls *  		#列出当前目录及下一级目录中的文件
ls */*		#列出当前目录中所有下一级目录中的文件
ls */*/* 	#由上面类推

## file and directory

cp -r dir1 dir2  #将dir1目录本身及其下面所有文件 拷贝到dir2下， 也就是dir2/dir1
cp -r dir/* dir2 #将dir1下面所有文件 拷贝到dir2下

cp dir1/* dir2	#使用一个通配符，在目录 dir1 中的所有文件（目录不能被复制）都被复制到目录 dir2 中。 dir2 必须已经存在。
cp -r dir1 dir2	
>复制目录 dir1 中的内容到目录 dir2。如果目录 dir2 不存在， 
>创建目录 dir2，操作完成后，目录 dir2 中的内容和 dir1 中的一样。 
>如果目录 dir2 存在，则目录 dir1 (和目录中的内容)将会被复制到 dir2 中。

对目录进行操作（复制，移动，删除），必需要用 -r

>小贴士。 当你使用带有通配符的rm命令时（除了仔细检查输入的内容外）， 
 用 ls 命令来测试通配符。这会让你看到将要被删除的文件是什么。
 后按下上箭头按键，重新调用 刚刚执行的命令，用 rm 替换 ls。				

#####重命名：
mv dir1 dir2
如果目录 dir2 已经存在，mv 命令会把 dir1 移动到 dir2 目录中。
如果 dir2 不存在， mv 会把dir1重命名为 dir2。

#####Link
当建立符号链接时，你既可以使用绝对路径名：也可用相对路径名。
使用相对路径名更令人满意， 因为它允许一个包含符号链接的目录重命名或移动，而不会破坏链接。

对于符号链接，有一点值得记住，执行的大多数文件操作是针对链接的对象，而不是链接本身。
 而 rm 命令是个特例。当你删除链接的时候，删除链接本身，而不是链接的对象

## Linux 系统中的目录

| 目录           | 评论                                                         |
| -------------- | ------------------------------------------------------------ |
| /              | 根目录，万物起源。                                           |
| /bin           | 包含系统启动和运行所必须的二进制程序。                       |
| /boot          | 包含 Linux 内核、初始 RAM 磁盘映像（用于启动时所需的驱动）和 启动加载程序。有趣的文件：/boot/grub/grub.conf or menu.lst， 被用来配置启动加载程序。/boot/vmlinuz，Linux 内核。 |
| /dev           | 这是一个包含设备结点的特殊目录。“一切都是文件”，也适用于设备。 在这个目录里，内核维护着所有设备的列表。 |
| /etc           | 这个目录包含所有系统层面的配置文件。它也包含一系列的 shell 脚本， 在系统启动时，这些脚本会开启每个系统服务。这个目录中的任何文件应该是可读的文本文件。有趣的文件：虽然/etc 目录中的任何文件都有趣，但这里只列出了一些我一直喜欢的文件：/etc/crontab， 定义自动运行的任务。/etc/fstab，包含存储设备的列表，以及与他们相关的挂载点。/etc/passwd，包含用户帐号列表。 |
| /home          | 在通常的配置环境下，系统会在/home 下，给每个用户分配一个目录。普通用户只能 在自己的目录下写文件。这个限制保护系统免受错误的用户活动破坏。 |
| /lib           | 包含核心系统程序所使用的共享库文件。这些文件与 Windows 中的动态链接库相似。 |
| /lost+found    | 每个使用 Linux 文件系统的格式化分区或设备，例如 ext3文件系统， 都会有这个目录。当部分恢复一个损坏的文件系统时，会用到这个目录。这个目录应该是空的，除非文件系统 真正的损坏了。 |
| /media         | 在现在的 Linux 系统中，/media 目录会包含可移动介质的挂载点， 例如 USB 驱动器，CD-ROMs 等等。这些介质连接到计算机之后，会自动地挂载到这个目录结点下。 |
| /mnt           | 在早些的 Linux 系统中，/mnt 目录包含可移动介质的挂载点。     |
| /opt           | 这个/opt 目录被用来安装“可选的”软件。这个主要用来存储可能 安装在系统中的商业软件产品。 |
| /proc          | 这个/proc 目录很特殊。从存储在硬盘上的文件的意义上说，它不是真正的文件系统。 相反，它是一个由 Linux 内核维护的虚拟文件系统。它所包含的文件是内核的窥视孔。这些文件是可读的， 它们会告诉你内核是怎样监管计算机的。 |
| /root          | root 帐户的家目录。                                          |
| /sbin          | 这个目录包含“系统”二进制文件。它们是完成重大系统任务的程序，通常为超级用户保留。 |
| /tmp           | 这个/tmp 目录，是用来存储由各种程序创建的临时文件的地方。一些配置导致系统每次 重新启动时，都会清空这个目录。 |
| /usr           | 在 Linux 系统中，/usr 目录可能是最大的一个。它包含普通用户所需要的所有程序和文件。 |
| /usr/bin       | /usr/bin 目录包含系统安装的可执行程序。通常，这个目录会包含许多程序。 |
| /usr/lib       | 包含由/usr/bin 目录中的程序所用的共享库。                    |
| /usr/local     | 这个/usr/local 目录，是非系统发行版自带程序的安装目录。 通常，由源码编译的程序会安装在/usr/local/bin 目录下。新安装的 Linux 系统中会存在这个目录， 并且在管理员安装程序之前，这个目录是空的。 |
| /usr/sbin      | 包含许多系统管理程序。                                       |
| /usr/share     | /usr/share 目录包含许多由/usr/bin 目录中的程序使用的共享数据。 其中包括像默认的配置文件、图标、桌面背景、音频文件等等。 |
| /usr/share/doc | 大多数安装在系统中的软件包会包含一些文档。在/usr/share/doc 目录下， 我们可以找到按照软件包分类的文档。 |
| /var           | 除了/tmp 和/home 目录之外，相对来说，目前我们看到的目录是静态的，这是说， 它们的内容不会改变。/var 目录存放的是动态文件。各种数据库，假脱机文件， 用户邮件等等，都位于在这里。 |
| /var/log       | 这个/var/log 目录包含日志文件、各种系统活动的记录。这些文件非常重要，并且 应该时时监测它们。其中最重要的一个文件是/var/log/messages。注意，为了系统安全，在一些系统中， 你必须是超级用户才能查看这些日志文件 |

## use commond
 注意表示法：出现在命令语法说明中的方括号，表示可选的项目。一个竖杠字符 表示互斥选项。
## redirect
程序，比方说 ls，实际上把他们的运行结果 输送到一个叫做标准输出的特殊文件（经常用 stdout 表示），
而它们的状态信息则送到另一个 叫做标准错误的文件（stderr）。默认情况下，标准输出和标准错误都连接到屏幕，
而不是 保存到磁盘文件。除此之外，许多程序从一个叫做标准输入（stdin）的设备得到输入，默认情况下， 标准输入连接到键盘。

使用 “>” 重定向符后接文件名将标准输出重定向到除屏幕 以外的另一个文件。

如果我们需要清空一个文件内容（或者创建一个 新的空文件），可以使用这样的技巧：
[me@linuxbox ~]$ > ls-output.txt

把重定向结果追加到文件内容后面，而不是从开头重写文件？为了这个目的， 我们使用”>>“重定向符，

一个程序可以在几个编号的文件流中的任一个上产生输出，前 三个称作标准输入、输出和错误，
shell 内部分别将其称为文件描述符0、1和2。
重定向标准错误：
$ ls -l /bin/usr 2> ls-error.txt
重定向标准输出和错误到同一个文件：
 $ ls -l /bin/usr > ls-output.txt 2>&1
注意重定向的顺序安排非常重要。标准错误的重定向必须总是出现在标准输出 重定向之后，要不然它不起作用。
如果命令顺序改为：
 $ ls -l /bin/usr 2>&1 >ls-output.txt
则标准错误定向到屏幕。

现在的 bash 版本提供了第二种方法，更精简合理的方法来执行这种联合的重定向。
$ ls -l /bin/usr &> ls-output.txt

##### cat

cat 命令读取一个或多个文件，然后复制它们到标准输出
如果 cat 没有给出任何参数，它会从标准输入读入数据，又因为标准输入默认情况下连接到键盘， 它正在等待我们输入数据！
下一步，输入 Ctrl-d（按住 Ctrl 键同时按下”d”），来告诉 cat，在标准输入中， 它已经到达文件末尾（EOF）
使用“<”重定向操作符，我们把标准输入源从键盘改到文件

##### pip 

使用管道操作符”|”（竖杠），一个命令的标准输出可以通过管道送至另一个命令的标准输入：
command1 | command2
比如：$ ls -l /usr/bin | less



wc (word count) ：显示文件中包含的行数，单词数和字节数

grep 是个很强大的程序，用来找到文件中的匹配文本。这样使用 grep 命令：
grep pattern [file...]
比如说，我们想在我们的程序列表中，找到文件名中包含单词”zip”的所有文件：
[me@linuxbox ~]$ ls /bin /usr/bin | sort | uniq | grep zip

head / tail － 打印文件开头部分/结尾部分
默认情况下，两个命令 都打印十行文本，但是可以通过”-n”选项来调整命令打印的行数。
tail 有一个选项允许你实时地浏览文件。当观察日志文件的进展时，这很有用，因为 它们同时在被写入。
使用”-f”选项，tail 命令继续监测这个文件，当新的内容添加到文件后，它们会立即 出现在屏幕上。这会一直继续下去直到你输入 Ctrl-c。

##### tee



Linux 提供了一个叫做 tee 的命令，这个命令制造了 一个”tee”，(管道上的T型接头)安装到我们的管道上。
tee 程序从标准输入读入数据，并且同时复制数据 到标准输出（允许数据继续随着管道线流动）
和一个或多个文件。当在某个中间处理 阶段来捕捉一个管道线的内容时，这很有帮助。



`tee -a  `追加内容到文件,而非覆盖

## (字符)展开([从 shell 眼中看世界](http://billie66.github.io/TLCL/book/chap08.html))

#### 算术表达式展开



shell 在展开中执行算数表达式。这允许我们把 shell 提示当作计算器来使用：

```shell
$((expression))
```

（以上括号中的）表达式是指算术表达式，它由数值和算术操作符组成。

算术表达式只支持整数（全部是数字，不带小数点），但是能执行很多不同的操作。这里是一些它支持的操作符：+,-*,/,%,**



### 花括号+展开

Perhaps the strangest expansion is called brace expansion. With it, you can createmultiple text strings from a pattern containing braces. Here’s an example:

可能最奇怪的展开是花括号展开。通过它，你可以从一个包含花括号的模式中创建多个文本字符串。这是一个例子：

```
[me@linuxbox ~]$ echo Front-{A,B,C}-Back
Front-A-Back Front-B-Back Front-C-Back

```

Patterns to be brace expanded may contain a leading portion called a preamble and atrailing portion called a postscript. The brace expression itself may contain either acomma-separated list of strings, or a range of integers or single characters. The patternmay not contain embedded whitespace. Here is an example using a range of integers:

花括号展开模式可能包含一个开头部分叫做报头，一个结尾部分叫做附言。花括号表达式本身可能包含一个由逗号分开的字符串列表，或者一个整数区间，或者单个的字符的区间。这种模式不能嵌入空白字符。这个例子中使用了一个整数区间：

```shell
[me@linuxbox ~]$ echo Number_{1..5}
Number_1  Number_2  Number_3  Number_4  Number_5
```

最常见的应用是，创建一系列的文件或目录列表。例如， 如果我们是摄影师，有大量的相片。我们想把这些相片按年月先后组织起来。首先， 我们要创建一系列以数值”年－月”形式命名的目录。通过这种方式，可以使目录名按照 年代顺序排列。

### 双引号

我们将要看一下引用的第一种类型，双引号。如果你把文本放在双引号中，shell 使用的特殊字符，都失去它们的特殊含义，被当作普通字符来看待。有几个例外： $，\ (反斜杠），和 `（倒引号）。**这意味着单词分割、路径名展开、波浪线展开和花括号展开都将失效，然而参数展开、算术展开和命令替换仍然执行。**使用双引号，我们可以处理包含空格的文件名。

### 单引号

If we need to suppress all expansions, we use single quotes. Here is a comparison ofunquoted, double quotes, and single quotes:

如果需要禁止所有的展开，我们要使用单引号。

### 转义字符

使用转义字符来消除文件名中一个字符的特殊含义，是很普遍的。例如，在文件名中可能使用
一些对于 shell 来说有特殊含义的字符。这些字符包括”$”, “!”, “ “等字符。

反斜杠除了作为转义字符外，也可以构成一种表示法，来代表某种
特殊字符，这些特殊字符叫做控制码。ASCII 编码表中前32个字符被用来把命令转输到电报机
之类的设备

echo 命令带上 ‘-e’ 选项，能够解释转义序列。你可以把转义序列放在 $' ' 里面。以下例子中，我们可以使用 sleep 命令创建一个简单的倒数计数器（ sleep 是一个简单的程序，它会等待指定的秒数，然后退出）：

*sleep 10; echo -e "Time's up\a"*

### 总结归纳



随着我们继续学习 shell，你会发现使用展开和引用的频率逐渐多起来，所以能够很好的理解它们的工作方式很有意义。事实上，可以这样说，它们是学习 shell 的最重要的主题。如果没有准确地理解展开模式，shell 总是神秘和混乱的源泉，并且 shell 潜在的能力也浪费掉了。

## 使用命令

 在这之前，我们已经知道了一系列神秘的命令，每个命令都有自己奇妙的 选项和参数。在这一章中，我们将试图去掉一些神秘性，甚至创建我们自己 的命令。这一章将介绍以下命令：

- type – Indicate how a command name is interpreted
- type – 说明怎样解释一个命令名
- which – Display which executable program will be executed
- which – 显示会执行哪个可执行程序
- man – Display a command’s manual page
- man – 显示命令手册页
- apropos – Display a list of appropriate commands
- apropos – 显示一系列适合的命令
- info – Display a command’s info entry
- info – 显示命令 info
- whatis – Display a very brief description of a command
- whatis – 显示一个命令的简洁描述
- alias – Create an alias for a command
- alias – 创建命令别名

## 键盘高级操作技巧

### 命令行编辑

| 按键   | 行动                                                   |
| ------ | ------------------------------------------------------ |
| Ctrl-a | 移动光标到行首。                                       |
| Ctrl-e | 移动光标到行尾。                                       |
| Ctrl-f | 光标前移一个字符；和右箭头作用一样。                   |
| Ctrl-b | 光标后移一个字符；和左箭头作用一样。                   |
| Alt-f  | 光标前移一个字。                                       |
| Alt-b  | 光标后移一个字。                                       |
| Ctrl-l | 清空屏幕，移动光标到左上角。clear 命令完成同样的工作。 |

| 按键          | 行动                                                         |
| ------------- | ------------------------------------------------------------ |
| Ctrl-k        | 剪切从光标位置到行尾的文本。                                 |
| Ctrl-u        | 剪切从光标位置到行首的文本。                                 |
| Alt-d         | 剪切从光标位置到词尾的文本。                                 |
| Alt-Backspace | 剪切从光标位置到词头的文本。如果光标在一个单词的开头，剪切前一个单词。 |
| Ctrl-y        | 把剪切环中的文本粘贴到光标位置。                             |

### 搜索历史命令

在任何时候，我们都可以浏览历史列表的内容，通过：

```shell
[me@linuxbox ~]$ history | less
```

bash 也具有按递增顺序来搜索历史列表的能力。这意味着随着字符的输入，我们
可以告诉 bash 去搜索历史列表，每一个附加字符都进一步提炼我们的搜索。启动递增搜索，
输入 Ctrl-r，其后输入你要寻找的文本。当你找到它以后，你可以敲入 Enter 来执行命令，
或者输入 Ctrl-j，从历史列表中复制这一行到当前命令行。再次输入 Ctrl-r，来找到下一个
匹配项（向上移动历史列表）。输入 Ctrl-g 或者 Ctrl-c，



## shell 环境

shell 在 shell 会话中保存着大量信息。这些信息被称为 (shell 的) 环境。
程序获取环境中的数据（即环境变量）来了解本机的配置。虽然大多数程序用配置文件来存储程序设置，
一些程序会根据环境变量来调整他们的行为。知道了这些，我们就可以用环境变量来自定制 shell 体验。

- printenv - 打印部分或所有的环境变量
- set - 设置 shell 选项
- export — 导出环境变量，让随后执行的程序知道。
- alias - 创建命令别名

| PATH | 由冒号分开的目录列表，当你输入可执行程序名后，会搜索这个目录列表。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

### 如何建立 shell 环境？

当我们登录系统后， bash 程序启动，并且会读取一系列称为启动文件的配置脚本，这些文件定义了默认的可供所有用户共享的 shell 环境。然后是读取更多位于我们自己家目录中的启动文件，这些启动文件定义了用户个人的 shell 环境。确切的启动顺序依赖于要运行的 shell 会话类型。有两种 shell 会话类型：一个是登录 shell 会话，另一个是非登录 shell 会话。

登录 shell 会话会在其中提示用户输入用户名和密码；例如，我们启动一个虚拟控制台会话。非登录 shell 会话通常当我们在 GUI 下启动终端会话时出现。

表12-2: 登录 shell 会话的启动文件

| 文件            | 内容                                                         |
| --------------- | ------------------------------------------------------------ |
| /etc/profile    | 应用于所有用户的全局配置脚本。                               |
| ~/.bash_profile | 用户个人的启动文件。可以用来扩展或重写全局配置脚本中的设置。 |
| ~/.bash_login   | 如果文件 ~/.bash_profile 没有找到，bash 会尝试读取这个脚本。 |
| ~/.profile      | 如果文件 ~/.bash_profile 或文件 ~/.bash_login 都没有找到，bash 会试图读取这个文件。这是基于 Debian 发行版的默认设置，比方说 Ubuntu。 |

表12-3: 非登录 shell 会话的启动文件

| 文件             | 内容                                                         |
| ---------------- | ------------------------------------------------------------ |
| /etc/bash.bashrc | 应用于所有用户的全局配置文件。                               |
| ~/.bashrc        | 用户个人的启动文件。可以用来扩展或重写全局配置脚本中的设置。 |

除了读取以上启动文件之外，非登录 shell 会话也会继承它们父进程的环境设置，通常是一个登录 shell。



PATH 变量经常（但不总是，依赖于发行版）在 /etc/profile 启动文件中设置，通过这些代码：

```shell
PATH=$PATH:$HOME/bin
```

修改 PATH 变量，添加目录 $HOME/bin 到目录列表的末尾。这是一个参数展开的实例，参数展开我们在第八章中提到过。为了说明这是怎样工作的，试试下面的例子：

```
[me@linuxbox ~]$ foo="This is some"
[me@linuxbox ~]$ echo $foo
This is some
[me@linuxbox ~]$ foo="$foo text."
[me@linuxbox ~]$ echo $foo
This is some text.
```

使用这种技巧，我们可以把文本附加到一个变量值的末尾。通过添加字符串 $HOME/bin 到 PATH 变量值的末尾，则目录 $HOME/bin 就添加到了命令搜索目录列表中。这意味着当我们想要在自d己的家目录下，创建一个目录来存储我们自己的私人程序时，shell 已经给我们准备好了\



```
export PATH
```

这个 export 命令告诉 shell 让这个 shell 的子进程可以使用 PATH 变量的内容。

### 文本编辑器

文本编辑器分为两种基本类型：图形化的和基于文本的编辑器。GNOME 和 KDE 两者都包含一些流行的
图形化编辑器。GNOME 自带了一个叫做 gedit 的编辑器，这个编辑器通常在 GNOME 菜单中称为”文本编辑器”。
KDE 通常自带了三种编辑器，分别是（按照复杂度递增的顺序排列）kedit，kwrite，kate。

有许多基于文本的编辑器。你将会遇到一些流行的编辑器，它们是 nano、vi和 emacs。 nano 编辑器
是一个简单易用的编辑器，用于替代随 PINE 邮件套件提供的 pico 编辑器。vi 编辑器
（在大多数 Linux 系统中被 vim 替代，vim 是 “Vi IMproved”的简写）是类 Unix 操作系统的传统编辑器。
vim 是我们下一章节的讨论对象。emacs 编辑器最初由 Richard Stallman 写成。它是一个庞大、多用途的，
可做任何事情的编程环境。虽然 emacs 很容易获取，但是大多数 Linux 系统很少默认安装它。

##### nano

因为设计 nano 是为了代替由电子邮件客户端提供的编辑器的，所以它相当缺乏编辑特性。在任一款编辑器中，你应该学习的第一个命令是怎样退出程序。以 nano 为例，你输入 Ctrl-x 来退出 nano。在屏幕底层的菜单中说明了这个命令。”^X” 表示法意思是 Ctrl-x。这是控制字符的常见表示法，许多程序都使用它。

### 修改 shell 环境

当我们编辑一个重要的配置文件时，首先创建一个这个文件的备份总是一个不错的主意。这样能避免我们在编辑文件时弄乱文件。创建文件 .bashrc 的备份文件，这样做：

```
[me@linuxbox ~]$ cp .bashrc .bashrc.bak
```

### 激活我们的修改

我们对于文件 .bashrc 的修改不会生效，直到我们关闭终端会话，再重新启动一个新的会话，因为 .bashrc 文件只是在刚开始启动终端会话时读取。然而，我们可以强迫 bash 重新读取修改过的 .bashrc 文件，使用下面的命令：

```
[me@linuxbox ~]$ source .bashrc
```

## 进程

通常，现在的操作系统都支持多任务，意味着操作系统通过在一个执行中的程序和另一个 程序之间快速地切换造成了一种它同时能够做多件事情的假象。Linux 内核通过使用进程来 管理多任务。进程，就是Linux 组织安排正在等待使用 CPU的各种程序的方式。

有时候，计算机变得呆滞，运行缓慢，或者一个应用程序停止响应。在这一章中，我们将看一些 可用的命令行工具，这些工具帮助我们查看程序的执行状态，以及怎样终止行为不当的进程。

This chapter will introduce the following commands:

- ps – Report a snapshot of current processes

- top – Display tasks

- jobs – List active jobs

- bg – Place a job in the background

- fg – Place a job in the foreground

- kill – Send a signal to a process

- killall – Kill processes by name

- shutdown – Shutdown or reboot the system

- ps – 报告当前进程快照

- top – 显示任务

- jobs – 列出活跃的任务

- bg – 把一个任务放到后台执行

- fg – 把一个任务放到前台执行

- kill – 给一个进程发送信号

- killall – 杀死指定名字的进程

- shutdown – 关机或重启系统

  

  ### 查看进程 

  

默认情况下，ps 不会显示很多进程信息，只是列出与当前终端会话相关的进程。为了得到更多信息， 我们需要加上一些选项，但是在这样做之前，我们先看一下 ps 命令运行结果的其它字段。 TTY 是 “Teletype” 的简写，是指进程的控制终端。这里，Unix 展示它的年龄。TIME 字段表示 进程所消耗的 CPU 时间数量。

默认情况下，ps 不会显示很多进程信息，只是列出与当前终端会话相关的进程。为了得到更多信息， 我们需要加上一些选项，但是在这样做之前，我们先看一下 ps 命令运行结果的其它字段。 TTY 是 “Teletype” 的简写，是指进程的控制终端。这里，Unix 展示它的年龄。TIME 字段表示 进程所消耗的 CPU 时间数量。

输出结果中，新添加了一栏，标题为 STAT 。STAT 是 “state” 的简写，它揭示了进程当前状态：

| 状态 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| R    | 运行中。这意味着，进程正在运行或准备运行。                   |
| S    | 正在睡眠。进程没有运行，而是，正在等待一个事件， 比如说，一个按键或者网络分组。 |
| D    | 不可中断睡眠。进程正在等待 I/O，比方说，一个磁盘驱动器的 I/O。 |
| T    | 已停止. 已经指示进程停止运行。稍后介绍更多。                 |
| Z    | 一个死进程或“僵尸”进程。这是一个已经终止的子进程，但是它的父进程还没有清空它。 （父进程没有把子进程从进程表中删除） |
| <    | 一个高优先级进程。这可能会授予一个进程更多重要的资源，给它更多的 CPU 时间。 进程的这种属性叫做 niceness。具有高优先级的进程据说是不好的（less nice）， 因为它占用了比较多的 CPU 时间，这样就给其它进程留下很少时间。 |
| N    | 低优先级进程。 一个低优先级进程（一个“好”进程）只有当其它高优先级进程被服务了之后，才会得到处理器时间。 |

另一个流行的选项组合是 “aux”（不带开头的”-“字符）。

这个选项组合，能够显示属于每个用户的进程信息。使用这个选项，可以唤醒 “BSD 风格” 的输出结果。 Linux 版本的 ps 命令，可以模拟几个不同 Unix 版本中的 ps 程序的行为。通过这些选项，我们得到 这些额外的列。

| 标题  | 含义                                             |
| ----- | ------------------------------------------------ |
| USER  | 用户 ID. 进程的所有者。                          |
| %CPU  | 以百分比表示的 CPU 使用率                        |
| %MEM  | 以百分比表示的内存使用率                         |
| VSZ   | 虚拟内存大小                                     |
| RSS   | 进程占用的物理内存的大小，以千字节为单位。       |
| START | 进程启动的时间。若它的值超过24小时，则用天表示。 |

## 查找文件

### which- 显示会执行哪个可执行程序

### whereis

### locate - 查找文件的简单方法

这个 locate 程序会执行一次快速的路径名数据库搜索，并且输出每个与给定子字符串相匹配的路径名。比如说， 例如，我们想要找到所有名字以“zip”开头的程序。因为我们正在查找程序，可以假定包含 程序的目录以”bin/”结尾。因此，我们试着以这种方式使用 locate 命令，来找到我们的文件：

```
[me@linuxbox ~]$ locate bin/zip
```

locate 命令将会搜索它的路径名数据库，输出任一个包含字符串“bin/zip”的路径名：

### find - 查找文件的复杂方式

locate 程序只能依据文件名来查找文件，而 find 程序能基于各种各样的属性 搜索一个给定目录（以及它的子目录），来查找文件。我们将要花费大量的时间学习 find 命令，因为 它有许多有趣的特性，当我们开始在随后的章节里面讨论编程概念的时候，我们将会重复看到这些特性。

在它的最简单的使用方式中，find 命令接收一个或多个目录名来执行搜索搜索。例如，输出我们的家目录的路径名列表（包括文件及目录，译者注）。

```
[me@linuxbox ~]$ find ~
```

#### Tests

比如说我们想在我们的搜索中得到目录列表。我们可以添加以下测试条件：

```
[me@linuxbox ~]$ find ~ -type d | wc -l
1695
```

添加测试条件-type d 限制了只搜索目录。相反地，我们可以使用这个测试条件来限定搜索普通文件：

```
[me@linuxbox ~]$ find ~ -type f | wc -l
38737
```

这里是 find 命令支持的常见文件类型测试条件：

| File Type | Description                   |
| --------- | ----------------------------- |
| b         | Block special device file     |
| c         | Character special device file |
| d         | Directory                     |
| f         | Regular file                  |
| l         | Symbolic link                 |

| 文件类型 | 描述             |
| -------- | ---------------- |
| b        | 块特殊设备文件   |
| c        | 字符特殊设备文件 |
| d        | 目录             |
| f        | 普通文件         |
| l        | 符号链接         |

我们也可以通过加入一些额外的测试条件，根据文件大小和文件名来搜索：让我们查找所有文件名匹配 通配符模式“*.JPG”和文件大小大于1M 的普通文件：

```
[me@linuxbox ~]$ find ~ -type f -name "*.JPG" -size +1M | wc -l
```

面的字符可以 被用来指定测量单位：

| Character | Unit                                                         |
| --------- | ------------------------------------------------------------ |
| b         | 512 byte blocks. This is the default if no unit is specified. |
| c         | Bytes                                                        |
| w         | Two byte words                                               |
| k         | Kilobytes (Units of 1024 bytes)                              |
| M         | Megabytes (Units of 1048576 bytes)                           |
| G         | Gigabytes (Units of 1073741824 bytes)                        |

| 字符 | 单位                                           |
| ---- | ---------------------------------------------- |
| b    | 512 个字节块。如果没有指定单位，则这是默认值。 |
| c    | 字节                                           |
| w    | 两个字节的字                                   |
| k    | 千字节(1024个字节单位)                         |
| M    | 兆字节(1048576个字节单位)                      |
| G    | 千兆字节(1073741824个字节单位)                 |

| 测试条件       | 描述                                                         |
| -------------- | ------------------------------------------------------------ |
| -cmin n        | 匹配内容或属性最后修改时间正好在 n 分钟之前的文件或目录。 指定少于 n 分钟之前，使用 -n，指定多于 n 分钟之前，使用 +n。 |
| -cnewer file   | 匹配内容或属性最后修改时间晚于 file 的文件或目录。           |
| -ctime n       | 匹配内容和属性最后修改时间在 n*24小时之前的文件和目录。      |
| -empty         | 匹配空文件和目录。                                           |
| -group name    | 匹配属于一个组的文件或目录。组可以用组名或组 ID 来表示。     |
| -iname pattern | 就像-name 测试条件，但是不区分大小写。                       |
| -inum n        | 匹配 inode 号是 n的文件。这对于找到某个特殊 inode 的所有硬链接很有帮助。 |
| -mmin n        | 匹配内容被修改于 n 分钟之前的文件或目录。                    |
| -mtime n       | 匹配的文件或目录的内容被修改于 n*24小时之前。                |
| -name pattern  | 用指定的通配符模式匹配的文件和目录。                         |
| -newer file    | 匹配内容晚于指定的文件的文件和目录。这在编写执行备份的 shell 脚本的时候很有帮。 每次你制作一个备份，更新文件（比如说日志），然后使用 find 命令来判断哪些文件自从上一次更新之后被更改了。 |
| -nouser        | 匹配不属于一个有效用户的文件和目录。这可以用来查找 属于被删除的帐户的文件或监测攻击行为。 |
| -nogroup       | 匹配不属于一个有效的组的文件和目录。                         |
| -perm mode     | 匹配权限已经设置为指定的 mode的文件或目录。mode 可以用 八进制或符号表示法。 |
| -samefile name | 类似于-inum 测试条件。匹配和文件 name 享有同样 inode 号的文件。 |
| -size n        | 匹配大小为 n 的文件                                          |
| -type c        | 匹配文件类型是 c 的文件。                                    |
| -user name     | 匹配属于某个用户的文件或目录。这个用户可以通过用户名或用户 ID 来表示。 |

This is not a complete list. The find man page has all the details.

这不是一个完整的列表。find 命令手册有更详细的说明。



## 文件系统

#### 为什么需要卸载(umount)设备

> Why Unmounting Is Important
>
> 为什么卸载重要
>
> If you look at the output of the free command, which displays statistics about memory usage, you will see a statistic called “buffers.” Computer systems are designed to go as fast as possible. One of the impediments to system speed is slow devices. Printers are a good example. Even the fastest printer is extremely slow by computer standards. A computer would be very slow indeed if it had to stop and wait for a printer to finish printing a page. In the early days of PCs (before multi-tasking), this was a real problem. If you were working on a spreadsheet or text document, the computer would stop and become unavailable every time you printed. The computer would send the data to the printer as fast as the printer could accept it, but it was very slow since printers don’t print very fast. This problem was solved by the advent of the printer buffer, a device containing some RAM memory that would sit between the computer and the printer. With the printer buffer in place, the computer would send the printer output to the buffer and it would quickly be stored in the fast RAM so the computer could go back to work without waiting. Meanwhile, the printer buffer would slowly spool the data to the printer from the buffer’s memory at the speed at which the printer could accept it.
>
> 如果你看一下 free 命令的输出结果，这个命令用来显示关于内存使用情况的统计信息，你 会看到一个统计值叫做”buffers“。计算机系统旨在尽可能快地运行。系统运行速度的 一个阻碍是缓慢的设备。打印机是一个很好的例子。即使最快速的打印机相比于计算机标准也 极其地缓慢。一台计算机确实会运行地非常慢，如果它要停下来等待一台打印机打印完一页。 在早期的个人电脑时代（多任务之前），这真是个问题。如果你正在编辑电子表格 或者是文本文档，每次你要打印文件时，计算机都会停下来而且变得不能使用。 计算机能以打印机可接受的最快速度把数据发送给打印机，但由于打印机不能快速地打印， 这个发送速度会非常慢。由于打印机缓存的出现，这个问题被解决了。打印机缓存是一个包含一些 RAM 内存 的设备，位于计算机和打印机之间。通过打印机缓存，计算机把要打印的结果发送到这个缓存区， 数据会迅速地存储到这个 RAM 中，这样计算机就能回去工作，而不用等待。与此同时，打印机缓存将会 以打印机可接受的速度把缓存中的数据缓慢地输出给打印机。
>
> This idea of buffering is used extensively in computers to make them faster. Don’t let the need to occasionally read or write data to/from slow devices impede the speed of the system. Operating systems store data read from, and to be written to storage devices in memory for as long as possible before actually having to interact with the slower device. On a Linux system for example, you will notice that the system seems to fill up memory the longer it is used. This does not mean Linux is “using“ all the memory, it means that Linux is taking advantage of all the available memory to do as much buffering as it can.
>
> 缓存被广泛地应用于计算机中，使其运行地更快。别让偶尔地读取或写入慢设备的需求阻碍了 系统的运行速度。在真正与比较慢的设备交互之前，操作系统会尽可能多的读取或写入数据到内存中的 存储设备里。以 Linux 操作系统为例，你会注意到系统看似填充了多于它所需要的内存。 这不意味着 Linux 正在使用所有的内存，它意味着 Linux 正在利用所有可用的内存，来作为缓存区。
>
> This buffering allows writing to storage devices to be done very quickly, because the writing to the physical device is being deferred to a future time. In the meantime, the data destined for the device is piling up in memory. From time to time, the operating system will write this data to the physical device.
>
> 这个缓存区允许非常快速地写入存储设备，因为写入物理设备的操作被延迟到后面进行。同时， 这些注定要传送到设备中的数据正在内存中堆积起来。时不时地，操作系统会把这些数据 写入物理设备。
>
> Unmounting a device entails writing all the remaining data to the device so that it can be safely removed. If the device is removed without unmounting it first, the possibility exists that not all the data destined for the device has been transferred. In some cases, this data may include vital directory updates, which will lead to file system corruption, one of the worst things that can happen on a computer.
>
> **卸载一个设备需要把所有剩余的数据写入这个设备，所以设备可以被安全地移除**。如果 没有卸载设备，就移除了它，就有可能没有把注定要发送到设备中的数据输送完毕。在某些情况下， 这些数据可能包含重要的目录更新信息，这将导致文件系统损坏，这是发生在计算机中的最坏的事情之一。

### 如何挂载设备

这个 mount 命令被用来挂载文件系统。执行这个不带参数的命令，将会显示 一系列当前挂载的文件系统

#### 确定设备名

首先，启动一个实时查看文件/var/log/messages （你可能需要超级用户权限）：

```
[me@linuxbox ~]$ sudo tail -f /var/log/messages
```

 [ubuntu16.04 没有/var/log/messages解决办法](https://blog.csdn.net/xtydtc/article/details/54342190)

这个设备名称是/dev/sdb 指整个设备，/dev/sdb1是这个设备的第一分区。

#### 进行挂载: 

简单地说，一个挂载点就是文件系统树中的一个目录。它没有 什么特殊的。它甚至不必是一个空目录，如果你把设备挂载到了一个非空目录上，你将不能看到 这个目录中原来的内容，直到你卸载这个设备。

```
[me@linuxbox ~]$ sudo mkdir /mnt/flash
[me@linuxbox ~]$ sudo mount /dev/sdb1 /mnt/flash
```

运行`df`查看挂载设备