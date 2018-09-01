#在切换cuda版本时
rm -rf /usr/local/cuda#删除之前创建的软链接
sudo ln -s /usr/local/cuda-8.0/ /usr/local/cuda/
nvcc --version #查看当前 cuda 版本

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2016 NVIDIA Corporation
Built on Mon_Jan_23_12:24:11_CST_2017
Cuda compilation tools, release 8.0, V8.0.62

#cuda8.0 切换到 cuda9.0 
rm -rf /usr/local/cuda
sudo ln -s /usr/local/cuda-9.0/ /usr/local/cuda/
nvcc --version


一、Ubuntu14.04命令行界面tty黑屏解决方法：
1、“ctrl+alt+t”打开终端，输入：(编辑grub文件)
sudo gedit /etc/default/grub 
2.、在文件中找到这一行：
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
改为：
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"
3、保存，关闭文件。在命令行中输入：（更新文件）
sudo update-grub
4、重启电脑即可。
二、Linux下配置Caffe及其Python接口全过程记录（Ubuntu14.04_amd64+CUDA8.0）及训练mnist数据集
一、安装显卡驱动
1.装显卡驱动，去nvidia下载吧，搜自己显卡的型号，linux64位的，提供链接：http://www.geforce.cn/drivers
2.下载后的文件应该是run文件，然后复制到一个目录下，我直接下载到主文件夹下了，注意：该路径千万不要有中文！！！然后将其改名为NVIDIA.run
3.下面要到文字界面输入，建议先看完教程或者从别处打开，再进行操作！！按下ctrl+alt+F1，进入文本界面，输入用户名密码（数字不要用小键盘输入），登录后输入sudo su -（注意su后面有个空格然后才是一个-），输入密码后进入root权限
4.停止用户界面Xserver。输入sudo /etc/init.d/lightdm stop，此时图形界面就关闭了，按下ctrl+alt+F7还是可以回到图形界面的。
5.回到主目录下 cd /home/XXX
6.给NVIDIA.run添加权限，输入sudo chmod +x NVIDIA.run（注意空格）
8.输入sudo ./NVIDIA.run，下一步下一步accept、continue、OK、YES、OK即可安装完驱动。
9.第八步，用reboot命令重启电脑。
10.第九步，正常进入图形界面，从终端中输入sudo lshw -c video，检查一下是否装好驱动，如果装好的话，应该会有以下文字：driver=nvidia

二、CUDA8.0安装
1、查询你的GPU是否支持CUDA，支持的话，请提前下载好CUDA8.0，我下载到了主文件夹下，提供链接：https://developer.nvidia.com/cuda-downloads/；（建议下载最新版本）
以及下载CUDNN V5，需要developer身份（注册），提供链接：https://developer.nvidia.com/cudnn
！注意都下成.run的格式。不然会很麻烦！
2、sudo sh cuda_8.0.44_linux.run。读完说明书，按Q键可直接跳到说明书最后。输入accept，注意当问到Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 361时（即第一个出现的问题，最后的数字因显卡驱动版本不同可能不同）。一定选择n！其他都选择yes。
3、安装完后显示如下：
Installing the CUDA Toolkit in /usr/local/cuda-8.0 …
Missing recommended library: libGLU.so
Missing recommended library: libX11.so
Missing recommended library: libXi.so
Missing recommended library: libXmu.so
Installing the CUDA Samples in /home/guan …
Copying samples to /home/zhou/NVIDIA_CUDA-8.0_Samples now…
Finished copying samples.
===========
= Summary =
===========
Driver: Not Selected
Toolkit: Installed in /usr/local/cuda-8.0
Samples: Installed in /home/zhou, but missing recommended libraries
4、输入nvidia-smi看是否安装成功

三、安装cudnn
1、将CUDNN的文件复制到cuda路径下：首先进入cudnn下载的zip文件提取，右键直接提取到此处即可，然后cd cuda 发现里面有两个文件夹 include和lib64；终端cd进入cuda文件夹，输入命令
sudo cp ./include/* /usr/local/cuda/include
sudo cp ./lib64/* /usr/local/cuda/lib64/
拷贝之后需要
cd /usr/local/cuda/lib64
sudo rm libcudnn.so.5
sudo rm libcudnn.so
然后
sudo ln -s libcudnn.so.5.1.5 libcudnn.so.5
sudo ln -s libcudnn.so.5 libcudnn.so
（执行完检查一下文件是否复制到了指定位置）

2、安装各种库，大概有那么二三十个吧。命令是sudo apt-get install Git.然后sudo apt-get update

3、sudo apt-get install git autoconf automake libtool libprotobuf-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-serial-dev protobuf-compiler libleveldb-dev liblmdb-dev Python-gflags cmake libgflags-dev libgoogle-glog-dev libatlas-dev liblapack-dev libatlas-base-dev python-numpy python-setuptools python-scipy python-matplotlib python-sklearn python-skimage python-h5py python-protobuf python-leveldb python-networkx python-nose python-pandas python-gflags Cython ipython

4、此时git已经装完，可以git clone了。输入sudo git clone --recursive https://github.com/bvlc/caffe.git
5、sudo chmod 777 -R caffe/
6、进入caffe目录：cd /home/XXX/caffe （XXX是你的用户名）
7、将makefile.config.example用cp复制一份到当前目录sudo cp Makefile.config.example Makefile.config，将文件名字改为makefile.config。用gedit makefile.config修改此文件。将use_cudnn：=1的那行的注释符删掉，改matlab的路径为MATLAB_DIR：=/usr/local/MATLAB/R2014a/
8.第七步，sudo make -j 16
9.第八步，此时应该caffe就编译结束了，生成的文件在/caffe/tools下


四、安装Matlab
假设用U盘拷贝安装文件
1、cp /media/电脑名字/xxxx(u盘名字)/MATHWORKS.R2014a.iso ~
2、sudo mount MATHWORKS.R2014a.iso matlab/
3、sudo ./matlab/install   一步一步安装，激活码先随便输一个。之后不选择联网激活，而使用本地的破解证书
4、sudo cp /media/电脑名字/U盘名字/matlab2014a/Crack/Linux/libmwservices.so /usr/local/MATLAB/R2014a/bin/glnxa64/
5、sudo /usr/local/MATLAB/R2014a/bin/matlab打开matlab
6、sudo make matcaffe
7、让caffe重新编译：sudo make superclean
8、sudo make mattest
9、如果出现什么lib库找不到的情况cannot open shared object file, no such file or directory，请sudo ldconfig /usr/local/cuda/lib64

Python:
1.第一步，如果python的所有库都安装没问题的话，应该就能够直接在caffe根目录下运行make pycaffe -j 32
2.第二步，之后将python的路径添加进环境变量，命令为export PYTHONPATH=/home/xxxxxxx/caffe/python:$PYTHONPATH
3.第三步，输入python进入python编辑器，输入import caffe，不报错即可。

Mnist:
Cd进入caffe
Sudo ./data/mnisit/get_mnist.sh
Sudo ./examples/mnisit/create_mnist.sh
Sudo ./examples/mninst/train_lenet.sh


ubuntu中如何将一个文件夹里面的所有文件夹和文件添加777权限
sudo chmod -R 777 /…


