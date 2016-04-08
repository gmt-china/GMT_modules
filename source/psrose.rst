.. index:: ! psrose

psrose
======

:官方文档: :ref:`gmt:psrose`
:简介: 绘制极坐标下的直方图（sector图、rose图或windrose图）

选项
----

``<table>``
    输入文件，数据格式为 ``length  azimuth``

    若输入文件中只有azimuth一列数据，则此时需要使用 ``-i`` 选项，此时所有的长度都默认为单位长度。

``-A[r]<sector_width>``
    指定扇页宽度，单位为度

    #. 默认扇页宽度为0，即windrose图
    #. 若扇页宽度不为0，则表示绘制sector图
    #. 若扇页宽度不为0，则使用了 ``r`` ，则表示绘制rose图

``-B``
    见 ``-B`` 选项的介绍。此处，X表示径向距离，Y表示方位角。Y轴的标签是图片的标题。

``-Cm|<mode_file>``
    绘制矢量以显示 ``<mode_file>`` 中指定的主方向。若使用 ``-Cm`` 则计算并绘制平均方向。

``-D``
    对扇页对偏移，使得其位于每个间隔的中间，即第一个扇页的中心在0度处

``-F``
    不绘制scale length bar，默认会在右下角绘制

``-G<fill>``
    绘制扇页的填充色

``-I``
    不绘制图形，计算 ``-R`` 选项所需要的参数

``-L[<wlabel>/<elabel>/<slabel>/<nlabel>]``
    指定0、90、180、270度处的标签。

    #. 对于full-circle图而言，默认值为 ``WEST/EAST/SOUTH/NORTH``
    #. 对于half-circle图而言，默认值为 ``90W/90E/-/0`` ，其中 ``-`` 表示不显示标签
    #. 只使用 ``-L`` 但无其他参数表示不显示所有标签

``-M<parameters>``
    与 ``-C`` 选项一起使用以修改矢量的属性。具体数据见 :ref:`doc:vectors` 一节

``-R<r0>/<r1>/<az_0>/<az_1>``
    指定绘图的半径和方位角范围。

``-S[n]<radial_scale>``
    指定圆的半径。

    ``-Sn`` 会将输入的半径归一化到0到1。

``-T``
    Specifies that the input data is orientation data (has a 180 degree
    ambiguity) instead of true 0-360 degree directions [Default].

``-W[v]<pen>``
    设置扇区边框的画笔属性。

    ``-Wv<pen>`` 可用于设置绘制矢量时所需的画笔属性。

``-Z<scale>``
    将数据的半径乘以 ``<scale>``

    比如 ``-Z0.001`` 会将数据的单位从m变成km。若不考虑半径，可以通过 ``-Zu`` 将所有的半径设置为单位长度。
