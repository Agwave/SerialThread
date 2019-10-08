## 一、流程简述
程序可以参考：
https://blog.csdn.net/colcloud/article/details/42454839

这是我参考后简化的版本：
https://github.com/Agwave/SerialThread/blob/master/SerialThread.py

下面利用虚拟串口软件和串口通信助手软件对程序进行测试。

**利用虚拟串口软件虚拟出一对相连的串口COM1和COM2。用程序打开串口COM1，用串口通信助手打开COM2。然后就可以进行收发文字了。**

测试结果如下：（黑体字为发出的文字，绿体字为接收到的文字）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191004203746594.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019100420385483.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA1NTEx,size_16,color_FFFFFF,t_70)
## 二、具体流程
计算机的串口数量有限，有时可以利用虚拟串口软件得到虚拟串口。

虚拟串口软件可以虚拟出一对相连的虚拟串口。

串口通信助手有打开串口等许多功能，对于调试程序十分有用。

**虚拟串口软件我用的是VSPD。串口通信助手用的是UartAsssist。**

下载和安装比较简单。两个安装完成后。

**1. 打开VSPD（如下）**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191004210824149.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA1NTEx,size_16,color_FFFFFF,t_70)
**2. 点击Add pair添加一对串口(记住串口名）**

**3. 打开 串口通信助手（如下）**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191004211807941.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA1NTEx,size_16,color_FFFFFF,t_70)
**4. 在红色框中，串口号选择前面的其中一个虚拟串口号，然后点击打开**（需要时可调整参数）

**5. 修改程序中的串口号为另一个虚拟串口号（如下），运行程序**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191004212201634.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA1NTEx,size_16,color_FFFFFF,t_70)
即可互相收发文字。
