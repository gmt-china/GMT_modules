.. index:: ! gmtdefaults

gmtdefaults
===========

:官方文档: :ref:`gmt:gmtdefaults`
:简介: 列出所有GMT参数的值

该模块会列出GMT参数的当前值或系统默认值。

必须选项
--------

无

可选选项
--------

``-D[u|s]``
    打印系统默认参数。若不使用该选项，则打印当前默认参数。

    #. ``-D`` ：列出GMT系统默认参数值，即 ``${GMT}/share/conf/gmt.conf``
    #. ``-Du`` ：列出GMT的US单位制下的默认参数值，即 ``${GMT}/share/conf/gmt_US.conf``
    #. ``-Ds`` ：列出GMT的SI单位制下的默认参数值，即 ``${GMT}/share/conf/gmt_SI.conf``

示例
----

在当前目录生成一份 GMT 系统默认配置::

    gmt gmtdefaults -D > gmt.conf

搜索与 LABEL 有关的参数的值::
    
    gmt gmtdefaults | grep LABEL

BUGS
----

- ``-D`` 选项无效（v5.1.2）
