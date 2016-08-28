.. index:: ! spectrum1d

spectrum1d
==========

:官方文档: :ref:`gmt:spectrum1d`
:简介: 计算一个时间序列的自功率谱，或两个时间序列的互功率谱
:描述: spectrum1d 从标准终端或数据文件中，读取一列或两列数据。这些数据是等时间间隔采样得到的时间序列。spectrum1d采用Welch方法，即加窗多段平均周期图法，计算输出自功率或互功率谱密度。其输出的功率谱的标准差，是用Bendat和Piersol提供的算法。

选项
----

