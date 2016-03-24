.. index:: ! grdlandmask

grdlandmask
===========

:官方文档: :ref:`gmt:grdlandmask`
:简介: 根据海岸线数据创建陆地-海洋的mask网格文件

该命令会根据海岸线数据，确定指定网格内的每个节点是在陆地上还是在水中，并给节点赋予不同的值。

选项
----

``-G<mask_grd_file>``
    生成的mask网格文件的文件名

``-I<xinc>[<unit>][=|+]/<yinc>[<unit>][=|+]``
    指定X和Y方向的网格间隔。见 :doc:`xyz2grd` 中的介绍。

``-A``
    不考虑面积过小的湖泊的边界，或不考虑某个级别的湖泊边界。见 :doc:`pscoast` 中的介绍。

``-D<resolution>[+]``
    选项海岸线数据的精度，见 :doc:`pscoast` 中的介绍。

``-N<maskvale>[o]``
    设置网格节点的值，可以是数字，也可以是NaN。 ``o`` 表示将位于边界处的节点当做在边界的外部。该选项可以取两种格式：

    #. ``-N<wet>/<dry>``
    #. ``-N<ocean>/<land>/<lake>/<island>/<pond>``

    默认值为 ``0/1/0/1/0`` （即 ``0/1`` ），即将水域内的网格设置为0，将陆地内的网格设置为1。


示例
----

将所有陆地上的节点设置为NaN，水域上的节点设置为1::

    gmt grdlandmask -R-60/-40/-40/-30 -Dh -I5m -N1/NaN -Gland_mask.nc -V

生成全球1x1度的网格，并将不同性质的区域设置成不同的值::

    gmt grdlandmask -R0/360/-90/90 -Dl -I1 -N0/1/2/3/4 -Glevels.nc -V
