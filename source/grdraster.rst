.. index:: ! grdraster

grdraster
=========

:官方文档: :ref:`gmt:grdraster`
:简介: 从二进制数据中提取子区域并保存为GMT网格文件

该命令会读取根据 ``grdraster.info`` 的内容，读取指定的二进制数据，从中提取出一个区域里的数据，并保存为网格文件。

``grdraster.info`` 位于 ``${GMTHOME}/share/dbase`` 目录下，文件内容的格式为::

    文件号 文件标题 Z值单位 -R范围 -I间隔  配准方式  数据格式 scale offset NaN 文件名

具体的细节在文件的注释中都有介绍。

该文件的作用在于，指定了本地二进制文件的基本信息，使得GMT可以精确地知道二进制数据的格式，进而可以准确读取二进制文件的内容。

选项
----

``<filenumber>``
    ``grdraster.info`` 中某文件所对应的文件号。或者也可以使用 ``text pattern`` 找到 ``grdraster.info`` 中数据描述中匹配的行。

``-G<grdfile>``
    默认会直接将数据以ASCII表的形式输出到标准输出流。使用该选项，则会将数据写到网格文件中

``-I<xinc>[<unit>][=|+]/<yinc>[<unit>][=|+]``
    指定X和Y方向的网格间隔

    - ``<xinc>`` X方向的网格间隔
    - ``<yinc>`` Y方向的网格间隔
    - ``<unit>`` 网格间隔的单位
    - ``=`` 微调X和Y方向范围的最大值，使得其是网格间隔的整数倍（默认会微调网格间隔以适应给定的数据范围）
    - ``+`` 表明 ``<xinc>`` 和 ``<yinc>`` 不是网格间隔，而是X和Y方向的节点数

示例
----

::

    gmt grdraster 1 -R-4/364/-62/62 -I30m -Gdata.nc
    gmt grdraster ETOPO2 -R160/20/220/30r -Joc190/25.5/292/69/1 -Gdata.nc
    gmt grdraster "2 min Geoware" -R20/25/-10/5 -bo > triplets.b
