.. index:: ! grdsample

grdsample
=========

:官方文档: :ref:`gmt:grdsample`
:简介: 对网格文件做重采样

该命令读取一个网格文件，并对其做插值以生成一个新的网格文件。新旧网格文件的区别在于：

#. 不同的配准方式（ ``-r`` 或 ``-T`` ）
#. 不同的网格间隔或网格节点数（ ``-I`` ）
#. 不同的网格范围（ ``-R`` ）

选项
----

``<in_grdfile>``
    要重采样的2D网格文件

``-G<out_grdfile>``
    重采样生成的网格文件

``-I<xinc>[<unit>][=|+]/<yinc>[<unit>][=|+]``
    指定X和Y方向的网格间隔，见 :doc:`xyz2grd` 中的介绍。

``-T``
    交换网格文件的配准方式。即若输入是网格线配准，则输出为像素点配准；若输入是像素点配准，则输出为网格线配准。

``-n[b|c|l|n][+a][+b<BC>][+c][+t<threshold>]``
    重采样时使用的插值算法，见 :ref:`doc:option-n` 一节。

示例
----

将5x5弧分的数据采样成1x1弧分::

    gmt grdsample hawaii_5by5_topo.nc -I1m -Ghawaii_1by1_topo.nc

将网格线配准的网格文件修改为像素配准的网格文件::

    gmt grdsample surface.nc -T -Gpixel.nc
