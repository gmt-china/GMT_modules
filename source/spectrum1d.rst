.. index:: ! spectrum1d

spectrum1d
==========

:官方文档: :ref:`gmt:spectrum1d`
:简介: 计算一个时间序列的自功率谱，或两个时间序列的互功率谱
:描述: spectrum1d 从标准终端或数据文件中，读取一列或两列数据。这些数据是等时间间隔采样得到的时间序列。spectrum1d采用Welch方法，即加窗多段平均周期图法，计算输出自功率或互功率谱密度。其输出的功率谱的标准差，是用Bendat和Piersol提供的算法。

spectrum1d的输出文件有三列：f或w, p和e。
f或w代表频率或波长（相当于周期）。
p代表计算的功率谱密度。
e代表一个标准差的值。

spectrum1d的输出文件的文件名是基于name_stem命名。
如果使用了-C选项，那么将会有8个文件输出，否则只有一个功率谱文件（.xpower）输出。
这些文件默认是以ASCII码格式，除非用-bo选项指定为二进制格式输出。
这8个文件分别是::
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

