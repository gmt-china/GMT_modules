.. index:: ! gmtsimplify

gmtsimplify
===========

:官方文档: :ref:`gmt:gmtsimplify`
:简介: 使用Douglas-Peucker算法对线段做简化

该命令可以将一个复杂多边形进行简化，用一条直线代替一系列点，并保证每个点与直线的偏离都在可容忍的范围内。

选项
----

``-T<tolerance>[<unit>]``
    指定最大所能容忍的误差。默认单位为用户单位，也可以指定其他距离单位。

示例
----

将线段简化，可容忍误差为2千米::

    gmt simplify segment.d -T2k > new_segment.d
