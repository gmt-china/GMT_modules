.. index:: ! fitcircle

fitcircle
=========

:官方文档: :ref:`gmt:fitcircle`
:简介: 拟合球面上数据点的平均位置及圆弧

该命令或从输入数据的前两列读取经纬度数据，并计算所有坐标点的平均位置以及可以拟合这些坐标点的大圆路径的pole。在计算时有两种计算方法，分别用 ``-L1`` 和 ``-L2`` 表示。

选项
----

``<table>``
    输入数据

``-L<norm>``

    - ``-L1`` 解法1，详见官方文档
    - ``-L2`` 解法2，详见官方文档
    - ``-L`` 或 ``-L3`` 同时输出解法1和解法2的结果

``-Ff|m|n|s|c``
    控制输出格式。

    正常情况下，该命令会将计算结果以较复杂的形式输出。使用 ``-F`` 选项，则只返回简单的坐标。 ``-F`` 后可以加上其他修饰符以指定要返回的坐标：

    - ``f`` Flat Earth mean location
    - ``m`` mean location
    - ``n`` north pole of great circle
    - ``s`` south pole of great circle
    - ``c`` pole of small circle and its colatitude, which requires ``-S``

``-S[<lat>]``
    拟合小圆弧而不是大圆弧，见官方文档

示例
----

如下命令，用两种计算方法拟合了数据的大圆弧路径和小圆弧路径，并借助 :doc:`project` 生成路径坐标。

.. literalinclude:: /scripts/fitcircle_ex1.sh
   :language: bash

.. figure:: /images/fitcircle_ex1.*
   :width: 600 px
   :align: center

   fitcircle示例
