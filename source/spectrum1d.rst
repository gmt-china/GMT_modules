.. index:: ! spectrum1d

spectrum1d
==========

:官方文档: :ref:`gmt:spectrum1d`
:简介: 计算一个时间序列的自功率谱，或两个时间序列的互功率谱
:描述: spectrum1d 从标准终端或数据文件中，读取一列或两列数据。这些数据是等时间间隔采样得到的时间序列。spectrum1d采用Welch方法，即加窗多段平均周期图法，计算输出自功率或互功率谱密度。其输出的功率谱的标准差，是用Bendat和Piersol提供的算法。

spectrum1d的输出文件有三列：f或w, p和e。f或w代表频率或波长（相当于周期）。p代表计算的功率谱密度。e代表一个标准差的值。

spectrum1d的输出文件的文件名是基于name_stem命名。如果使用了-C选项，那么将会有8个文件输出，否则只有一个功率谱文件（.xpower）输出。
这些文件默认是以ASCII码格式，除非用-bo选项指定为二进制格式输出。这8个文件介绍如下。

name_stem.xpower
	X(t)的功率谱。单位是X*X*dt。
name_stem.ypower
	Y(t)的功率谱。单位是Y*Y*dt。
name_stem.cpower
	一致性（coherent)的功率谱。单位和*ypower一样。
name_stem.npower
	噪声的功率谱。单位和*ypower一样。
name_stem.gain
	增益谱，或传输函数的模。单位是(Y/X)
name_stem.phase
	相位谱，或传输函数的相位。单位是弧度。
name_stem.admit
	导纳（Admittance)谱，或传输函数的实部。单位是（Y/X）。
name_stem.coh
	（平方）相干谱，或者线性相关系数（它是频率的函数）。无单位，取值范围为[0,1]。
	信噪比SNR=coh/(1-coh)。当coh=0.5时，SNR=1。
以上文件会以单个文件单列输出。除非使用-T。

选项
----
必选项
----
-Ssegment_size
	segment_size是一个2的指数数值，它是为了控制Welch方法中分段平均时的窗口长度。它也决定了功率谱密度的最小频率分辨率和最大频率分辨率，即1.0/(segment_size*dt)和1.0/(2*dt)(即Nyquist频率)。在功率谙密度中的一个标准误差大约为1.0/(n_data/segment_size)，比如segment_size=256,那么就需要25600个数据点去计算一个误差棒的10%。互功率谱误差棒的计算则需要更多数据点，而且是相干性的函数，比较复杂。

----	
可选项
table
	输入文件名。它是ASCII类型的一列数据或两列数据。如果是一列数据文件，就计算自功率谱；如果是两列，就计算互功率谱。如果没有此文件名，spectrum1d将会从屏幕上读取数据。

-C[xycnpago]
	选择性地输出8个文件，如果不规定其中一个，那么8个文件全部输出。x=xpower,y=ypower,c=cpower,n=npower,p=phase,a=admit,g=gain,o=coh.

-Ddt
	规定时间序列的时间采样间隔。默认是1.

-L[m|h]
	不去信号中的线性趋势。默认情况下，在对信号进行变换处理时，会先去掉其中的线性趋势。m去掉其中的均值。h去掉其中的中值。

-N[name_stem]
	输出文件名的前缀。默认为spectrum。不加此选项，输出的8个文件会合到一个文件里。

-T
	不让单个分量的结果输出到stdout。

-W
	规定功率谱是周期的函数，而不是频率的函数。默认是频率的函数。

-bi[ncols][t]
	选择输入为二进制文件。默认为2列输入。
-bo[ncols][type]
	选择输出为二进制文件。默认为2列输出。

-d[i|o]nodata
	设定输入或输出数据中NaN的值。

-f[i|o]colinfo
	规定输入或输出文件列信息。

-g[a]x|y|d|X|Y|D|[col]z[+|-]gap[u]
	规定数据段区分标记和行间断。

-h[i|o][n][+c][+d][+rremark][+rtitle]
	跳过或生成文件头标记。

-icols[I][sscale][ooffset][,...]
	选择哪一列为输入数据。

-^ or just -
	打印这个命令的简短语法介绍。Windows下用-。

-+ or just +
	打印这个命令的简短语法介绍的扩展版本。

-? or no arguments
	打印这个命令的完整用法。
--version
	打印GMT版本信息，并退出。
-show-datedir
	打印GMT共享文件夹的全路径，并退出。

示例
1.假设g是重力数据，单位为mGal，空间采样间隔为1.5km。输入其功率谱，用mGal**2-Km表示。
	gmt spectrum1d data.g -S256 -D1.5 -Ndata
2.假设你除了有重力数据data.g之外，还有在相同地点测得的地形数据data.t，单位为m。计算二者之间的传输函数。即，data.t是输入，data.g是输出。
	paste data.t data.g | gmt spectrum1d -S256 -D1.5 -Ndata -C > results.txt
	
